# ipssi-casino-python

live coding ou répartition des tâches ? : à déterminer

Le livrable c'est le repo du code

Lire et comprendre le projet : dispatcher les tâches

Datas : enregistrer les noms des joueurs dans un fichier

On part sur de la POO et on se base sur le travail de Brandon et de Sebastien

On adopte le Single responsibility principle : une fonction/méthode = une action

Il faudra penser à mettre les commentaires au niveau des classes

Liste de fonctions à implémenter :

- Déterminer si première partie ou non
- Tirer un nombre au hasard, en fonction du level
- Récupérer le nombre de l'user et le stocker

(compléter avec les TODOs du code de Brandon)

On part sur de la BDD SQLlite

A la fin d'une manche on enregistre les stats
- l'user
- le niveau
- son nombre de tentative
- son gain
- le résultat

User <--> Statistique : relation one to one

`User.py` contient déjà un constructeur depuis lequel on peut
affecter des valeurs provenant de la BDD

# MVC : option

Model User
- les propriétés de l'user seront = aux champs de la BDD


UserController :
- insertUser()
- getUser()

# groupes

1 groupe de 3
A :
- Mouhamadou
- Wissem
- Vittorio

2 groupe de 2

B : TEST
- Sébastien
- Narcisse

C :
- Brandon
- Raïd














