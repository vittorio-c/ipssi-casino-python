import sys
from classes.User import User
from classes.Database.DBConnection import DBConnection

class UserRepository :

    def createUser(self, user_name):
        bindings = tuple([user_name])

        sql = ''' INSERT INTO users (user_name)
                  VALUES(?) '''

        user_id = DBConnection.insert_data(sql, bindings)
        user_model = self.getUserById(user_id)

        return user_model

    def getUserById(self, user_id):
        bindings = tuple([user_id])

        sql = ''' SELECT * FROM users WHERE users.id = ? '''

        user_row = DBConnection.get_data(sql, bindings)
        user_id, user_name, is_first_time, last_level, created_at, solde = list(user_row[0])
        user_model = User(user_id, user_name, is_first_time, last_level, created_at, solde)

        return user_model

    def getUserByName(self, user_name):
        bindings = tuple([user_name])

        sql = ''' SELECT * FROM users WHERE users.user_name =? '''

        user_row = DBConnection.get_data(sql, bindings)

        if user_row :
            user_id, user_name, is_first_time, last_level, created_at, solde = list(user_row[0])
            user_model = User(user_id, user_name, is_first_time, last_level, created_at, solde)
        else:
            user_model = None

        return user_model

    def updateUser(self, user_model):
        bindings = user_model.__dict__

        sql = '''
                UPDATE users
                SET
                    user_name = :user_name,
                    is_first_time = :is_first_time,
                    last_level = :last_level,
                    solde = :solde
                WHERE id = :user_id '''
        user_id = DBConnection.insert_data(sql, bindings)
        user_model = self.getUserById(bindings['user_id'])

        return user_model
