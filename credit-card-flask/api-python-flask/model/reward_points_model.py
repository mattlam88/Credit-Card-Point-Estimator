import sqlite3


class RewardPointsDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_reward_points(self, id):
        self.cur.execute(f"SELECT * FROM rewardPoints WHERE id = {id}")

    def add_reward_points(self, data):
        self.cur.execute(
            f"INSERT INTO rewardPoints (reward_type, reward_point_value) VALUES (?,?);", data)
        self.conn.commit()

    def delete_reward_points(self, id):
        self.cur.execute(f"DELETE FROM rewardPoints WHERE id = {record_num};")
        self.conn.commit()

    def edit_reward_points(self, record_no, data):
        self.cur.execute(
            f"UPDATE rewardPoints SET reward_type={data[0]},reward_point_value={data[1]} WHERE id={record_no};")
        self.conn.commit()


class RewardPoints:
    def __init__(self, id=0, reward_type, reward_point_value):
        self.id = id
        self.reward_type = reward_type
        self.reward_point_value = reward_point_value
