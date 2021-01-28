import sqlite3

from model.monthly_budget_model import MonthlyBudgetDAO, MonthlyBudget
from model.yearly_budget_model import YearlyBudgetDAO, YearlyBudget
from model.credit_card_model import CreditCardDAO, CreditCard
from model.reward_points_model import RewardPointsDAO, RewardPoints
from model.user_model import UserDAO, User
from model.user_max_multipliers import UserMaxCreditCardMult, UserMaxCreditCardMultDAO
from model.reward_points_expected_value_model import RewardPointsEVDAO, RewardPointsEV

class SaveDB:
    def __init__(self):
        self.conn = sqlite3.connect("/Users/mattlam/Documents/Coding Bootcamp/Final-Project-Individual-Matt/creditCard.db")
        self.cur = self.conn.cursor()
    def save_db(self):
        self.conn.commit()

class MonthlyBudgetService:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()

    def calculate_total_monthly_budget(self, username, month, year):
        monthly_spend = self.MonthlyBudgetDAO
        month_budget = monthly_spend.get_monthly_budget(username, month, year)
        month_total_spend = (
            month_budget.restaurant_spend +
            month_budget.grocery_spend +
            month_budget.non_cat_spend +
            month_budget.utility_spend +
            month_budget.gas_spend
        )
        print(month_total_spend)
        monthly_spend.edit_monthly_total_spend(username, month, year, month_total_spend)
        # this will sum up each month by adding up each category spend

class YearlyBudgetService:
    def __init__(self):
        self.MonthlyBudgetDAO = MonthlyBudgetDAO()
        self.YearlyBudgetDAO = YearlyBudgetDAO()

    def calc_total_yearly_category_spend(self, username, year):
        total_yearly_category_spend = self.MonthlyBudgetDAO
        budget_data = total_yearly_category_spend.get_total_monthly_category_spend(username, year)
        
        data = [
            budget_data.username, 
            budget_data.year,
            budget_data.yearly_restaurant_spend,
            budget_data.yearly_grocery_spend,
            budget_data.yearly_non_cat_spend,
            budget_data.yearly_utility_spend,
            budget_data.yearly_gas_spend            
        ]

        yearly_budget = self.YearlyBudgetDAO
        yearly_budget.add_yearly_budget(data)

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
        self.RewardPointsDAO = RewardPointsDAO()
        self.RewardPoints = RewardPoints()

    def calc_reward_points_monthly(self, username, month, year):
        users_multipliers = self.UserMaxCreditCardMultDAO
        multipliers = users_multipliers.get_max_multipliers(username)

        month_spend = self.MonthlyBudgetDAO
        month_spend_data = month_spend.get_monthly_budget(username, month, year)

        restaraunt_points = multipliers.restaurant_mult*month_spend_data.restaurant_spend
        grocery_points = multipliers.grocery_mult*month_spend_data.grocery_spend
        non_category_points = multipliers.non_cat_mult*month_spend_data.non_cat_spend
        utility_points = multipliers.utility_mult*month_spend_data.utility_spend
        gas_points = multipliers.gas_mult*month_spend_data.gas_spend
        total_monthly_points = (restaraunt_points + grocery_points + non_category_points + utility_points + gas_points)

        rewards = self.RewardPointsDAO
        rewards.update_monthly_reward_points(username, month, year, total_monthly_points) 
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