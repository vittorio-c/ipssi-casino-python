from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from .User import User
from random import randint
from .Controller import Controller
from .Service import Service

class Game :
    """ Contient la logique du JEU """

    connected_user = None
    id_level = None
    nb_python = None
    nb_user = None
    nb_coup = 0
    list_level = []
    mise = None
    gain = None
    solde = None
    controller = None


    def __init__(self) :
        self.list_level = [
            ConfigurationLevel(1, 3, 10), # (number, nbTry, interval)
            ConfigurationLevel(2, 5, 20),
            ConfigurationLevel(3, 7, 30),
        ]
        self.time_interval = 10 # secondes
        self.controller = Controller()
        self.id_level = 0

    def run(self) :
        """ Execution du jeu """
        Scenario.launchGame()
        user_name = Scenario.askUsername()
        self.connected_user = self.getUser(user_name)

        if self.connected_user.last_level > 1 :
            self.askLevel()

        Scenario.askShowRules(self.list_level[0]) # Récupérer le `last_level`du USER
        status = 'continue'
        self.askLevel()
        while (self.hasSolde() and status == 'continue' ) :
            self.askMise()
            self.generateRandomNumber()
            status = self.hasEnoughTry()
            self.resetProperties()
        self.handleStatusGame(status)
            
    def getUser(self,user_name) :
        """ Renvoie un USER depuis la base de données ou créé un nouvel USER"""
        user = self.controller.getUserByName(user_name)

        if user is None :
            user = self.controller.createUser(user_name)

        return user

    def checkUserProgression(self, user_name) :
        """ Vérifier son dernier niveau """
        user = self.controller.getUserByName(user_name)
        return user.last_level

    def askLevel(self) :
        """ Selectionne un niveau """
        if not self.connected_user.is_first_time :
            user_level = Scenario.askLevel(self.connected_user.last_level)

            while not self.isCorrectLevel(user_level):
                user_level = Scenario.wrongLevel(self.connected_user.last_level)

            self.id_level = int(user_level) - 1
        else:
            self.id_level = 0

    def isCorrectLevel(self, level):
        """Vérifie le level entré par l'user"""
        try:
            if int(level) > 0 and int(level) <= self.connected_user.last_level:
                return True
            else:
                return False
        except ValueError as e :
            return False

    def askMise(self) :
        """ Demande la mise au USER et la vérifie """
        mise = Scenario.askMise()
        while (not self.isCorrectMiseValue(mise)) :
            mise = Scenario.miseInvalid(self.connected_user.solde)
        self.mise = int(mise)
        self.connected_user.solde -= self.mise

    def isCorrectMiseValue(self, bet_value) :
        """ Vérifie la mise """
        try:
            bet_value = int(bet_value)
            if ((bet_value <= 0) or (bet_value > self.connected_user.solde)) :
                return False
            return True
        except:
            return False

    def generateRandomNumber(self) :
        """ Génère un nombre aléatoire entre 1 (inclus) et `max` (inclus) """
        Scenario.showIntervalNumber(self.list_level[self.id_level])
        level = self.list_level[int(self.id_level)]
        random_number = randint(1, level.interval)
        self.nb_python = random_number

    def askUserNumber(self) :
        """ Demande un nombre au USER et le vérifie """
        user_number = ''
        isCorrect = False
        while (self.list_level[self.id_level].nb_try != self.nb_coup) and not isCorrect :
            user_number = Service.delay10SecondesInput(Scenario.askNumberToUser())
            isCorrect = self.isCorrectNumberValue(user_number)
        self.nb_user = int(user_number) if isCorrect else ''

    def isCorrectNumberValue(self, number_value) :
        """ Vérifie le nombre """
        if number_value == '':
            self.nb_coup = self.nb_coup + 1
            Scenario.timeoutMessage(str(self.list_level[self.id_level].nb_try - self.nb_coup))
            return False
        if number_value.isdigit() == False:
            Scenario.notUnderstandMessage(str(self.list_level[self.id_level].interval))
            return False
        number_value = int(number_value)
        if number_value <= 0 or number_value > self.list_level[self.id_level].interval:
            Scenario.notUnderstandMessage(str(self.list_level[self.id_level].interval))
            return False
        self.nb_coup = self.nb_coup + 1
        return True

    def hasWin(self) :
        """ Retourne si le USER a gagner """
        comparison = self.compareNumberUser()
        if (comparison == 'equal') :
            return True
        else :
            return False

    def compareNumberUser(self) :
        """ Compare la valeur du USER par rapport à la réponse, donne des indications au USER"""
        if (self.nb_user == '') :
            return None
        elif (self.nb_user > self.nb_python) :
            Scenario.clueMessageIsInferior()
            return 'superior'
        elif (self.nb_user < self.nb_python) :
            Scenario.clueMessageIsSuperior()
            return 'inferior'
        else :
            return 'equal'

    def inCaseUserLoose(self) :
        """ Dans le cas où le user perd son level """
        Scenario.looseMessage(self.nb_python)
        if (not self.hasSolde()) :
            return 'tooPoor'
        while True:
            inputUser = Service.delay10SecondesInput(Scenario.askNewTry())
            checkInput = self.checkChoiceUser(inputUser)
            if checkInput == 'quit':
                return 'quit'
            elif checkInput == 'continue':
                if self.id_level != 0:
                    self.id_level = self.id_level - 1
                return 'continue'

    def inCaseUserWin(self) :
        """ Dans le cas où le user gagne son level """
        self.getGainWin()
        self.connected_user.solde += self.gain
        Scenario.winMessage(self.connected_user.user_name, self.nb_coup , self.gain)
        if not self.isLevelMaxReached():
            self.id_level += 1
            print("\t- Super ! Vous passez au Level {}.\n".format(str(self.id_level + 1)))
            while True:
                inputUser = Service.delay10SecondesInput("\t- Souhaitez-vous continuer la partie (O/N) ?\n")
                checkInput = self.checkChoiceUser(inputUser)
                if checkInput == 'quit':
                    return 'quit'
                elif checkInput == 'continue':
                    return 'continue'
        return 'finished'

    def isLevelMaxReached(self) :
        if self.id_level == len(self.list_level) - 1:
            return True
        return False

    def checkChoiceUser(self, inputUser) :
        if inputUser == '' or inputUser.lower() == 'n': 
            return 'quit'
        if inputUser.lower() == 'o':
            return 'continue'
        return 0

    def getGainWin(self) : 
        self.list_level[self.id_level].generateArrayGain(self.mise)
        self.gain = self.list_level[self.id_level].gain[str(self.id_level + 1)][str(self.nb_coup)]

    def hasSolde(self) :
        if self.connected_user.solde <= 0 :
            return False
        else :
            return True

    #TODO: AFFICHER LES STATS
    def showUserStats(self) :
        """ Affiche les meilleurs et pires statistiques """

    def hasEnoughTry(self) :
        """ Retourne si le USER possède encore des essais """
        while (self.list_level[self.id_level].nb_try != self.nb_coup) :
            self.askUserNumber()
            if(self.hasWin()) :
                return self.inCaseUserWin()
        return self.inCaseUserLoose()
    
    def handleStatusGame(self, status) :
        """ Gère les différentes fin du jeu """
        if(status == 'quit') :
            Scenario.quitMessage(self.connected_user.solde)
        elif(status == 'tooPoor') :
            Scenario.tooPoorMessage()
        elif(status == 'finished') :
            Scenario.finishedMessage()

    def resetProperties(self) :
        """ Reinitialise les propriétés de la classe GAME """
        self.nb_python = None
        self.nb_user = None
        self.nb_coup = 0
        self.mise = None
        self.gain = None

