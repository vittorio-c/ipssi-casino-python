class Stat :
    """ Contient les Stats d'un USER """

    user_id = None
    stat_id = None
    average_nb_try = 0 # Le nombre moyen de tentatives pour trouver le bon nombre
    highest_level = 1
    lowest_level = 1
    nb_first_time_win = 0 # Le nombre de fois que le user gagne du premier coup
    nb_loose = 0
    gain_max = 0
    gain_min = 0
    mise_max = 0
    mise_moy = 0
    mise_min = 0

    def __init__(self, user_id, stat_id, list_mise, successful_nb_try, highest_level, lowest_level, nb_first_time_win,
                    nb_loose, gain_max, gain_min, mise_max, mise_moy, mise_min) :
        self.user_id = user_id
        self.stat_id = stat_id
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