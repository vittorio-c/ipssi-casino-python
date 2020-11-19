import time
from .TextColor import TextColor

class Scenario :
    """ Permet l'affichage des textes d'ambiances et contextuels """

    @staticmethod
    def launchGame() :
        print(TextColor.ColorText('\n**********************************************************', 'MAGENTA'))

    @staticmethod
    def askUsername() :
        user_name = input(TextColor.ColorText('\t- Je suis ' + TextColor.ColorText('Python', 'YELLOW', 'MAGENTA') +
         '. Quel est votre pseudo ? \n ', 'MAGENTA'))
        return user_name
    
    @staticmethod
    def sayHi(user_name, solde) :
        print(TextColor.ColorText('\n\t- Hello ' + TextColor.ColorText(str(user_name), 'YELLOW', 'MAGENTA') +
            ', vous avez ' + TextColor.ColorText(str(solde) + '€', 'YELLOW', 'MAGENTA') +
            ', Très bien ! Installez vous SVP à la table de pari.\n\tJe vous expliquerai le principe du jeu : \n', 'MAGENTA'))

    @staticmethod
    def askMise() :
        mise = input(TextColor.ColorText('\t- Le jeu commence, entrez votre mise : ?\n', 'MAGENTA'))
        return mise

    @staticmethod
    def miseInvalid(montant_max) :
        mise = input(TextColor.ColorText('\t- Le montant saisi n\'est pas valide. Entrer SVP un montant entre 1 et ' +
            str(montant_max) + ' € :  ?\n ', 'RED'))
        return mise

    @staticmethod
    def askLevel(level_max):
        user_level = input("\t- Veuillez choisir le level entre 1 et " + str(level_max) +" s'il vous plaît :\n")
        return user_level

    @staticmethod
    def wrongLevel(level_max):
        user_level = input(TextColor.ColorText("\t- Le niveau choisi n'existe pas ! Veuillez choisir le level entre 1 et " +
            str(level_max) + " s'il vous plaît\n",'RED'))
        return user_level

    @staticmethod
    def showIntervalNumber(level) :
        print(TextColor.ColorText('\t- Je viens de penser à un nombre entre ' +
            TextColor.ColorText('1 et ' + str(level.interval), 'YELLOW', 'MAGENTA') + '.\n', 'MAGENTA'))

    @staticmethod
    def askShowRules(level) :
        show_rules = input(TextColor.ColorText('\t- Souhaitez-vous connaitre les règles ?(O/N) \n ', 'YELLOW'))

        if (show_rules.casefold() == 'o') :
            Scenario.rules(level)

    @staticmethod
    def rules(level) :
        print(TextColor.ColorText('\t- Attention : vous avez le droit à ' +
            TextColor.ColorText(str(level.nb_try),'RED','GREEN') + ' essais !\n', 'GREEN'))
        print(TextColor.ColorText('\t- Si vous devinez mon nombre dès ' +
            TextColor.ColorText('au premier coup', 'YELLOW', 'GREEN') + ', vous gagnez le double de votre mise !\n', 'GREEN'))
        print(TextColor.ColorText('\t- Si vous le devinez ' + TextColor.ColorText('au 2è coup', 'YELLOW', 'GREEN') +
            ', vous gagnez exactement votre mise !\n', 'GREEN'))
        print(TextColor.ColorText('\t- Si vous le devinez ' + TextColor.ColorText('au 3è coup', 'YELLOW', 'GREEN') +
            ', vous gagnez la moitiè votre mise !\n', 'GREEN'))
        print(TextColor.ColorText('\t- Si vous ' + TextColor.ColorText('ne le devinez pas au 3è coup', 'RED', 'GREEN') +
            ', vous perdez votre mise et vous avez le droit : ', 'GREEN'))
        print(TextColor.ColorText('\t\t- de retenter votre chance avec l\'argent qu\'il vous reste pour reconquérir' +
            ' le level perdu.', 'YELLOW'))
        print(TextColor.ColorText('\t\t- de quitter le jeu.\n', 'YELLOW'))
        print(TextColor.ColorText('\t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et ' +
            TextColor.ColorText('de partir avec vos gains', 'YELLOW', 'GREEN') + ' OU \n\tde continuer le jeu en passant ' +
            TextColor.ColorText('au level supérieur', 'YELLOW', 'GREEN') + '.\n', 'GREEN'))

    @staticmethod
    def askNumber() :
        number = input("\t- Alors mon nombre est : ?\n")
        return number

    @staticmethod
    def wrongNumberMessage(level) :
        number = input(TextColor.ColorText('\t- Je ne comprends pas ! Entrer SVP un nombre entre ' + 
            TextColor.ColorText('1 et ' + str(level.interval), 'YELLOW', 'RED') + ' : \n', 'RED'))
        return number

    @staticmethod
    def askNewTry() :
        return "\t- Souhaitez-vous continuer la partie (O/N) ?\n"

    @staticmethod
    def askNumberToUser() :
        return "\t- Alors mon nombre est : ?\n"

    @staticmethod
    def timeoutMessage(nb_try) :
        print(TextColor.ColorText("\t- Vous avez dépassé le délai de 10 secondes ! " +
            "Vous perdez l'essai courant\n\tet il vous reste {} essai(s) !\n".format(nb_try),'RED'))

    @staticmethod
    def notUnderstandMessage(nb_max) :
        print(TextColor.ColorText("\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {} :  ?\n".format(nb_max),  'RED'))

    @staticmethod
    def clueMessageIsInferior() :
        print('\t- Votre nbre est ' + TextColor.ColorText('trop grand', 'YELLOW') + ' !\n')

    @staticmethod
    def clueMessageIsSuperior() :
        print('\t- Votre nbre est ' + TextColor.ColorText('trop petit', 'YELLOW') + ' !\n')

    @staticmethod
    def indicateLastChance() :
        print('\t- Il vous reste ' + TextColor.ColorText('une chance', 'RED') + ' !\n')

    @staticmethod
    def winMessage(user_name,nb_coup, gain) :
        print('\t- Bingo ' + TextColor.ColorText(str(user_name), 'YELLOW', 'MAGENTA') +
            ', vous avez gagné ' + TextColor.ColorText('en "'+ str(nb_coup) +'" coup(s)', 'YELLOW')
        + ' et vous avez emporté ' + TextColor.ColorText('"'+ str(gain) +'" €', 'YELLOW')+ ' !\n')

    @staticmethod
    def looseMessage(number_python) :
        print(TextColor.ColorText('\t- Vous avez perdu ! Mon nombre est "' +
            TextColor.ColorText(str(number_python), 'YELLOW', 'RED') + '" !\n ', 'RED'))
    
    @staticmethod
    def quitMessage(solde) :
        print(TextColor.ColorText('\t- Au revoir ! Vous finissez la partie avec "' +
            TextColor.ColorText(str(solde), 'GREEN', 'RED') + '" €.\n', 'RED'))

    @staticmethod
    def tooPoorMessage() :
        print(TextColor.ColorText('-\t Désolé, mais votre solde est insuffisant.\n', 'RED'))

    @staticmethod
    def finishedMessage() :
        print(TextColor.ColorText('-\t Nous vous remercions pour votre fidélité !\n', 'RED'))

    @staticmethod
    def nextLevel(level) :
        print("\t- Super ! Vous passez au Level {}.\n".format(str(level)))

