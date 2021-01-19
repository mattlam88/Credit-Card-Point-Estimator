import sqlite3

class UserBudgetFormDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def add_user_budget_form(self, data):
        self.cur.execute()
        self.conn.commit()

    def get_user_budget_form(self, username):
        user_budget_info = self.cur.execute()
        for info in user_budget_info:
            user_budget = UserBudgetForm()
        return user_credit_card


class UserBudgetForm:
    def __init__(self, id=0, username=None, month=None, year=0,
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
