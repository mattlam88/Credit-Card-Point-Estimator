import sqlite3

from api_python_flask.model.monthly_budget_model import MonthlyBudgetDAO, MonthlyBudget
from api_python_flask.model.yearly_budget_model import YearlyBudgetDAO, YearlyBudget
from api_python_flask.model.credit_card_model import CreditCardDAO, CreditCard
from api_python_flask.model.reward_points_model import RewardsPointsDAO, RewardPoints
from api_python_flask.model.user_model import UserDAO, User


class Controller:
    def __init__(self):
        pass

class MonthlyBudgetService:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()

    def calculate_total_monthly_budget(self, username, month, year):
        monthly_spend = MonthlyBudgetDAO.get_monthly_budget(username, month, year)
        total_month_spend = monthly_spend[4]+monthly_spend[5]+monthly_spend[6]+monthly_spend[7]+monthly_spend[8]
        self.MonthlyBudgetDAO.edit_monthly_total_spend(username, month, year, total_month_spend)
        # this will sum up each month by adding up each category spend


class YearlyBudgetServce:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()
        self.YearlyBudgetDAO = YearlyBudgetDAO()

    def calc_total_yearly_category_spend(self, username, year):
        total_yearly_category_spend = MonthlyBudgetDAO.get_total_monthly_category_spend(username, year)
        self.YearlyBudgetDAO.edit_total_yearly_category_spend(username, year, total_yearly_category_spend)

    def calc_total_yearly_spend(self, username, year):
        total_yearly_spend = MonthlyBudgetDAO.get_all_monthly_user_spend(username, year)
        self.YearlyBudgetDAO.edit_yearly_budget(username, year, total_yearly_spend)
        # update the yearlySpend table with the total yearly spend by aggregating all of the monthly spend totals

class RewardPointsService:
    def __init__(self):
        self.YearlyBudgetDAO = YearlyBudgetDAO()
        self.CreditCardDAO = CreditCardDAO()
        self.UserDAO = UserDAO()
        self.User = User()

    def calc_reward_points_monthly(self, username, month, credit_card_id):
        pass

    def calc_reward_points_yearly(self,username, year, credit_card_id):
        yearly_spend = YearlyBudgetDAO.get_yearly_spend_total(username, year)
        pass



class FMVRewardsPointsService:
    def calc_rewards_exp_value(self):
        # this function will take the total rewards collected and multiply it by its "FMV"
        # will need to join user's points table and multiply it by the EV of the points to get this value
        pass


        

