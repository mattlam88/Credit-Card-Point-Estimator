import sqlite3


class YearlyBudgetDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def get_yearly_budget(self, username, year):
        cursor = self.cur.execute(
            f"SELECT janSpendTotal, febSpendTotal, marSpendTotal, aprSpendTotal, maySpendTotal, juneSpendTotal, julySpendTotal, augSpendTotal, septSpendTotal, octSpendTotal, novSpendTotal, decSpendTotal FROM yearlyBudget WHERE id = {username}, {year}")
        for row in cursor:
            year_spend = YearlyBudget(
                username, year, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
            return year_spend
        self.conn.commit()

    def add_yearly_budget(self, data):
        self.cur.execute(
            f"INSERT INTO budget (username, month, restaurant_spend, grocery_spend, non_cat_spend, utility_spend, gas_spend) VALUES (?,?,?,?,?,?,?);", data)
        self.conn.commit()

    def delete_yearly_budget(self, id):
        self.cur.execute(f"DELETE FROM budget WHERE id = {id};")
        self.conn.commit()

    def edit_yearly_budget(self, id, data):
        self.cur.execute(
            f"UPDATE budget SET username={data[0]},restaurant_spend={data[1]}, grocery_spend={data[2]},non_cat_spend={data[3]},utility_spend={data[4]},gas_spend={data[5]} WHERE id={id};")
        self.conn.commit()

    def edit_yearly_spend_total(self, username, year, data):
        self.cur.execute(
            f"UPDATE budget SET yearlySpendTotal WHERE username={username}, year={year};")
        self.conn.commit()
        # will update to include code to edit yearly total spend for a user

    def get_yearly_spend_total(self, username, year, data):
        self.cur.execute(
            f"SELECT yearlySpendTotal WHERE username={username}, year={year};")

        self.conn.commit()


class YearlyBudget:
    def __init__(self, username=None, year=0, jan_spend_total=0, feb_spend_total=0, mar_spend_total=0, apr_spend_total=0, may_spend_total=0,
                 june_spend_total=0, july_spend_total=0, aug_spend_total=0, sept_spend_total=0, oct_spend_total=0, nov_spend_total=0,
                 dec_spend_total=0, yearly_spend_total=0, jan_points_total=0, feb_points_total=0, mar_points_total=0, apr_points_total=0, may_points_total=0,
                 june_points_total=0, july_points_total=0, aug_points_total=0, sept_points_total=0, oct_points_total=0, nov_points_total=0,
                 dec_points_total=0, yearly_points_total=0):
        self.username = username
        self.year = year
        self.jan_spend_total = jan_spend_total
        self.feb_spend_total = feb_spend_total
        self.mar_spend_total = mar_spend_total
        self.apr_spend_total = apr_spend_total
        self.may_spend_total = may_spend_total
        self.june_spend_total = june_spend_total
        self.july_spend_total = july_spend_total
        self.aug_spend_total = aug_spend_total
        self.sept_spend_total = sept_spend_total
        self.oct_spend_total = oct_spend_total
        self.nov_spend_total = nov_spend_total
        self.dec_spend_total = dec_spend_total
        self.yearly_spend_total = yearly_spend_total
        self.jan_points_total = jan_points_total
        self.feb_points_total = feb_points_total
        self.mar_points_total = mar_points_total
        self.apr_points_total = apr_points_total
        self.may_points_total = may_points_total
        self.june_points_total = june_points_total
        self.july_points_total = july_points_total
        self.aug_points_total = aug_points_total
        self.sept_points_total = sept_points_total
        self.oct_points_total = oct_points_total
        self.nov_points_total = nov_points_total
        self.dec_points_total = dec_points_total
        self.yearly_points_total = yearly_points_total
