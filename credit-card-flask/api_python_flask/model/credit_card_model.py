import sqlite3


class CreditCardDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_user_credit_cards(self, username):
        self.cur.execute(f"SELECT brand, cardType FROM creditCardDetails WHERE username = {username};")

    def add_credit_card(self, data):
        self.cur.execute(
            f"INSERT INTO creditCardDetails (brand, card_type, reward_type, restaurant_mult, grocery_mult, non_cat_mult, utility_mult, gas_mult) VALUES (?,?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_credit_card(self, id):
        self.cur.execute(f"DELETE FROM creditCardDetails WHERE id = {id};")
        self.conn.commit()

    def edit_credit_card(self, id, data):
        self.cur.execute(
            f"UPDATE creditCardDetails SET brand={data[0]},card_type={data[1]}, reward_type={data[2]},restaurant_mult={data[3]},non_cat_mult={data[4]},gas_mult={data[5]} WHERE id={id};")
        self.conn.commit()

    def get_max_multipliers(self, username):
        cursor = self.cur.execute(
            f"SELECT {username}, max(restaurantMultiplier), max(groceryMultiplier), max(nonCategoryMultiplier), max(utilityMultiplier), max(gasMultiplier) FROM creditCardDetails GROUP BY {username};")
        for row in cursor:
            user_max_multipliers = [row[0], row[1], row[2], row[3], row[4], row[5]]
            return user_max_multipliers
        self.conn.commit()


class CreditCard:
    def __init__(self, id=0, username=None, brand=None, card_type=None, reward_type=None, restaurant_mult=0, grocery_mult=0, non_cat_mult=0, utility_mult=0, gas_mult=0):
        self.id = id
        self.username = username
        self.brand = brand
        self.card_type = card_type
        self.reward_type = reward_type
        self.restaurant_mult = restaurant_mult
        self.grocery_mult = grocery_mult
        self.non_cat_mult = non_cat_mult
        self.gas_mult = gas_mult
