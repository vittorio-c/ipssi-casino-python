import sys
from classes.Stat import Stat
from classes.Database.DBConnection import DBConnection

class StatRepository:

    def createStats(self, stats_model):
        bindings = stats_model.__dict__

        sql = ''' INSERT INTO stats (user_id, level, attempts, bet, profit, result)
                  VALUES(:user_id, :level, :attempts, :bet, :profit, :result) '''

        stat_id = DBConnection.insert_data(sql, bindings)
        stat_model = self.getStatById(stat_id)

        return stat_model

    def getStatById(self, stat_id):
        bindings = tuple([stat_id])

        sql = ''' SELECT * FROM stats WHERE stats.id = ? '''

        stats_row = DBConnection.get_data(sql, bindings)
        stat_id, user_id, created_at, level, attempts, bet, profit, result = list(stats_row[0])
        stat_model = Stat(user_id, level, attempts, bet, profit, result, created_at, stat_id)

        return stat_model


    def getStatsByUserId(self, user_id) :
        bindings = tuple([user_id])

        sql = ''' SELECT * FROM stats WHERE stats.user_id = ? '''

        stats_rows = DBConnection.get_data(sql, bindings)
        results = []

        for row in stats_rows:
            stat_id, user_id, created_at, level, attempts, bet, profit, result = list(row)
            stat_model = Stat(user_id, level, attempts, bet, profit, result, created_at, stat_id)
            results.append(stat_model)

        return results
