import sqlite3


class CreditCardDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_credit_card(self, id):
        self.cur.execute(f"SELECT * FROM creditCardDetails WHERE id = {id}")

    def add_credit_card(self, data):
        self.cur.execute(
            f"INSERT INTO creditCardDetails (brand, card_type, reward_type, restaurant_mult, grocery_mult, non_cat_mult, utility_mult, gas_mult) VALUES (?,?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_credit_card(self, id):
        self.cur.execute(f"DELETE FROM creditCardDetails WHERE id = {record_num};")
        self.conn.commit()

    def edit_credit_card(self, record_no, data):
        self.cur.execute(
            f"UPDATE creditCardDetails SET brand={data[0]},card_type={data[1]}, reward_type={data[2]},restaurant_mult={data[3]},non_cat_mult={data[4]},gas_mult={data[5]} WHERE id={record_no};")
        self.conn.commit()


class CreditCard:
    def __init__(self, id=0, brand, card_type, reward_type, restaurant_mult, grocery_mult, non_cat_mult, utility_mult, gas_mult):
        self.id = id
        self.brand = brand
        self.card_type = card_type
        self.reward_type = reward_type
        self.restaurant_mult = restaurant_mult
        self.grocery_mult = grocery_mult
        self.non_cat_mult = non_cat_mult
        self.gas_mult = gas_mult
