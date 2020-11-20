from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from random import randint
from classes.Controllers.UserController import UserController
from classes.Controllers.StatsController import StatsController
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
    user_controller = None
    stats_controller = None
    statusLevel = None
    level_history = None

    def __init__(self) :
        self.list_level = [
            ConfigurationLevel(1, 3, 10), # (number, nbTry, interval)
            ConfigurationLevel(2, 5, 20),
            ConfigurationLevel(3, 7, 30),
        ]
        self.time_interval = 10 # secondes
        self.user_controller = UserController()
        self.id_level = 0
        self.stats_controller = StatsController()

    def run(self) :
        """ Execution du jeu """
        Scenario.launchGame()
        user_name = self.getUsername()
        self.connected_user = self.getUser(user_name)
        if not self.hasSolde() :
            self.showUserStats()
            Scenario.tooPoorMessage()
        else :
            Scenario.sayHi(self.connected_user.user_name, self.connected_user.solde)
            Scenario.askShowRules(self.list_level[self.id_level]) if self.connected_user.is_first_time else ''
            status = 'continue'
            while (self.hasSolde() and status == 'continue' ) :
                self.askLevel()
                self.askMise()
                self.generateRandomNumber()
                status = self.hasEnoughTry()
                self.insertLevelInDatabase()
                self.updateLocalUser()
                self.user_controller.updateUser(self.connected_user)
                self.resetProperties()
            self.showUserStats()
            self.handleStatusGame(status)

    def getUsername(self) : 
        """ Récupère le pseudo de l'USER via un input """
        user_name = Scenario.askUsername()
        while (not self.isCorrectUsername(user_name)) :
            user_name = Scenario.usernameInvalid()
        return user_name

    def isCorrectUsername(self, user_name) :
        """ Retourne si le pseudo de l'USER est correct """
        try :
            user_name = int(user_name)
            return False
        except :
            if user_name == '' :
                return False
            return True

    def getUser(self,user_name) :
        """ Renvoie un USER depuis la base de données ou créé un nouvel USER"""
        user = self.user_controller.getUserByName(user_name)

        if user is None :
            user = self.user_controller.createUser(user_name)

        return user

    def checkUserProgression(self, user_name) :
        """ Vérifier son dernier niveau """
        user = self.user_controller.getUserByName(user_name)
        return user.last_level

    def askLevel(self) :
        """ Selectionne un niveau """
        if (not self.connected_user.is_first_time) and (self.connected_user.last_level > 1) :
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
        except:
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
            user_number = Service.delay10SecondesInput(Scenario.askNumber())
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
        self.statusLevel = 0
        self.gain = 0
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
                    self.id_level -= 1
                return 'continue'

    def inCaseUserWin(self) :
        """ Dans le cas où le user gagne son level """
        self.statusLevel = 1
        self.getGainWin()
        self.connected_user.solde += self.gain
        Scenario.winMessage(self.connected_user.user_name, self.nb_coup , self.gain)
        if not self.isLevelMaxReached():
            self.id_level += 1
            Scenario.nextLevel(str(self.id_level + 1))
        while True:
            inputUser = Service.delay10SecondesInput(Scenario.askNewTry())
            checkInput = self.checkChoiceUser(inputUser)
            if checkInput == 'quit':
                return 'quit'
            elif checkInput == 'continue':
                return 'continue'

    def isLevelMaxReached(self) :
        """ Retourne si on a atteint le dernier niveau """
        if self.id_level == len(self.list_level) - 1:
            return True
        return False

    def checkChoiceUser(self, inputUser) :
        """ Vérifie le choix de l'utilisateur """
        if inputUser == '' or inputUser.lower() == 'n':
            return 'quit'
        if inputUser.lower() == 'o':
            return 'continue'
        return 0

    def getGainWin(self) :
        """ Met à jour la variable gain locale """
        self.list_level[self.id_level].generateArrayGain(self.mise)
        self.gain = self.list_level[self.id_level].gain[str(self.id_level + 1)][str(self.nb_coup)]

    def hasSolde(self) :
        """ Retourne si l'USER possède un solde suffisant """
        if self.connected_user.solde <= 0 :
            return False
        else :
            return True

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
        self.statusLevel = None

    def updateLocalUser(self) :
        """ Mise à jour les propriétés de la classe USER avant insertion dans la base de données """
        self.connected_user.is_first_time = False
        self.connected_user.last_level = self.id_level + 1

    def showUserStats(self) :
        """ Affiche les meilleurs et pires statistiques """
        self.getAllStats()
        self.getNbTotalLevelsPlayed()
        Scenario.messageAllStats(self.level_history[0].created_at)
        self.showBestStats()
        self.showWorstStats()
        self.showAverageStats()

    def insertLevelInDatabase(self) :
        """ Insertion du level en base de donnée """
        stats_data = {
            'level': self.connected_user.last_level,
            'attempts': self.nb_coup,
            'bet': self.mise,
            'profit': self.gain,
            'result': self.statusLevel
            # Ajouter le nb_python qu'il fallait trouver
        }
        new_stats = self.stats_controller.createStats(self.connected_user.user_id, stats_data)

    def getAllStats(self) :
        """ Récupère l'historique des parties de l'USER """
        self.level_history = self.stats_controller.getStatsByUser(self.connected_user.user_id)

    def getNbTotalLevelsPlayed(self) :
        """ Traite et affiche le nombre de parties jouées """
        nbTotalLevelsPlayed = len(self.level_history)
        Scenario.messagegetNbTotalLevelsPlayed(nbTotalLevelsPlayed)

    def showBestStats(self) :
        """ Affiche les meilleures stats """
        Scenario.messageBestStats()
        self.showBestStatLevelReached()
        self.showNbCoupFindFirstAttempt()
        self.showBestGainWon()
        self.showBestBetUse()
        self.showNbLevelWon()

    def showWorstStats(self) :
        """ Affiche les pires stats """
        Scenario.messageWorstStats()
        self.showWorstGainWon()
        self.showWorstBetUse()
        self.showNbLevelLose()

    def showAverageStats(self) :
        """ Affiche les stats moyennes """
        Scenario.messageAverageStats()
        self.showAverageGainWon()
        self.showAverageBetUsed()
        self.showAverageNbAttemptsByLevels()

    def showBestStatLevelReached(self) :
        """ Traite et affiche le plus grand niveau atteint """
        bestLevel = 0
        for level in self.level_history :
            bestLevel = level.level if bestLevel < level.level else bestLevel
        Scenario.messageBestStatLevelReached(bestLevel)

    def showNbCoupFindFirstAttempt(self) :
        """ Traite et affiche les nombre de partie finie en un coup """
        nbCoupFindFirstAttempt = 0
        for level in self.level_history :
            if level.attempts == 1:
                nbCoupFindFirstAttempt += 1
        Scenario.messageNbCoupFindFirstAttempt(nbCoupFindFirstAttempt)

    def showBestGainWon(self) :
        """ Traite et affiche le plus grand gain obtenu """
        bestGainWon = 0
        for level in self.level_history :
            bestGainWon = level.profit if bestGainWon < level.profit else bestGainWon
        Scenario.messageGetBestGainWon(bestGainWon)

    def showBestBetUse(self) :
        """ Traite et affiche la plus grande mise de l'USER """
        bestBetUse = 0
        for level in self.level_history :
            bestBetUse = level.bet if bestBetUse < level.bet else bestBetUse
        Scenario.messageGetBestBetUse(bestBetUse)

    def showNbLevelWon(self) :
        """ Traite et affiche le nombre de niveau gagné """
        nbLevelWon = 0
        for level in self.level_history :
            if level.result == 1:
                nbLevelWon += 1
        Scenario.messageGetNbLevelWon(nbLevelWon)
    
    def showWorstGainWon(self) :
        """ Traite et affiche le plus petit gain obtenu """
        worstGainWon = self.level_history[0].profit
        for level in self.level_history :
            worstGainWon = level.profit if ((worstGainWon > level.profit) and (level.result == 1)) else worstGainWon
        Scenario.messageGetWorstGainWon(worstGainWon)

    def showWorstBetUse(self) :
        """ Traite et affiche la plus petit mise de l'USER """
        worstBetUse = self.level_history[0].bet
        for level in self.level_history :
            worstBetUse = level.bet if worstBetUse > level.bet else worstBetUse
        Scenario.messageGetWorstBetUse(worstBetUse)

    def showNbLevelLose(self) :
        """ Traite et affiche le nombre de niveau perdu """
        nbLevelLose = 0
        for level in self.level_history :
            if level.result == 0:
                nbLevelLose += 1
        Scenario.messageGetNbLevelLose(nbLevelLose)
    
    def showAverageGainWon(self) :
        """ Traite et affiche la moyenne des gains """
        averageGainWon = 0
        for level in self.level_history :
            averageGainWon += level.profit
        averageGainWon = averageGainWon/len(self.level_history)
        Scenario.messageGetAverageGainWon(averageGainWon)

    def showAverageBetUsed(self) :
        """ Traite et affiche la moyenne des mises de l'USER """
        averageBetUsed = 0
        for level in self.level_history :
            averageBetUsed += level.bet
        averageBetUsed = averageBetUsed/len(self.level_history)
        Scenario.messageGetAverageBetUsed(averageBetUsed)

    def showAverageNbAttemptsByLevels(self) :
        """ Traite et affiche le nombre de coup moyen pour tous les niveaux """
        level_current = 1
        while level_current <= len(self.list_level) :
            self.showAverageNbAttemptsByLevel(level_current)
            level_current += 1

    def showAverageNbAttemptsByLevel(self, num_level) : 
        """ Traite et affiche le nombre de coup moyen pour un niveau spécifique """
        nbAttempts = 0
        nbLevel = 0
        for level in self.level_history :
            if ((level.level == num_level) and (level.result == 1))  :
                nbLevel += 1
                nbAttempts += level.attempts
        if nbLevel != 0 :
            nbAttempts = nbAttempts/nbLevel
        Scenario.messageGetNbAttemptsByLevel(nbAttempts, num_level)
