import sqlite3


class MonthlyBudgetDAO:
    def __init__(self):
        self.conn = sqlite3.connect("/Users/mattlam/Documents/Coding Bootcamp/Final-Project-Individual-Matt/creditCard.db")
        self.cur = self.conn.cursor()

    def get_monthly_budget(self, username, month, year):
        monthly_budget_data = self.cur.execute(
            f'SELECT restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend FROM monthlyBudget WHERE username = "{username}" AND month = "{month}" AND year = {year};')
        self.conn.commit()
        for data in monthly_budget_data:
            month_spend = MonthlyBudget(
                id, username, month, year, data[0], data[1], data[2], data[3], data[4])
            return month_spend
        
    def get_total_monthly_category_spend(self, username, year):
        total_monthly_category_spend = self.cur.execute(
            f'SELECT username, year, sum(restaurantSpend), sum(grocerySpend), sum(nonCategorySpend), sum(utilitySpend), sum(gasSpend) FROM monthlyBudget WHERE username = "{username}" AND year = {year} GROUP BY username AND year;')
        self.conn.commit()
        for spend in total_monthly_category_spend:
            monthly_category_spend = YearlyCategorySpend(
                spend[0], spend[1], spend[2], spend[3], spend[4], spend[5], spend[6])
        return monthly_category_spend

    def get_all_monthly_user_spend(self, username, year):
        user_month_spend = {}

        month_spend = self.cur.execute(f'SELECT id, username, month, year, restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend, monthlySpend FROM monthlyBudget WHERE username="{username}" AND year={year};')
        self.conn.commit()
        for info in month_spend:
            month = info[2]
            user_month_spend[month] = MonthlyBudget(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9])
        print(user_month_spend)
       # accessing information user_month_spend['January'].monthlySpend
        return user_month_spend
        # Will need to think through this

    def add_monthly_budget(self, data):
        self.cur.execute(
            f"INSERT INTO monthlyBudget (username, month, year, restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend, monthlySpend) VALUES (?,?,?,?,?,?,?,?,?);", data)
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
            f'UPDATE monthlyBudget SET monthlySpend={total_month_spend} WHERE username="{username}" AND month="{month}" AND year={year};')
        self.conn.commit()

class MonthlyBudget:
    def __init__(self, id, username=None, month=None, year=0,
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
    
    def toJSON(self):
        return self.__dict__


# class MonthlyYTDSpend:
#     def __init__(self, username=None, year=0, jan_spend=0, feb_spend=0,
#                  mar_spend=0, apr_spend=0, may_spend=0, june_spend=0,
#                  july_spend=0, aug_spend=0, sept_spend=0, oct_spend=0,
#                  nov_spend=0, dec_spend=0):
#         self.username = username
#         self.year = year
#         self.jan_spend = jan_spend
#         self.feb_spend = feb_spend
#         self.mar_spend = mar_spend
#         self.apr_spend = apr_spend
#         self.may_spend = may_spend
#         self.june_spend = june_spend
#         self.july_spend = july_spend
#         self.aug_spend = aug_spend
#         self.sept_spend = sept_spend
#         self.oct_spend = oct_spend
#         self.nov_spend = nov_spend
#         self.dec_spend = dec_spend


class YearlyCategorySpend:
    def __init__(self, username=None, year=0, yearly_restaurant_spend=0, yearly_grocery_spend=0, yearly_non_cat_spend=0, yearly_utility_spend=0, yearly_gas_spend=0):
        self.username = username
        self.year = year
        self.yearly_restaurant_spend = yearly_restaurant_spend
        self.yearly_grocery_spend = yearly_grocery_spend
        self.yearly_non_cat_spend = yearly_non_cat_spend
        self.yearly_utility_spend = yearly_utility_spend
        self.yearly_gas_spend = yearly_gas_spend
