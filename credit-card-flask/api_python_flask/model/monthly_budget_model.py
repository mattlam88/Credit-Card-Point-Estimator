import sqlite3


class MonthlyBudgetDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_monthly_budget(self, id):
        self.cur.execute(f"SELECT * FROM monthlyBudget WHERE id = {id}")

    def add_monthly_budget(self, data):
        self.cur.execute(
            f"INSERT INTO monthlyBudget (username, month, restaurant_spend, grocery_spend, non_cat_spend, utility_spend, gas_spend) VALUES (?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_monthly_budget(self, id):
        self.cur.execute(f"DELETE FROM monthlyBudget WHERE id = {id};")
        self.conn.commit()

    def edit_monthly_budget(self, id, data):
        self.cur.execute(
            f"UPDATE monthlyBudget SET username={data[0]},restaurant_spend={data[1]}, grocery_spend={data[2]},non_cat_spend={data[3]},utility_spend={data[4]},gas_spend={data[5]} WHERE id={id};")
        self.conn.commit()


class MonthlyBudget:
    def __init__(self, id=0, username=None, month=None,
                 restaurant_spend=0, grocery_spend=0, non_cat_spend=0,
                 utility_spend=0, gas_spend=0):
        self.id = id
        self.username = username
        self.month = month
        self.restaurant_spend = restaurant_spend
        self.grocery_spend = grocery_spend
        self.non_cat_spend = non_cat_spend
        self.utility_spend = utility_spend
        self.gas_spend = gas_spend

