from classes.Stat import Stat
from operator import itemgetter
from classes.Database.Repository.StatRepository import StatRepository

class StatsController :
    """ Permet de réaliser des opérations sur les stats"""

    def __init__(self) :
        self.stat_repo = StatRepository()

    def createStats(self, user_id, stats_data) :
        """ Insert une stat en base de données """
        try:
            self.validateStatData(stats_data)
            level, attempts, bet, profit, result = itemgetter('level', 'attempts', 'bet', 'profit', 'result')(stats_data)
            stats_model = Stat(user_id, level, attempts, bet, profit, result)
            return self.stat_repo.createStats(stats_model)
        except (TypeError, ValueError) as e:
            print('Sorry, we could not create the stats.')
            print(e)

    def getStatsByUser(self, user_id) :
        """ Récupère les stats models via le user depuis la base de données
            :return: list(Stat,)
        """
        stats_models = self.stat_repo.getStatsByUserId(user_id)

        return stats_models

    def validateStatData(self, stat_data) :
        """ Vérifie les datas avant insertion en stat_repo """
        try :
            if stat_data['level'] not in (1, 2, 3) :
                raise TypeError()

            if not isinstance(stat_data['attempts'], int) :
                raise TypeError()

            if not isinstance(stat_data['bet'], int) :
                raise TypeError()

            if not isinstance(stat_data['profit'], int) :
                raise TypeError()

            if int(stat_data['result']) not in (0, 1) :
                raise TypeError()

        except (TypeError, ValueError) as e:
            raise e
