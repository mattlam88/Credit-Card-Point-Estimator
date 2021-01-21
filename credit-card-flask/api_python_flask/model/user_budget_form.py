import sqlite3


class UserBudgetFormDAO:
    def __init__(self):
        self.conn = sqlite3.connect(
            "/Users/mattlam/Documents/Coding Bootcamp/Final-Project-Individual-Matt/creditCard.db")
        self.cur = self.conn.cursor()

    def add_user_budget_form(self, data):
        self.cur.execute(
            f'INSERT INTO userBudgetForm (username, month, year, restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend) VALUES (?,?,?,?,?,?,?,?);', data)
        self.conn.commit()

    def get_user_budget_form(self, username, year):
        user_budget = {
            'January': [],
            'February': [],
            'March': [],
            'April': [],
            'May': [],
            'June': [],
            'July': [],
            'August': [],
            'September': [],
            'October': [],
            'November': [],
            'December': []
        }

        user_budget_info = self.cur.execute(f'SELECT id, username, month, year, restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend FROM userBudgetForm WHERE username={username} AND year={year};')
        for info in user_budget_info:
            month = info[2]
            user_budget[month].append(UserBudgetForm(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8]))
        return user_budget


class UserBudgetForm:
    def __init__(self, id, username=None, month=None, year=0,
                 restaurant_spend=0, grocery_spend=0, non_category_spend=0,
                 utility_spend=0, gas_spend=0):
        self.id = id
        self.username = username
        self.month = month
        self.year = year
        self.restaurant_spend = restaurant_spend
        self.grocery_spend = grocery_spend
        self.non_category_spend = non_category_spend
        self.utility_spend = utility_spend
        self.gas_spend = gas_spend
