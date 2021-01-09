import sqlite3

from api_python_flask.model.monthly_budget_model import MonthlyBudgetDAO, MonthlyBudget
from api_python_flask.model.yearly_budget_model import YearlyBudgetDAO, YearlyBudget
from api_python_flask.model.credit_card_model import CreditCardDAO, CreditCard
from api_python_flask.model.reward_points_model import RewardPointsDAO, RewardPoints
from api_python_flask.model.user_model import UserDAO, User
from api_python_flask.model.user_max_multipliers import UserMaxCreditCardMult, UserMaxCreditCardMultDAO
from api_python_flask.model.reward_points_expected_value_model import RewardPointsEVDAO, RewardPointsEV

class MonthlyBudgetService:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()

    def calculate_total_monthly_budget(self, username, month, year):
        monthly_spend = MonthlyBudgetDAO.get_monthly_budget(username, month, year)
        total_month_spend = monthly_spend.restaurant_spend + monthly_spend.grocery_spend + monthly_spend.non_cat_spend + monthly_spend.utility_spend + monthly_spend.gas_spend
        self.MonthlyBudgetDAO.edit_monthly_total_spend(username, month, year, total_month_spend)
        # this will sum up each month by adding up each category spend

class YearlyBudgetService:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()
        self.YearlyBudgetDAO = YearlyBudgetDAO()

    def calc_total_yearly_category_spend(self, username, year):
        total_yearly_category_spend = MonthlyBudgetDAO.get_total_monthly_category_spend(username, year)
        self.YearlyBudgetDAO.edit_total_yearly_category_spend(username, year, total_yearly_category_spend)

    def calc_total_yearly_spend(self, username, year):
        year_spend = MonthlyBudgetDAO.get_all_monthly_user_spend(username, year)
        total_year_spend = sum(year_spend.jan_spend, year_spend.feb_spend, year_spend.mar_spend, year_spend.apr_spend, year_spend.may_spend, year_spend.june_spend, year_spend.july_spend, year_spend.aug_spend, year_spend.sept_spend, year_spend.oct_spend, year_spend.nov_spend, year_spend.dec_spend)
        self.YearlyBudgetDAO.edit_yearly_budget(username, year, total_year_spend)
        # update the yearlySpend table with the total yearly spend by aggregating all of the monthly spend totals

class RewardPointsService:
    def __init__(self):
        self.UserMaxCreditCardMultDAO = UserMaxCreditCardMultDAO()
        self.UserMaxCreditCardMult = UserMaxCreditCardMult()
        self.UserDAO = UserDAO()
        self.User = User()
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()
        self.MonthlyBudget = MonthlyBudget()
        self.RewardPointsDAO = RewardPointsDAO()
        self.RewardPoints = RewardPoints()

    def calc_reward_points_monthly(self, username, month, year):
        users_multipliers = UserMaxCreditCardMultDAO.get_max_multipliers(username)
        month_spend = MonthlyBudgetDAO.get_monthly_budget(username, month, year)

        restaraunt_points = users_multipliers.restaurant_mult*month_spend.restaurant_spend
        grocery_points = users_multipliers.grocery_mult*month_spend.grocery_spend
        non_category_points = users_multipliers.non_cat_mult*month_spend.non_cat_spend
        utility_points = users_multipliers.utility_mult*month_spend.utility_spend
        gas_points =users_multipliers.gas_mult*month_spend.gas_spend
        total_monthly_points = sum(restaraunt_points, grocery_points, non_category_points, utility_points, gas_points)

        self.RewardPointsDAO.update_monthly_reward_points(username, month, year, total_monthly_points) 
        # This pulls the max multipliers from the user table and spend from the budgets table
        # The algo then multiplies each category by the respective multiplier, which then updates the rewards point table 

    def calc_reward_points_yearly(self,username, year): #WIP THIS NEEDS TO BE UPDATED AND EVERYTHING BELOW THIS
        list_monthly_points = self.RewardPointsDAO.get_all_monthly_reward_points(username, year)
        total_year_points = sum(list_monthly_points)
        self.RewardPointsDAO.update_total_year_points(username, year, total_year_points)

class FMVRewardsPointsService:
    def __init__(self):
        self.RewardPointsDAO = RewardPointsDAO()
        self.RewardPoints = RewardPoints()
        self.RewardPointsEVDAO = RewardPointsEVDAO()
        self.RewardPointsEV = RewardPointsEV()

    def calc_rewards_exp_value(self, username, year):
        reward_points_data = self.RewardPointsDAO.join_reward_expected_value(username, year)
        reward_points_EV = reward_points_data[2]*reward_points_data[3]
        self.RewardPointsDAO.update_reward_points_FMV(username, year, reward_points_EV)
        # this function will take the total rewards collected and multiply it by its "FMV"
        # will need to join user's points table and multiply it by the EV of the points to get this value