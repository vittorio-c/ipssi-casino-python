from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from .User import User
from .Controller import Controller
from .Service import Service

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
        if not self.connected_user.is_first_time :
            user_level = Scenario.askLevel(self.connected_user.last_level)
            while not self.isCorrectLevel(user_level):
                user_level = Scenario.wrongLevel(self.connected_user.last_level)
            self.id_level = user_level-1
        else:
            self.id_level = 0

    def isCorrectLevel(self,level):
        """Vérifie le level entré par l'user"""
        try:
            int(level)
            if level > 0 or level <= self.connected_user.last_level:
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
        while True:
            user_number = Service.delay10SecondesInput(Scenario.askNumberToUser())
            checked_number = self.checkNumberValue(user_number)
            if checked_number == "Delai depasse":
                Scenario.timeoutMessage(str(self.list_level[self.id_level].nb_try - self.nb_coup))
            elif checked_number == "NaN" or checked_number == "Hors limite":
                Scenario.notUnderstandMessage(str(self.list_level[self.id_level].interval))
            else:
                break
            if self.list_level[self.id_level].nb_try == self.nb_coup:
                return -1
        return checked_number

    def checkNumberValue(self, number_value) :
        """ Vérifie le nombre """
        if number_value == '': 
            self.nb_coup = self.nb_coup + 1
            return "Delai depasse"
        if number_value.isdigit() == False:
            return "NaN"
        number_value = int(number_value)
        if number_value <= 0 or number_value > self.list_level[self.id_level].interval:
            return "Hors limite"
        self.nb_coup = self.nb_coup + 1
        return number_value

    #TODO: Est ce que c'est la bonne réponse
        #? Reussi
        #? Supérieur
        #? Inférieur
        #? Est ce que c'est le dernier essai
    def hasWin(self, number) :
        """ Retourne si le USER a gagner """
        comparison = self.compareNumberUser(number)
        if (comparison == 'equal') :
            return True
        else :
            return False


    def compareNumberUser(self, number) :
        """ Compare la valeur du USER par rapport à la réponse, donne des indications au USER"""
        if (number > self.nb_python) :
            Scenario.clueMessageIsInferior()
            return 'superior'
        elif (number < self.nb_python) :
            Scenario.clueMessageIsSuperior()
            return 'inferior'
        else :
            Scenario.winMessage(self.nb_coup , self.gain)
            return 'equal'

    #TODO: Check solde
        #? EST CE QUE C'EST SUPERIEUR A 0 ?
    def hasMoney(self) :
        """ Retourne si le USER possède encore de l'argent """

    #TODO: Si on perd, lancer le compteur de 10 secondes, quitter par défaut
        #? Choix : Rejouer, et il redescend d'un level ?
        #? Choix : Quitter ?
    def inCaseUserLoose(self) :
        """ Dans le cas où le user perd son level """
        Scenario.looseMessage(self.nb_python)
        while True:         
            inputUser = Service.delay10SecondesInput(Scenario.askNewTry())
            checkInput = self.checkCaseUserLoose(inputUser)
            if checkInput == 'quit':
                return 'quit'
            elif checkInput == 'continue':
                if self.id_level != 0:
                    self.id_level = self.id_level - 1
                return 'continue'

    def checkCaseUserLoose(self, inputUser) :
        """ Check la réponse de l'user """
        if inputUser == '' or inputUser.lower == 'n': 
            return 'quit'
        if inputUser.lower == 'o':
            return 'continue'
        return 'error'
        
    #TODO: Si on gagne, lancer le compteur de 10 secondes, quitter par défaut
        #? Choix : Rejouer, et il passe d'un level ?
        #? Choix : Quitter ?
        #? Est ce que l'on est au level max ?
        #? Combien a-t-il gagné (GESTION DES GAINS)
    def inCaseUserWin(self) :
        """ Dans le cas où le user gagne son level """
        self.solde = self.solde + self.gain
        self.id_level = self.id_level + 1
        if self.isLevelMaxReached():
            return 0
        print("\t- Super ! Vous passez au Level {}.\n".format(str(self.id_level + 1)))
        while True:
            inputUser = Service.delay10SecondesInput("\t- Souhaitez-vous continuer la partie (O/N) ?\n")
            checkInput = self.checkChoiceUser(inputUser)
            if checkInput == -1:
                return -1
            elif checkInput == 1:
                return 1

    def isLevelMaxReached(self) :
        if self.id_level == len(self.list_level):
            return True
        return False

    def checkChoiceUser(self, inputUser) :
        if inputUser == '' or inputUser.lower() == 'n': 
            return -1
        if inputUser.lower() == 'o':
            return 1
        return 0

    #TODO: AFFICHER LES STATS
    def showUserStats(self) :
        """ Affiche les meilleurs et pires statistiques """

    #TODO: Gestion des gains
        #? Voir SEBASTIEN
    def manageUserGain(self) :
        """ Retourne le gain du USER  """
        # regarder dans `ConfigurationLevel` pour savoir comment configurer les `gains` de chaque level

    def hasSolde(self) :
        if self.solde <= 0 :
            return False
        else :
            return True
