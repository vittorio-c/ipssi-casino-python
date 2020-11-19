from .SqliteDatabase import SqliteDatabase
from .User import User

class Controller :
    """ Permet de récupérer des éléments spécifiques depuis la base de données """

    database = None

    def __init__(self) :
        self.database = SqliteDatabase()

    def getUserByName(self, name) :
        """ Récupère le user via son nom depuis la base de données"""
        user = self.database.getUserByName(name)
        return user

    def createUser(self, user_name) :
        """ Insert un user en base de données """
        return self.database.createUser(user_name)

    def updateUser(self, user_model) :
        """ Update un user en base de données """
        try:
            if not isinstance(user_model, User) :
                raise TypeError()

            self.checkUserData(user_model)
            return self.database.updateUser(user_model)
        except:
            print('Sorry, we could not update the user.')

    # TODO A voir plus tard pour les stats
    def getStatsByName(self, name) :
        """ Récupère les stats via le nom du user depuis la base de données"""

    def setStat(self, name) :
        """ Insert une stat en base de données à partir du nom du user """

    def checkUserData(self, user_model) :
        """ Check les datas avant insertion en database """
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
