from .SqliteDatabase import SqliteDatabase

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

    # TODO A voir plus tard pour les stats
    def getStatsByName(self, name) :
        """ Récupère les stats via le nom du user depuis la base de données"""

    def setStat(self, name) :
        """ Insert une stat en base de données à partir du nom du user """
