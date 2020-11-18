from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from .User import User
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
        while True:
            result = Service.delay10SecondesInput("\t- Alors mon nombre est : ?\n")
            checknumber = self.checkNumberValue(result)
            if checknumber == -1:
                print("    \t- Vous avez dépassé le délai de 10 secondes ! Vous perdez l'essai courant\n\t\t\t et il vous reste {} essai(s) !\n".format(str(self.list_level[self.id_level].nb_try - self.nb_coup)))
            elif checknumber == -2:
                print("    \t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {} :  ?\n".format(str(self.list_level[self.id_level].interval)))
            else:
                break
            if self.list_level[self.id_level].nb_try == self.nb_coup:
                return -1
        return checknumber

    def checkNumberValue(self, number_value) :
        """ Vérifie le nombre """
        if number_value == '': 
            self.nb_coup = self.nb_coup + 1
            return -1
        if number_value.isdigit() == False:
            return -2
        number_value = int(number_value)
        if number_value <= 0 or number_value > self.list_level[self.id_level].interval:
            return -2
        self.nb_coup = self.nb_coup + 1
        return number_value

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
        print("\t- Vous avez perdu ! Mon nombre est "+ str(self.nb_python) + " !\n")
        while True:
            inputUser = Service.delay10SecondesInput("\t- Souhaitez-vous continuer la partie (O/N) ?\n")
            checkInput = self.checkChoiceUser(inputUser)
            if checkInput == -1:
                return -1
            elif checkInput == 1:
                if self.id_level != 0:
                    self.id_level = self.id_level - 1
                return 1
    
    #TODO: Si on gagne, lancer le compteur de 10 secondes, quitter par défaut
        #? Choix : Rejouer, et il passe d'un level ?
        #? Choix : Quitter ?
        #? Est ce que l'on est au level max ?
        #? Combien a-t-il gagné (GESTION DES GAINS)
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
        
    #TODO: AFFICHER LES STATS
    def showUserStats(self) :
        """ Affiche les meilleurs et pires statistiques """

    #TODO: Gestion des gains
        #? Voir SEBASTIEN
    def manageUserGain(self) :
        """ Retourne le gain du USER  """
        # regarder dans `ConfigurationLevel` pour savoir comment configurer les `gains` de chaque level
