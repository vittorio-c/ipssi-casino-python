from classes.User import User
from classes.Database.Repository.UserRepository import UserRepository

class UserController :
    """ Permet de réaliser des opérations sur les users"""

    def __init__(self) :
        self.user_repo = UserRepository()

    def getUserByName(self, user_name) :
        """ Récupère le user via son nom depuis la base de données"""
        user = self.user_repo.getUserByName(user_name)

        return user

    def createUser(self, user_name) :
        """ Insert un user en base de données """

        return self.user_repo.createUser(user_name)


    def updateUser(self, user_model) :
        """ Update un user en base de données """
        try:
            if not isinstance(user_model, User) :
                raise TypeError()

            self.validateUserData(user_model)
            return self.user_repo.updateUser(user_model)
        except (TypeError, ValueError) as e:
            print('Sorry, we could not update the user.')
            print(e)

    def validateUserData(self, user_model) :
        """ Vérifie les datas avant insertion en database """
        user_data = user_model.__dict__

        try :
            if len(str(user_data['user_name'])) > 64:
                raise TypeError()

            if int(user_data['is_first_time']) not in (0, 1) :
                raise TypeError()

            if user_data['last_level'] not in (1, 2, 3) :
                raise TypeError()

            if not isinstance(user_data['solde'], int) :
                raise TypeError()

        except (TypeError, ValueError) as e:
            raise e
