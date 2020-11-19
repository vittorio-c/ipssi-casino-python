from classes.SqliteDatabase import SqliteDatabase
from classes.Stat import Stat
from operator import itemgetter

class StatsController :
    """ Permet de réaliser des opérations sur les stats"""

    database = None

    def __init__(self) :
        self.database = SqliteDatabase()

    def createStats(self, user_id, stats_data) :
        """ Insert une stat en base de données """
        try:
            self.validateStatData(stats_data)
            level, attempts, bet, profit, result = itemgetter('level', 'attempts', 'bet', 'profit', 'result')(stats_data)
            stats_model = Stat(user_id, level, attempts, bet, profit, result)
            return self.database.createStats(stats_model)
        except (TypeError, ValueError) as e:
            print('Sorry, we could not create the stats.')
            print(e)

    def getStatsByUser(self, user_id) :
        """ Récupère les stats models via le user depuis la base de données
            :return: list(Stat,)
        """
        stats_models = self.database.getStatsByUserId(user_id)
        return stats_models

    def validateStatData(self, stat_data) :
        """ Vérifie les datas avant insertion en database """
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
