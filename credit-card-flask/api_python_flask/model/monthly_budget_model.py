import sqlite3


class MonthlyBudgetDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_monthly_budget(self, username, month, year):
        cursor = self.cur.execute(
            f"SELECT restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend FROM monthlyBudget WHERE username = {username} AND month = {month} AND year = {year};")
        for row in cursor:
            month_spend = MonthlyBudget(
                id, username, month, year, row[0], row[1], row[2], row[3], row[4])
            return month_spend
        self.conn.commit()

    def get_total_monthly_category_spend(self, username, year):
        cursor = self.cur.execute(
            f"SELECT sum(dollars) restaurantSpend, sum(dollars) grocerySpend, sum(dollars) nonCategorySpend, sum(dollars) utilitySpend, sum(dollars) gasSpend FROM monthlyBudget WHERE username = {username} AND year = {year};")
        for row in cursor:
            monthly_category_spend = [row[0], row[1], row[2], row[3], row[4]] 
        return monthly_category_spend
        
    def get_all_monthly_user_spend(self, username, year):
        cursor = self.cur.execute(
            f"SELECT sum(dollars) monthlySpend FROM monthlyBudget WHERE username={username} AND year={year};")
        for row in cursor:
            year_spend = row[0]
        return year_spend

    def add_monthly_budget(self, data):
        self.cur.execute(
            f"INSERT INTO monthlyBudget (username, month, year, restaurant_spend, grocery_spend, non_cat_spend, utility_spend, gas_spend) VALUES (?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_monthly_budget(self, id):
        self.cur.execute(f"DELETE FROM monthlyBudget WHERE id = {id};")
        self.conn.commit()

    def edit_monthly_budget(self, id, data):
        self.cur.execute(
            f"UPDATE monthlyBudget SET username={data[0]},restaurant_spend={data[1]}, grocery_spend={data[2]},non_cat_spend={data[3]},utility_spend={data[4]},gas_spend={data[5]} WHERE id={id};")
        self.conn.commit()

    def edit_monthly_total_spend(self, username, month, year, total_month_spend):
        self.cur.execute(
            f"UPDATE monthlyBudget SET monthlySpend={total_month_spend} WHERE username={username} AND month={month} AND year={year};")
        self.conn.commit()


class MonthlyBudget:
    def __init__(self, id=0, username=None, month=None, year=0,
                 restaurant_spend=0, grocery_spend=0, non_cat_spend=0,
                 utility_spend=0, gas_spend=0, monthly_spend=0):
        self.id = id
        self.username = username
        self.month = month
        self.year = year
        self.restaurant_spend = restaurant_spend
        self.grocery_spend = grocery_spend
        self.non_cat_spend = non_cat_spend
        self.utility_spend = utility_spend
        self.gas_spend = gas_spend
        self.monthly_spend = monthly_spend
