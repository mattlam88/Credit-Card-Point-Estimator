import sqlite3


class YearlyBudgetDAO:
    def __init__(self):
        self.conn = sqlite3.connect("/Users/mattlam/Documents/Coding Bootcamp/Final-Project-Individual-Matt/creditCard.db")
        self.cur = self.conn.cursor()

    def get_yearly_budget(self, username, year):
        cursor = self.cur.execute(
            f'SELECT restaurantSpendYearly, grocerySpendYearly, nonCategorySpendYearly, utilitySpendYearly, gasSpendYearly FROM yearlyBudget WHERE username = "{username}" AND year = {year};')
        self.conn.commit()
        for row in cursor:
            year_spend = YearlyBudget(
                id, username, year, row[0], row[1], row[2], row[3], row[4], 0)
        return year_spend

    def add_yearly_budget(self, data):
        self.cur.execute(
            f"INSERT INTO yearlyBudget (username, year, restaurantSpendYearly, grocerySpendYearly, nonCategorySpendYearly, utilitySpendYearly, gasSpendYearly) VALUES (?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_yearly_budget(self, id):
        self.cur.execute(f"DELETE FROM yearlyBudget WHERE id = {id};")
        self.conn.commit()

    def edit_yearly_budget(self, id, data):
        self.cur.execute(
            f"UPDATE yearlyBudget SET username={data[0]}, year={data[1]}, restaurantSpendYearly={data[2]}, grocerySpendYearly={data[3]}, nonCategorySpendYearly={data[4]}, utilitySpendYearly={data[5]}, gasSpendYearly={data[6]} WHERE id={id};")
        self.conn.commit()

    def edit_total_yearly_category_spend(self, username, year, total_yearly_category_spend):
        self.cur.execute(
            f"UPDATE yearlyBudget SET restaurantSpendYearly={total_yearly_category_spend[0]}, grocerySpendYearly={total_yearly_category_spend[1]}, nonCategorySpendYearly={total_yearly_category_spend[2]}, utilitySpendYearly={total_yearly_category_spend[3]}, gasSpendYearly={total_yearly_category_spend[4]} WHERE username={username} AND year={year};")
        self.conn.commit()

    def edit_total_yearly_spend(self, username, year, total_yearly_spend):
        self.cur.execute(
            f"UPDATE yearlyBudget SET yearlySpend={total_yearly_spend} WHERE username={username} AND year={year};")
        self.conn.commit()


class YearlyBudget:
    def __init__(self, id=0, username=None, year=0, restaurant_spend_yearly=0, grocery_spend_yearly=0, non_category_spend_yearly=0, utility_spend_yearly=0,  gas_spend_yearly=0, yearly_spend=0):
        self.id = id
        self.username = username
        self.year = year
        self.restaurant_spend_yearly = restaurant_spend_yearly
        self.grocery_spend_yearly = grocery_spend_yearly
        self.non_category_spend_yearly = non_category_spend_yearly
        self.utility_spend_yearly = utility_spend_yearly
        self.gas_spend_yearly = gas_spend_yearly
        self.yearly_spend = yearly_spend
        