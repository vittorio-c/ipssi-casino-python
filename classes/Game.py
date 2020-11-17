from .Scenario import Scenario
from .ConfigurationLevel import ConfigurationLevel
from .User import User

class Game :
    """ Contient la logique du JEU """

    User = None
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
        Scenario.launchGame(self.list_level[0])

        # Todo: Implémenter la recupération du USER s'il a deja joué sinon en créer un
        #? self.User = User
        
        #TODO: Determiner si première partie ou non
            #TODO: Choisir le level

        #TODO: Demander la mise
            #TODO: Check mise 
            #? Est que c'est un int
            #? < 0 AND >= SOLDE
            #? Retirer du SOLDE

        #TODO: Tirer un nombre au hasard

        #TODO: Est ce que c'est la bonne réponse
            #? Reussi
            #? Supérieur
            #? Inférieur
            #? Est ce que c'est le dernier essai

        #TODO: Recuperer le nombre de l'USER
            #TODO: Timer 10 secondes (Peut elle prendre une fonction en parametre)
        
        #TODO: Check solde
            #? EST CE QUE C'EST SUPERIEUR A 0 ?

        #TODO: Si on perd, lancer le compteur de 10 secondes, quitter par défaut
            #? Choix : Rejouer, et il redescend d'un level ?
            #? Choix : Quitter ?
            
        #TODO: Si on gagne, lancer le compteur de 10 secondes, quitter par défaut
            #? Choix : Rejouer, et il redescend d'un level ?
            #? Choix : Quitter ?

            #? Est ce que l'on est au level max ?
            #? Combien a-t-il gagné (GESTION DES GAINS)
                #TODO: AFFICHER LES STATS
        
        #TODO: Gestion des gains
            #? Voir SEBASTIEN

        #TODO: ENREGISTRER LES INFOS DANS UN FICHIER
        


            