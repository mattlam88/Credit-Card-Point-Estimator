import sqlite3

class RewardPointsEVDAO:
    def __init__(self):
        self.conn = sqlite3.connect("/Users/mattlam/Documents/Coding Bootcamp/Final-Project-Individual-Matt/creditCard.db")
        self.cur = self.conn.cursor()

    def add_reward_type_EV(self, reward_type, expected_value):
        self.cur.execute(
            f"INSERT INTO rewardPointsEV (rewardType, expectedValue) VALUES (?,?);", reward_type, expected_value)
        self.conn.commit()

    def delete_reward_type_EV(self, reward_type):
        self.cur.execute(f"DELETE FROM rewardPointsEV WHERE rewardType = {reward_type};")
        self.conn.commit()

    def update_reward_expected_value(self, reward_type, expected_value):
        self.cur.execute(f"UPDATE rewardPointsEV SET expectedValue={expected_value} WHERE reward_type={reward_type};")
        self.conn.commit()

class RewardPointsEV:
    def __init__(self, id=0, reward_type=None, expected_value=0):
        self.id = id
        self.reward_type = reward_type
        self.expected_value = expected_value