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

B :
- Sébastien
- Narcisse

C :
- Brandon
- Raïd

# Update user API

Exemples pour update user depuis `Game.py` :

```
self.connected_user.user_name = user_name_updated
self.connected_user.solde = 456
self.controller.updateUser(self.connected_user)
```

# stats

A la fin d'une partie on enregistre les stats
- l'user
- le niveau
- son nombre de tentative
- son gain
- le résultat

Les statistiques du level 1

Les statistiques de la partie

statistiques partie = statistiques cumulée des levels (manches). statistiques calculées

Voici statistiques, depuis la 1è fois jj/mm/aaaa hh:mm :

> stocker date de la partie

**stats calculées:**
- Level le plus élevé atteint est "level"
- Vous avez réussi à trouver le bon nombre dès le 1è coup "f" fois
- Le gain le plus elevé est
- La mise la plus elevé est
- Vos pires statistiques (dans l'autre sens)
- La mise moyenne est de "mise_moy"
- Le nombre moyen de tentatives pour trouver le bon nombre est
- le pourcentage de réussite

Table stats d'une manche :
- id
- user_id
- datetime
- level joué (enum: 1, 2, 3)
- nombre de tentatives pour trouver la bonne réponse
- mise
- gain
- résultat : booléan win/loose



    # stats calculées, à retourner au travers de fonctions dans Stat.py :
    # nb_first_time_win = 0 # Le nombre de fois que le user gagne du premier coup
    # nb_loose = 0
    # gain_max = 0
    # gain_min = 0
    # mise_max = 0
    # mise_moy = 0
    # mise_min = 0
    # average_nb_try = 0 # Le nombre moyen de tentatives pour trouver le bon nombre
    # highest_level = 1
    # lowest_level = 1


Exemple pour insérer des stats  depuis Game.py :

```
stats_data = {
        'level': 1,
        'attempts': 2,
        'bet': 8,
        'profit': 5,
        'result': 1
}
new_stats = self.stats_controller.createStats(self.connected_user.user_id, stats_data)
```

Exemple pour get toutes les stats d'un user depuis Game.py :

```
allstats = self.stats_controller.getStatsByUser(self.connected_user.user_id)

for stat in allstats:
    print(stat.profit)
```

# singleton

Pour tester qu'il s'agit bien du même objet, dans DBConnection faire :

```
        c1 = DBConnector.Instance()
        c2 = DBConnector.Instance()

        print("Id of c1 : {}".format(str(id(c1))))
        print("Id of c2 : {}".format(str(id(c1))))

        print("c1 is c2 ? " + str(c1 is c2))
        sys.exit()

```

Ou bien dans DBConnection faire :

```
        print("Id of Instance Connector : {}".format(str(id(cls.connector))))

```
