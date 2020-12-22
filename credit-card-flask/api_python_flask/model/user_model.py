import sqlite3


class UserDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_user(self, id):
        self.cur.execute(f"SELECT * FROM users WHERE id = {id}")

    def add_user(self, data):
        self.cur.execute(
            f"INSERT INTO users (first_name, last_name, username, password, credit_card1, credit_card2, credit_card3, budget_ID) VALUES (?,?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_user(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id = {id};")
        self.conn.commit()

    def edit_user(self, id, data):
        self.cur.execute(
            f"UPDATE users SET first_name={data[0]},last_name={data[1]}, username={data[2]},password={data[3]},credit_card1={data[4]},credit_card2={data[5]},credit_cart3={data[6]} WHERE id={id};")
        self.conn.commit()


class User:
    def __init__(self, id=0, first_name=None, last_name=None,
                 username=None, password=None, credit_card1=0, 
                 credit_card2=0, credit_card3=0, budget_ID=0,
                 credit_card_one_points_total=0, credit_card_two_points_total=0, credit_crd_three_points_total=0,
                 credit_card_one_points_fmv=0, credit_cardtwo_points_fmv=0, credit_card_three_points_fmv=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.credit_card1 = credit_card1
        self.credit_card2 = credit_card2
        self.credit_card3 = credit_card3
        self.budget_ID = budget_ID
        self.credit_card_one_points_total = credit_card_one_points_total
        self.credit_card_two_points_total = credit_card_two_points_total
        self.credit_crd_three_points_total = credit_crd_three_points_total
        self.credit_card_one_points_fmv = credit_card_one_points_fmv
        self.credit_cardtwo_points_fmv = credit_cardtwo_points_fmv
        self.credit_card_three_points_fmv = credit_card_three_points_fmv
