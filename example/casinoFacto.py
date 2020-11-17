from random import randrange
import math
import sys
from myInputFacto import input_with_timeout
import pickle
import datetime

try:
    level = 1
    level_max = 3
    solde = 10
    name_user = input("\t- Je suis Python. Quel est votre pseudo ? ")
    dv = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    # Si le fichier donnees n'existent pas
    donnees = {}
    donnees[name_user] = {}
    donnees[name_user]["Derniere_visite"] = dv
    donnees[name_user]["Solde"] = 10

    derniere_visite = False

    try:
        with open('donnees', 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            try:
                mes_donnees = mon_depickler.load()
                fichier.close()
                if name_user in mes_donnees:
                    derniere_visite = mes_donnees[name_user]["Derniere_visite"]
                if not name_user in mes_donnees:
                    mes_donnees[name_user] = {}
                    mes_donnees[name_user]["Solde"] = 10
                mes_donnees[name_user]["Derniere_visite"] = dv
                solde = mes_donnees[name_user]["Solde"]
                with open('donnees', 'wb') as fichier2:
                    mon_pickler = pickle.Pickler(fichier2)
                    mon_pickler.dump(mes_donnees)
                    fichier2.close()
            except EOFError:
                pass
    except FileNotFoundError:
        with open('donnees', 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(donnees)
            fichier.close()


    if solde == 0:
        print("\t- Désolé mais vous n'avez pas d'argent !")
        raise SystemExit

    if not derniere_visite:
        print("\t- Bonjour", name_user, ", ceci est votre première visite dans notre casino. Vous avez", solde, "€. Très bien ! Installez vous SVP à la table de pari.")
    else:
        print("\t- Bonjour", name_user, "ravi de vous revoir, votre dernière visite remonte au", derniere_visite, "Vous avez", solde, "€. Très bien ! Installez vous SVP à la table de pari.")
    print("""\t- Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?\n
        \t- Att : vous avez le droit à trois essais !\n
        \t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n
        \t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n
        \t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n    
        \t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et
        \tvous avez le droit : 
        \t\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
        \t\t- de quitter le jeu.\n
        \t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level supérieur.\n     
        """)

    def reset_param(level, mise):
        """Permet de réinitialiser les variables pour chaque niveau."""
        nb_python = randrange(1,((level * 10) + 1))
        nb_coup = 0
        dico = {}
        dico["1"] = {}
        dico["2"] = {}
        dico["3"] = {}

        # Crée le dictionnaire selon la mise de l'utilisateur
        dico["1"]["1"] = math.ceil(mise * 2)
        dico["1"]["2"] = math.ceil(mise)
        dico["1"]["3"] = math.ceil(mise / 2)

        dico["2"]["1"] = math.ceil(mise * 3)
        dico["2"]["2"] = math.ceil(mise * 2)
        dico["2"]["3"] = math.ceil(mise)
        dico["2"]["4"] = math.ceil(mise / 2)
        dico["2"]["5"] = math.ceil(mise / 3)

        dico["3"]["1"] = math.ceil(mise * 4)
        dico["3"]["2"] = math.ceil(mise * 3)
        dico["3"]["3"] = math.ceil(mise * 2)
        dico["3"]["4"] = math.ceil(mise)
        dico["3"]["5"] = math.ceil(mise / 2)
        dico["3"]["6"] = math.ceil(mise / 3)
        dico["3"]["7"] = math.ceil(mise / 4)

        nb_max = level * 10

        nb_coup_max = ((level * 2) + 1)       
        return (nb_python, nb_coup, dico, nb_max, nb_coup_max)

    def recup_mise(solde):
        """Permet de récupérer la mise de l'utilisateur"""
        mise = input("\t- Le jeu commence, entrez votre mise : ?\n\t- ")
        while True:
            try:
                mise = int(mise)
                if mise <= 0 or mise > solde:
                    raise  ValueError()
            except ValueError:
                mise = input("\t- Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et {} € :  ?\n\t- ".format(solde))
            else:
                return mise

    def demander_si_rejouer(solde):
        """Vérifie si l'utilisateur a encore du crédit sur son solde et si oui, lui demande de rejouer ou non"""
        if solde <= 0:
            print("\t- Votre solde n'est pas suffisant pour continuer à jouer")
            raise SystemExit
        print("\t- Votre solde est de {}€\n".format(str(solde)))
        restart = input("\t- Souhaitez-vous continuer la partie (O/N) ?\n\t- ")
        while True:
            if restart.lower() == "o":
                break
            elif restart.lower() == "n":
                raise SystemExit
            else:
                restart = input("\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n\t- ")

    mise = recup_mise(solde)
    nb_python, nb_coup, dico, nb_max, nb_coup_max = reset_param(level, mise)
    solde -= mise

    while True:
        try:
            print("Konami code ON : {}".format(nb_python))
            # Demande un nombre à l'utilisateur et s'arrête si on dépasse 10 secondes
            nb_user = int(input_with_timeout("\t- (LEVEL {} - nb entre 1 et {}) Alors mon nombre est : ?\n\t- ".format(level, nb_max), 10))
            if nb_user <= 0 or nb_user > nb_max:
                raise  ValueError()
            nb_coup += 1
            if nb_user > nb_python:
                print("\t- Votre nbre est trop grand !\n")
            elif nb_user < nb_python:
                print("\t- Votre nombre est trop petit !\n")
            # Si le joueur a trouvé le bon nombre
            else:
                gain = dico[str(level)][str(nb_coup)]
                print("\t- Bingo {}, vous avez gagné en {} coup(s) et vous avez emporté {} € !\n".format(name_user, str(nb_coup), str(gain)))
                solde += gain
                level += 1
                if (level > level_max):
                    raise SystemExit
                demander_si_rejouer(solde)
                mise = recup_mise(solde)
                nb_python, nb_coup, dico, nb_max, nb_coup_max = reset_param(level, mise)
                solde -= mise
        except ValueError:
            nb_user = print("\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {} :  ?\n".format(nb_max))
        except RuntimeError:
            nb_coup += 1
            print("\t- Vous avez dépassé le délai de 10 secondes ! Vous perdez l'essai courant\n\t\t\t et il vous reste {} essai(s) !\n".format(nb_coup_max - nb_coup))
        if nb_coup == (nb_coup_max - 1):
            print("\t- Il vous reste une chance !\n")
        if nb_coup == nb_coup_max:
            print("\t- Vous avez perdu ! Mon nombre est {} !\n".format(str(nb_python)))
            demander_si_rejouer(solde)
            mise = recup_mise(solde)
            nb_python, nb_coup, dico, nb_max, nb_coup_max = reset_param(level, mise)
            solde -= mise

except SystemExit:
    with open('donnees', 'rb') as fichier3:
        mon_depickler = pickle.Unpickler(fichier3)
        try:
            mes_donnees = mon_depickler.load()
            fichier3.close()
            mes_donnees[name_user]["Solde"] = solde
            with open('donnees', 'wb') as fichier4:
                mon_pickler = pickle.Pickler(fichier4)
                mon_pickler.dump(mes_donnees)
                fichier4.close()
        except EOFError:
            pass
    if (not solde):
        print("\t- Navré, vous avez tout perdu.. N'hésitez pas à revenir pour faire mieux la prochaine fois !")
    elif (level > level_max):
        print("\t- Bravo, vous êtes arrivé au bout des {} niveaux ! Vous repartez du casino avec {}€".format(level_max,solde))
    else:
        print("\t- Merci d'avoir joué ! Vous repartez du casino avec {}€".format(solde))
    pass