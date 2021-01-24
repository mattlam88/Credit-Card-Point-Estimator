import sqlite3

from model.monthly_budget_model import MonthlyBudgetDAO, MonthlyBudget
from model.yearly_budget_model import YearlyBudgetDAO, YearlyBudget
from model.credit_card_model import CreditCardDAO, CreditCard
from model.reward_points_model import RewardPointsDAO, RewardPoints
from model.user_model import UserDAO, User
from model.user_max_multipliers import UserMaxCreditCardMult, UserMaxCreditCardMultDAO
from model.reward_points_expected_value_model import RewardPointsEVDAO, RewardPointsEV

class MonthlyBudgetService:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()

    def calculate_total_monthly_budget(self, username, month, year):
        monthly_spend = MonthlyBudgetDAO()
        month_budget = monthly_spend.get_monthly_budget(username, month, year)
        total_month_spend = (
            month_budget.restaurant_spend +
            month_budget.grocery_spend +
            month_budget.non_cat_spend +
            month_budget.utility_spend +
            month_budget.gas_spend
        )
        monthly_budget_DAO = MonthlyBudgetDAO()
        monthly_budget_DAO.edit_monthly_total_spend(username, month, year, total_month_spend)
        # this will sum up each month by adding up each category spend

class YearlyBudgetService:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()
        self.YearlyBudgetDAO = YearlyBudgetDAO()

    def calc_total_yearly_category_spend(self, username, year):
        total_yearly_category_spend = MonthlyBudgetDAO.get_total_monthly_category_spend(username, year)
        self.YearlyBudgetDAO.add_yearly_budget(total_yearly_category_spend)

    def calc_total_yearly_spend(self, username, year):
        year_spend = MonthlyBudgetDAO.get_all_monthly_user_spend(username, year)
        total_year_spend = sum(
            year_spend.jan_spend, 
            year_spend.feb_spend, 
            year_spend.mar_spend, 
            year_spend.apr_spend, 
            year_spend.may_spend, 
            year_spend.june_spend, 
            year_spend.july_spend, 
            year_spend.aug_spend, 
            year_spend.sept_spend, 
            year_spend.oct_spend, 
            year_spend.nov_spend, 
            year_spend.dec_spend
        )
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

    def calc_reward_points_yearly(self,username, year):
        year_total_monthly_points = self.RewardPointsDAO.get_all_monthly_reward_points(username, year)
        total_year_points = sum(
            year_total_monthly_points.jan_points,
            year_total_monthly_points.feb_points,
            year_total_monthly_points.mar_points,
            year_total_monthly_points.apr_points,
            year_total_monthly_points.may_points,
            year_total_monthly_points.june_points,
            year_total_monthly_points.july_points,
            year_total_monthly_points.aug_points,
            year_total_monthly_points.sept_points,
            year_total_monthly_points.oct_points,
            year_total_monthly_points.nov_points,
            year_total_monthly_points.dec_points
        )
        self.RewardPointsDAO.update_total_year_points(username, year, total_year_points)

class FMVRewardsPointsService:
    def __init__(self):
        self.RewardPointsDAO = RewardPointsDAO()
        self.RewardPoints = RewardPoints()
        self.RewardPointsEVDAO = RewardPointsEVDAO()
        self.RewardPointsEV = RewardPointsEV()

    def calc_rewards_exp_value(self, username, year):
        reward_points_data = self.RewardPointsDAO.join_reward_expected_value(username, year)
        reward_points_EV = reward_points_data.total_year_points*reward_points_data.expected_point_value
        self.RewardPointsDAO.update_reward_points_FMV(username, year, reward_points_EV)
        # this function will take the total rewards collected and multiply it by its "FMV"
        # will need to join user's points table and multiply it by the EV of the points to get this value