import sqlite3
import sys
from sqlite3 import Error as DatabaseError
from .User import User
from .Stat import Stat

class SqliteDatabase :
    """ Permet de créer la connexion et les interractions avec la base de données """

    # Voir comment créer une connexion tout en s'assurant de la fermer
    # https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class

    database_file_name = r'.sqlite_database.db'
    connexion = None

    def __init__(self):
        try:
            self.connexion = sqlite3.connect(self.database_file_name)
            self.connexion.row_factory = sqlite3.Row
            self.createTables()
        except DatabaseError as e:
            print(e)

    def getConnection(self):
        return self.connexion

    def createTables(self):
        sql_create_user_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY NOT NULL,
                                        user_name VARCHAR(64) NOT NULL,
                                        is_first_time TINYINT DEFAULT 1,
                                        last_level TINYINT DEFAULT 1,
                                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                                        solde INTEGER DEFAULT 10
                                    ); """

        sql_create_stats_table = """ CREATE TABLE IF NOT EXISTS stats (
                                        id INTEGER PRIMARY KEY NOT NULL,
                                        user_id INTEGER NOT NULL,
                                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                                        level TINYINT NOT NULL,
                                        attempts INT NOT NULL,
                                        bet INT,
                                        profit INT,
                                        result TINYINT NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (id)
                                    ); """

        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql_create_user_table)
        except DatabaseError as e:
            cursor.execute(sql_create_stats_table)
            raise e

    def createUser(self, user_name):
        bindings = tuple([user_name])

        sql = ''' INSERT INTO users(user_name)
                  VALUES(?) '''

        try:
            cursor = self.connexion.cursor()
            # préparation de la requête
            cursor.execute(sql, bindings)
            # insertion des données
            self.connexion.commit()

            userId = cursor.lastrowid
        except DatabaseError as e:
            print(e)

        return self.getUserById(userId)

    def updateUser(self, user_model):
        bindings = user_model.__dict__

        sql = '''
                UPDATE users
                SET
                    user_name = :user_name,
                    is_first_time = :is_first_time,
                    last_level = :last_level,
                    solde = :solde
                WHERE id = :user_id
              '''
        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql, bindings)
            self.connexion.commit()
        except DatabaseError as e:
            print(e)

        return self.getUserById(bindings['user_id'])

    def getUserById(self, user_id):
        bindings = tuple([user_id])

        sql = ''' SELECT * FROM users WHERE users.id =? '''

        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql, bindings)

            user_row = cursor.fetchone()
        except DatabaseError as e:
            print(e)

        user_id, user_name, is_first_time, last_level, created_at, solde = list(user_row)

        user_model = User(user_id, user_name, is_first_time, last_level, created_at, solde)
        return user_model

    def getUserByName(self, user_name):
        bindings = tuple([user_name])

        sql = ''' SELECT * FROM users WHERE users.user_name =? '''

        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql, bindings)

            user_row = cursor.fetchone()
        except DatabaseError as e:
            print(e)

        if user_row is not None:
            user_id, user_name, is_first_time, last_level, created_at, solde = list(user_row)
            user_model = User(user_id, user_name, is_first_time, last_level, created_at, solde)
        else:
            user_model = None

        return user_model

    def createStats(self, stats_model):
        bindings = stats_model.__dict__

        sql = ''' INSERT INTO stats(user_id, level, attempts, bet, profit, result)
                  VALUES(:user_id, :level, :attempts, :bet, :profit, :result) '''

        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql, bindings)
            self.connexion.commit()

            statId = cursor.lastrowid
        except DatabaseError as e:
            print(e)

        return self.getStatById(statId)

    def getStatById(self, stat_id):
        bindings = tuple([stat_id])

        sql = ''' SELECT * FROM stats WHERE stats.id = ? '''

        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql, bindings)

            stats_row = cursor.fetchone()
        except DatabaseError as e:
            print(e)

        stat_id, user_id, created_at, level, attempts, bet, profit, result = list(stats_row)

        stat_model = Stat(user_id, level, attempts, bet, profit, result, created_at, stat_id)
        return stat_model

    def getStatsByUserId(self, user_id) :
        bindings = tuple([user_id])

        sql = ''' SELECT * FROM stats WHERE stats.user_id = ? '''

        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql, bindings)

            stats_rows = cursor.fetchall()
        except DatabaseError as e:
            print(e)

        results = []

        for row in stats_rows:
            stat_id, user_id, created_at, level, attempts, bet, profit, result = list(row)

            stat_model = Stat(user_id, level, attempts, bet, profit, result, created_at, stat_id)

            results.append(stat_model)

        return results

