from .Database import Database

class Controller :
    """ Permet de récupérer des éléments spécifiques depuis la base de données """

    database = None

    def __init__(self) :
        database = Database()

    def getUserByName(self, name) :
        """ Récupère le user via son nom depuis la base de données"""
    
    # Doit retourner le USER créé
    def setUser(self) :
        """ Insert un user en base de données """
    
    # A voir plus tard pour les stats
    def getStatsByName(self, name) :
        """ Récupère les stats via le nom du user depuis la base de données"""
    
    def setStat(self, name) :
        """ Insert une stat en base de données à partir du nom du user """