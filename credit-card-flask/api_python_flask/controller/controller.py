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

        yearly_spend = f"SELECT {year} SUM(restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend) FROM monthlyBudget GROUP BY {year};"
        insert_yearly_spend_total = f"INSERT INTO yearlyBudget ({year},yearly_spend_total) VALUES (?,?);"

        cur.execute(yearly_spend, insert_yearly_spend_total)
        cur.close()
        # this function will sum up 
    
    def calc_budget_rewards(self):
        # this needs to be updated
        conn = sqlite3.connect('creditCard.db')
        cur = conn.cursor()

        yearly_spend = f"SELECT {year} SUM(restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend) FROM monthlyBudget GROUP BY {year};"
        insert_yearly_spend_total = f"INSERT INTO yearlyBudget ({year},yearly_spend_total) VALUES (?,?);"

        cur.execute(yearly_spend, insert_yearly_spend_total)
        cur.close()

        # this function will take the budget table and credit card details to calculate total rewards collected

    def calc_rewards_exp_value(self):
        # this needs to be updated
        conn = sqlite3.connect('creditCard.db')
        cur = conn.cursor()

        yearly_spend = f"SELECT {year} SUM(restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend) FROM monthlyBudget GROUP BY {year};"
        insert_yearly_spend_total = f"INSERT INTO yearlyBudget ({year},yearly_spend_total) VALUES (?,?);"

        cur.execute(yearly_spend, insert_yearly_spend_total)
        cur.close()
        # this function will take the total rewards collected and multiply it by its "FMV"
        pass