import sqlite3


class UserDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_user(self, username):
        self.cur.execute(f"SELECT * FROM users WHERE username = {username}")

    def add_user(self, data):
        self.cur.execute(
            f"INSERT INTO users (first_name, last_name, username, password, credit_card1, credit_card2, credit_card3, budget_ID) VALUES (?,?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_user(self, username):
        self.cur.execute(f"DELETE FROM users WHERE username = {username};")
        self.conn.commit()

    def edit_user(self, id, data):
        self.cur.execute(
            f"UPDATE users SET first_name={data[0]},last_name={data[1]}, username={data[2]},maxRestaurantMultiplier={data[3]}, maxGroceryMultiplier={data[4]}, maxNonCategoryMultiplier{data[5]},maxUtilityMultiplier={data[6]}, maxGasMultiplier={data[7]} WHERE id={id};")
        self.conn.commit()

    def get_max_multipliers(self, username):
        cursor = self.cur.execute(
            f"SELECT maxRestaurantMultiplier, maxGroceryMultiplier, maxNonCategoryMultiplier, maxUtilityMultiplier, maxGasMultiplier FROM users WHERE username={username};")
        for max_multipliers in cursor:
            user_max_multipliers = [max_multipliers[0], max_multipliers[1], max_multipliers[2], max_multipliers[3], max_multipliers[4]]
            return user_max_multipliers
        self.conn.commit()

    def update_user_max_multipliers(self, username, user_max_multipliers):
        self.cur.execute(
            f"UPDATE users SET maxRestaurantMultiplier={user_max_multipliers[1]}, maxGroceryMultiplier={user_max_multipliers[2]}, maxNonCategoryMultiplier={user_max_multipliers[3]},maxUtilityMultiplier={user_max_multipliers[4]}, maxGasMultiplier={user_max_multipliers[5]}, WHERE username={username};")
        self.conn.commit()


class User:
    def __init__(self, id=0, first_name=None, last_name=None,
                 username=None, max_restaurant_multiplier=0, max_grocery_multiplier=0, max_noncat_multiplier=0,
                 max_utility_multiplier=0, max_gas_multiplier=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.max_restaurant_multiplier = max_restaurant_multiplier
        self.max_grocery_multiplier = max_grocery_multiplier
        self.max_noncat_multiplier = max_noncat_multiplier
        self.max_utility_multiplier = max_utility_multiplier
        self.max_gas_multiplier = max_gas_multiplier
