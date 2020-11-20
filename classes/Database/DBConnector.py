import sqlite3
from sqlite3 import Error as DatabaseError
from .Singleton import Singleton

@Singleton
class DBConnector(object):

    database_file_name = r'.sqlite_database.db'

    def __init__(self):
        """Initialize database connection and creates neccesary tables once for all """
        try:
            self.connection = sqlite3.connect(self.database_file_name)
            self.connection.row_factory = sqlite3.Row
            print('HELLOOOOO HELLOOOOO HELLOOOOO HELLOOOOO')
            self.createTables()
        except DatabaseError as e:
            print(e)

    def __str__(self):
        return 'Database connection object'

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
            cursor = self.connection.cursor()
            cursor.execute(sql_create_user_table)
            cursor.execute(sql_create_stats_table)
        except DatabaseError as e:
            raise e
