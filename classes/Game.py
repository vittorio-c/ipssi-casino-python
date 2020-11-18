from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from .User import User
from .Controller import Controller

class Game :
    """ Contient la logique du JEU """

    connected_user = None
    level = []
    id_level = None
    nb_python = None
    nb_user = None
    nb_coup = None
    list_level = None
    mise = None
    dotations = None
    gain = None
    solde = None

    def __init__(self) :
        self.list_level = [
            ConfigurationLevel(1, 3, 10), # (number, nbTry, interval)
            ConfigurationLevel(2, 5, 20),
            ConfigurationLevel(3, 7, 30),
        ]
        self.time_interval = 10 # secondes
        
    def run(self) :
        Scenario.launchGame()
        user_name = Scenario.askUsername()
        Scenario.askShowRules(self.list_level[0]) # Récupérer le `last_level`du USER

######################################## TODO: ##########################################

    # Todo: Implémenter la recupération du USER s'il a deja joué sinon en créer un
    def getUser(self,user_name) :
        """ Renvoie un USER depuis la base de données ou créé un nouvel USER"""
        controller = Controller()
        user = controller.getUserByName(user_name)
        if user:
            if user.last_level > 1:
                self.selectLevel()
        else:
            user= controller.createUser(user_name)   
        return user  

    #TODO: Determiner si première partie ou non
        #TODO: Choisir le level
    def checkUserProgression(self, user_name) :
        """ Vérifier son dernier niveau """
        controller = Controller()
        user = controller.getUserByName(user_name)
        return user.last_level 

    def askLevel(self) :
        """ Selectionne un niveau """
        if not connected_user.is_first_time :
            user_level= Scenario.askLevel(connected_user.last_level)
            while self.isCorrectLevel(user_level):
                user_level= Scenario.wrongLevel(connected_user.last_level)
            id_level=user_level-1
        else:
            id_level=0

    def isCorrectLevel(self,level):
        """Vérifie le level entré par l'user"""
        try:
            int(level)
            if level > 0 or level <= connected_user.last_level:
                return True
            else:
                return False    
        except:
            return False


             
    #TODO: Demander la mise
        #TODO: Check mise 
        #? Est que c'est un int
        #? < 0 AND >= SOLDE
        #? Retirer du SOLDE
    def askMise(self) :
        """ Demande la mise au USER et la vérifie """

    def checkMiseValue(self, bet_value) :
        """ Vérifie la mise """

    #TODO: Tirer un nombre au hasard
    def generateRandomNumber(self, max) :
        """ Génère un nombre aléatoire entre 1 (inclus) et `max` (inclus) """
    #TODO: Recuperer le nombre de l'USER
        #TODO: Check le nombre
    def askUserNumber(self) :
        """ Demande un nombre au USER et le vérifie """

    def checkNumberValue(self, number_value) :
        """ Vérifie le nombre """

    #TODO: Est ce que c'est la bonne réponse
        #? Reussi
        #? Supérieur
        #? Inférieur
        #? Est ce que c'est le dernier essai
    def giveClueForNumber(self, number) :
        """ Retourne un indice en fonction du nombre du USER """

    #TODO: Check solde
        #? EST CE QUE C'EST SUPERIEUR A 0 ?
    def hasMoney(self) :
        """ Retourne si le USER possède encore de l'argent """

    #TODO: Si on perd, lancer le compteur de 10 secondes, quitter par défaut
        #? Choix : Rejouer, et il redescend d'un level ?
        #? Choix : Quitter ?
    def inCaseUserLoose(self) :
        """ Dans le cas où le user perd son level """
        
    #TODO: Si on gagne, lancer le compteur de 10 secondes, quitter par défaut
        #? Choix : Rejouer, et il redescend d'un level ?
        #? Choix : Quitter ?
        #? Est ce que l'on est au level max ?
        #? Combien a-t-il gagné (GESTION DES GAINS)
    def inCaseUserWin(self) :
        """ Dans le cas où le user gagne son level """
    
    #TODO: AFFICHER LES STATS
    def showUserStats(self) :
        """ Affiche les meilleurs et pires statistiques """

    #TODO: Gestion des gains
        #? Voir SEBASTIEN
    def manageUserGain(self) :
        """ Retourne le gain du USER  """
        # regarder dans `ConfigurationLevel` pour savoir comment configurer les `gains` de chaque level
