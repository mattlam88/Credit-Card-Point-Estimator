import sqlite3

class UserMaxCreditCardMultDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_max_multipliers(self, username):
        multipliers = self.cur.execute(
            f"SELECT {username}, max(restaurantMultiplier), max(groceryMultiplier), max(nonCategoryMultiplier), max(utilityMultiplier), max(gasMultiplier) FROM creditCardDetails GROUP BY {username};")
        for multiplier in multipliers:
            user_max_multipliers = UserMaxCreditCardMult(multiplier[0], multiplier[1], multiplier[2], multiplier[3], multiplier[4], multiplier[5])
            return user_max_multipliers
        self.conn.commit()

class UserMaxCreditCardMult:
    def __init__(self, username=None, restaurant_mult=0, grocery_mult=0, non_cat_mult=0, utility_mult=0, gas_mult=0):
        self.username = username
        self.restaurant_mult = restaurant_mult
        self.grocery_mult = grocery_mult
        self.non_cat_mult = non_cat_mult
        self.utility_mult = utility_mult
        self.gas_mult = gas_mult