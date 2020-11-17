from datetime import date

class User :
    """ Contient les informations d'un USER """

    user_name = None
    is_first_time = True
    last_level = 1
    list_mise = []
    successful_nb_try = [] # Le nombre moyen de tentatives pour trouver le bon nombre est
    highest_level = 1
    lowest_level = 1
    nb_first_time_win = 0
    nb_loose = 0
    gain_max = 0
    gain_min = 0
    mise_max = 0
    mise_moy = 0
    mise_min = 0
    create_date = date.today()

    def __init__(self, user_name = '', is_first_time = True, last_level = 1, list_mise = [], successful_nb_try = [],
                    highest_level = 1, lowest_level = 1, nb_first_time_win = 0, nb_loose = 0, gain_max = 0, gain_min = 0,
                    mise_max = 0, mise_moy = 0, mise_min = 0, create_date = date.today()) :
        self.user_name = user_name
        self.is_first_time = is_first_time
        self.last_level = last_level
        self.list_mise = list_mise
        self.successful_nb_try = successful_nb_try
        self.highest_level = highest_level
        self.lowest_level = lowest_level
        self.nb_first_time_win = nb_first_time_win
        self.nb_loose = nb_loose
        self.gain_max = gain_max
        self.gain_min = gain_min
        self.mise_max = mise_max
        self.mise_moy = mise_moy
        self.mise_min = mise_min
        self.create_date = create_date

    #TODO: Implementer les fonctions modifiant les propriétés d'un USER