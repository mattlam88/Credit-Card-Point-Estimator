import sqlite3


class RewardPointsDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_month_reward_points (self, username, month, year):
        self.cur.execute(f"SELECT {month}Points FROM rewardPoints WHERE username={username} AND month={month} AND year={year};")
        self.conn.commit()

    def get_all_monthly_reward_points(self, username, year):
        cursor = self.cur.execute(f"SELECT janPoints, febPoints, marPoints, aprPoints, mayPoints, junPoints, julPoints, augPoints, sepPoints, octPoints, novPoints, decPoints FROM rewardPoints WHERE username={username} AND year={year};")
        yearly_points_balance=[]
        for points in cursor:
            yearly_points_balance.append(points)
        year_reward_points = RewardPoints(id,username,year,None,yearly_points_balance[0], yearly_points_balance[1], yearly_points_balance[2], yearly_points_balance[3],yearly_points_balance[4], yearly_points_balance[5], yearly_points_balance[6], yearly_points_balance[7], yearly_points_balance[8], yearly_points_balance[9], yearly_points_balance[10], yearly_points_balance[11])    
        self.conn.commit()
        return year_reward_points

    def add_reward_points(self, data):
        self.cur.execute(
            f"INSERT INTO rewardPoints (reward_type, reward_point_value) VALUES (?,?);", data)
        self.conn.commit()

    def delete_reward_points(self, id):
        self.cur.execute(f"DELETE FROM rewardPoints WHERE id = {id};")
        self.conn.commit()

    def edit_reward_points(self, id, data):
        self.cur.execute(
            f"UPDATE rewardPoints SET reward_type={data[0]},reward_point_value={data[1]} WHERE id={id};")
        self.conn.commit()

    def update_monthly_reward_points(self, username, month, year, points_balance):
        self.cur.execute(
            f"UPDATE rewardPoints SET {month}_points = {points_balance} WHERE username={username} AND month={month} AND year={year};")
        self.conn.commit()

    def update_total_year_points(self, username, year, points_balance):
        self.cur.execute(f"UPDATE rewardPoints SET totalYearPoints={points_balance} WHERE username={username} AND year={year}")
        self.conn.commit()

    def update_reward_points_FMV(self, username, year, reward_FMV):
        self.cur.execute(f"UPDATE rewardPoints SET pointsFMV={reward_FMV} WHERE username={username} AND year={year};")
        self.conn.commit()

    def join_reward_expected_value(self, username, year):
        cursor = self.cur.execute(
            f"SELECT  rewardPoints.username, rewardPoints.rewardType, rewardPoints.totalYearPoints, rewardPointsEV.expectedValue FROM rewardPoints LEFT JOIN rewardPointsEV ON rewardPointsEV.rewardType = rewardPoints.rewardType WHERE rewardPoints.username={username} AND rewardPoints.year={year};")
        
        reward_points_data = []
        for reward_info in cursor:
            reward_points_data.append(reward_info)
        self.conn.commit()  
        rewards_data = RewardPointsJoinEV(reward_points_data[0], reward_points_data[1], reward_points_data[2], reward_points_data[3])     
        return rewards_data

class RewardPoints:
    def __init__(self, id=0, username=None, year=0, reward_type=None,
                 jan_points=0, feb_points=0, mar_points=0, apr_points=0, may_points=0, jun_points=0,
                 jul_points=0, aug_points=0, sep_points=0, oct_points=0, nov_points=0, dec_points=0, 
                 total_year_points=0, reward_points_FMV=0):
        self.id = id
        self.username = username
        self.year = year
        self.reward_type = reward_type
        self.jan_points = jan_points
        self.feb_points = feb_points
        self.mar_points = mar_points
        self.apr_points = apr_points
        self.may_points = may_points
        self.jun_points = jun_points
        self.jul_points = jul_points
        self.aug_points = aug_points
        self.sep_points = sep_points
        self.oct_points = oct_points
        self.nov_points = nov_points
        self.dec_points = dec_points
        self.total_year_points = total_year_points
        self.reward_points_FMV = reward_points_FMV

class RewardPointsJoinEV:
    def __init__(self, username=None, reward_type=None, total_year_points=0, expected_point_value=0):
        self.username = username
        self.reward_type = reward_type
        self.total_year_points = total_year_points
        self.expected_point_value = expected_point_value
