import sqlite3

from api_python_flask.model.monthly_budget_model import MonthlyBudgetDAO, MonthlyBudget
from api_python_flask.model.yearly_budget_model import YearlyBudgetDAO, YearlyBudget
from api_python_flask.model.credit_card_model import CreditCardDAO, CreditCard
from api_python_flask.model.reward_points_model import RewardsPointsDAO, RewardPoints
from api_python_flask.model.user_model import UserDAO, User


class Controller:
    def __init__(self):
        pass

    def calc_total_monthly_spend(self, year, month):
        conn = sqlite3.connect('creditCard.db')
        cur = conn.cursor()

        monthly_spend = f"SELECT {year}, {month} SUM(restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend) FROM monthlyBudget GROUP BY {year}, {month};"
        insert_monthly_spend_total = f"INSERT INTO yearlyBudget ({year},{month}_spend_total) VALUES (?,?);"

        cur.execute(monthly_spend, insert_monthly_spend_total)
        cur.close()
        # this function will add up each monthly spend by year


    def calc_total_yearly_spend(self, year):
        conn = sqlite3.connect('creditCard.db')
        cur = conn.cursor()

        yearly_spend = f"SELECT {year} SUM(janSpendTotal, febSpendTotal, marSpendTotal, aprSpendTotal, maySpendTotal, juneSpendTotal, julySpendTotal, augSpendTotal, septSpendTotal, octSpendTotal, novSpendTotal, decSpendTotal) FROM yearlyBudget GROUP BY {year};"
        insert_yearly_spend_total = f"INSERT INTO yearlyBudget ({year},yearly_spend_total) VALUES (?,?);"

        cur.execute(yearly_spend, insert_yearly_spend_total)
        cur.close()
        # this function will sum up

    def calc_budget_rewards(self):
        conn = sqlite3.connect('creditCard.db')
        cur = conn.cursor()

        monthBudget_join_rewardPoints = """
        SELECT id FROM yearlyTable
        INNER JOIN rewardPoints ON yearlyTable.column = rewardPoints.column;
        """

        insert_yearly_spend_total = f"INSERT INTO yearlyBudget ({year},yearly_spend_total) VALUES (?,?);"

        cur.execute(yearly_spend, insert_yearly_spend_total)
        cur.close()

        # this function will take the budget table and credit card details to calculate total rewards collected

    def calc_rewards_exp_value(self):
        # this function will take the total rewards collected and multiply it by its "FMV"
        pass


class MonthlyBudgetService:
    def __init__(self):
        pass
    def calculate_monthly_budget():
        # this will use DAO to query the database to get the monthly spend information and then run the addition operation, then the DAO will save/update the database.
        months = [jan, feb, mar, apr, may, june, july, aug, sept, oct, nov, dec]
        # imagine this a for loop
        monthly_spend = MonthlyBudgetDAO.get_monthly_budget(username,months)

        

