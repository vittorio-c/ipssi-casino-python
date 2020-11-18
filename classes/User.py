from datetime import date

class User :
    """ Contient les informations d'un USER """
    user_id = None # id => mot clé
    user_name = None
    is_first_time = True
    last_level = 1
    solde = 10
    create_date = date.today()

    def __init__(self, user_id, user_name, is_first_time, last_level, solde, create_date) :
        self.user_id = user_id
        self.user_name = user_name
        self.is_first_time = is_first_time
        self.last_level = last_level
        self.solde = solde
        self.create_date = create_date