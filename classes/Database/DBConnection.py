from .DBConnector import DBConnector
from sqlite3 import Error as DatabaseError
import sys

class DBConnection(object):

    @classmethod
    def get_connector(cls):
        """Creates or return new Singleton database connection"""
        cls.connector = DBConnector.Instance()
        print("Id of Instance Connector : {}".format(str(id(cls.connector))))

        return cls.connector

    @classmethod
    def get_data(cls, query, bindings):
        try:
            connector = cls.get_connector()
            cursor = connector.connection.cursor()
            cursor.execute(query, bindings)
        except DatabaseError as e:
            print(e)

        result = cursor.fetchall()
        cursor.close()

        return result

    @classmethod
    def insert_data(cls, query, bindings):
        try:
            connector = cls.get_connector()
            cursor = connector.connection.cursor()
            cursor.execute(query, bindings)

            connector.connection.commit()
        except DatabaseError as e:
            print(e)

        last_row_id = cursor.lastrowid
        cursor.close()

        return last_row_id
