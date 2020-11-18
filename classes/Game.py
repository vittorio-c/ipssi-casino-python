from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from .User import User

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
    def getUser(self) :
        """ Renvoie un USER depuis la base de données ou créé un nouvel USER"""

    #TODO: Determiner si première partie ou non
        #TODO: Choisir le level
    def checkUserProgression(self) :
        """ Vérifier son dernier niveau """

    def selectLevel(self, level) :
        """ Selectionne un niveau """

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
    def hasWin(self, number) :
        """ Retourne si le USER a gagner """
        comparison = self.compareNumberUser(number)
        if (comparison == 'Egale') :
            return True
        else :
            return False


    def compareNumberUser(self, number) :
        """ Compare la valeur du USER par rapport à la réponse, donne des indications au USER"""
        if (number > self.nb_python) :
            Scenario.clueMessageIsInferior()
            return 'Supérieur'
        elif (number < self.nb_python) :
            Scenario.clueMessageIsSuperior()
            return 'Inférieur'
        else :
            Scenario.winMessage(self.nb_coup , self.gain)
            return 'Egale'

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
