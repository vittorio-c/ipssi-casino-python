from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from .User import User
from random import randint
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
        """ Execution du jeu """
        Scenario.launchGame()
        user_name = Scenario.askUsername()
        Scenario.askShowRules(self.list_level[0]) # Récupérer le `last_level`du USER

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

    def askMise(self) :
        """ Demande la mise au USER et la vérifie """
        mise = Scenario.askMise()
        while (not self.isCorrectMiseValue(mise)) :
            mise = Scenario.miseInvalid(self.solde)
        self.mise = mise
        self.solde -= self.mise

    def isCorrectMiseValue(self, bet_value) :
        """ Vérifie la mise """
        try:
            int(bet_value)
            if (not(bet_value > 0) and (bet_value <= self.solde)) :
                return False
            return True
        except:
            return False

    def generateRandomNumber(self) :
        """ Génère un nombre aléatoire entre 1 (inclus) et `max` (inclus) """
        level = self.list_level[int(self.id_level)]
        random_number = randint(1, level.interval)
        self.nb_python = random_number

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
        
    def inCaseUserWin(self) :
        """ Dans le cas où le user gagne son level """
        self.id_level = self.id_level + 1
        self.solde = self.solde + self.getGainWin()
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

    def getGainWin(self) : 
        return self.list_level[self.id_level - 1].gain[str(self.id_level)][str(self.nb_coup)]

    def hasSolde(self) :
        if self.solde <= 0 :
            return False
        else :
            return True

    #TODO: AFFICHER LES STATS
    def showUserStats(self) :
        """ Affiche les meilleurs et pires statistiques """