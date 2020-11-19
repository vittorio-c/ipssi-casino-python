import sqlite3
import sys
from sqlite3 import Error as DatabaseError
from .User import User

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
                                        id INTEGER PRIMARY KEY,
                                        user_name VARCHAR(64) NOT NULL,
                                        is_first_time TINYINT DEFAULT 1,
                                        last_level TINYINT DEFAULT 1,
                                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                                        solde INTEGER DEFAULT 10
                                    ); """
        try:
            cursor = self.connexion.cursor()
            cursor.execute(sql_create_user_table)
        except DatabaseError as e:
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
