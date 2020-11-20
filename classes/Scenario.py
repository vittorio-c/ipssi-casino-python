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
        mise = input(TextColor.ColorText('\t- Le jeu commence, entrez votre mise : ?\n', 'YELLOW'))
        return mise

    @staticmethod
    def miseInvalid(montant_max) :
        mise = input(TextColor.ColorText('\t- Le montant saisi n\'est pas valide. Entrer SVP un montant entre 1 et ' +
            str(montant_max) + ' € :  ?\n ', 'RED'))
        return mise

    @staticmethod
    def askLevel(level_max):
        user_level = input(TextColor.ColorText("\t- Veuillez choisir le level entre 1 et " + str(level_max) +" s'il vous plaît :\n", 'YELLOW'))
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
        while(not show_rules.casefold() == 'o' and not show_rules.casefold() == 'n' ):
            print(TextColor.ColorText('\t- Désolé, je n\'ai pas compris votre réponse.', 'RED')) 
            show_rules = input(TextColor.ColorText('\t Veuillez répondre par (O/N) :\n ', 'YELLOW'))
        if (show_rules.casefold() == 'o') :
            Scenario.rules(level)
            print(TextColor.ColorText('\t ******** Bienvenue au Casino-Game, Amusez-vous bien ! ********  \n', 'WHITE'))
        elif (show_rules.casefold() == 'n'):
            print(TextColor.ColorText('\t ******** Bienvenue au Casino-Game, Amusez-vous bien ! ******** \n', 'WHITE'))
        
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
        return TextColor.ColorText("\t- Alors mon nombre est : ?\n",'YELLOW')

    @staticmethod
    def wrongNumberMessage(level) :
        number = input(TextColor.ColorText('\t- Je ne comprends pas ! Entrer SVP un nombre entre ' + 
            TextColor.ColorText('1 et ' + str(level.interval), 'YELLOW', 'RED') + ' : \n', 'RED'))
        return number

    @staticmethod
    def askNewTry() :
        return TextColor.ColorText("\t- Souhaitez-vous continuer la partie (O/N) ?\n", 'YELLOW')

    @staticmethod
    def timeoutMessage(nb_try) :
        print(TextColor.ColorText("\t- Vous avez dépassé le délai de 10 secondes ! " +
            "Vous perdez l'essai courant\n\tet il vous reste {} essai(s) !\n".format(nb_try),'RED'))

    @staticmethod
    def notUnderstandMessage(nb_max) :
        print(TextColor.ColorText("\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {} :  ?\n".format(nb_max),
            'RED'))

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
        print(TextColor.ColorText('\t- Bingo ' + TextColor.ColorText(str(user_name), 'YELLOW', 'MAGENTA') +
            ', vous avez gagné ' + TextColor.ColorText('en "'+ str(nb_coup) +'" coup(s)', 'YELLOW', 'MAGENTA') +
            ' et vous avez emporté ' + TextColor.ColorText('"'+ str(gain) +'" €', 'YELLOW', 'MAGENTA')+ ' !\n', 'MAGENTA'))

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
        print(TextColor.ColorText('\t- Désolé, mais votre solde est insuffisant.\n', 'RED'))

    @staticmethod
    def finishedMessage() :
        print(TextColor.ColorText('-\t Nous vous remercions pour votre fidélité !\n', 'RED'))

    @staticmethod
    def nextLevel(level) :
        print("\t- Super ! Vous passez au Level {}.\n".format(str(level)))

    @staticmethod
    def messageAllStats(date) :
        print("\t- Voici vos statistiques, depuis la 1è fois le "+str(date)+" :\n")

    @staticmethod
    def messageBestStats() :
        print("\t\t- Vos meilleures statistiques :\n")

    @staticmethod
    def messageBestStatLevelReached(level) :
        print("\t\t\t- Level le plus élevé atteint est "+str(level)+"\n")

    @staticmethod
    def messageNbCoupFindFirstAttempt(nb) :
        print("\t\t\t- Vous avez réussi à trouver le bon nombre dès le 1è coup "+str(nb)+" fois.\n")

    @staticmethod
    def messageGetBestGainWon(nb) :
        print("\t\t\t- Le gain le plus elevé est "+str(nb)+" €.\n")

    @staticmethod
    def messageGetBestBetUse(nb) :
        print("\t\t\t- La mise la plus elevé est "+str(nb)+" €.\n")

    @staticmethod
    def messageGetNbLevelWon(nb) :
        print("\t\t\t- Le nombre de manche gagné est de "+str(nb)+".\n")

    @staticmethod
    def messageWorstStats() :
        print("\t\t- Vos pires statistiques :\n")

    @staticmethod
    def messageGetWorstGainWon(nb) :
        print("\t\t\t- Le gain le plus bas est "+str(nb)+" €.\n")

    @staticmethod
    def messageGetWorstBetUse(nb) :
        print("\t\t\t- La mise la plus basse est "+str(nb)+" €.\n")

    @staticmethod
    def messageGetNbLevelLose(nb) :
        print("\t\t\t- Le nombre de manche perdu est de "+str(nb)+".\n")

    @staticmethod
    def messageAverageStats() :
        print("\t\t- Vos moyennes :\n")

    @staticmethod
    def messageGetAverageGainWon(nb) :
        print("\t\t\t- Le gain moyenne est de "+str(nb)+" €.\n")

    @staticmethod
    def messageGetAverageBetUse(nb) :
        print("\t\t\t- La mise moyenne est de "+str(nb)+" €.\n")

    @staticmethod
    def messageGetNbAttemptsByLevel(nbAttempts, num_level) :
        print("\t\t\t- Le nombre moyen de tentatives pour trouver le bon nombre au niveau {} est de {}.\n".format(str(num_level), str(nbAttempts)))
        print("\t\t\t(on ne comptabilise le nombre de coups qu'en cas de réussite)\n")
        
    @staticmethod
    def messagegetNbTotalLevelsPlayed(nb) :
        print("\t- Vous avez joué au total "+str(nb)+" parties.\n")

        

        


        


        



