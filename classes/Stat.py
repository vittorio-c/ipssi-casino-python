class Stat :
    """ Contient les Stats d'un user sur une manche """

    stat_id = None
    user_id = None
    created_at = None
    level = None
    attempts = None
    bet = None
    profit = None
    result = None

    # nb_coup = None
    # mise = None
    # gain = None
    def __init__(self, user_id, level, attempts, bet, profit, result, created_at = None, stat_id = None) :
        self.user_id = user_id
        self.level = level
        self.attempts = attempts
        self.bet = bet
        self.profit = profit
        self.result = result
        self.stat_id = stat_id
        self.created_at = created_at
