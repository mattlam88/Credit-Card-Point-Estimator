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
        self.YearlyBudgetDAO = YearlyBudgetDAO()

    def calculate_category_monthly_budget(self, id, username, month):
        monthly_spend = MonthlyBudgetDAO.get_monthly_budget(id,username,month)
        total_month_spend = monthly_spend[4]+monthly_spend[5]+monthly_spend[6]+monthly_spend[7]+monthly_spend[8]
        data = [id, username, month, total_month_spend]
        self.YearlyBudgetDAO.add_yearly_budget(data)
        # this will sum up each month by adding up each category spend


class YearlyBudgetServce:
    def __init__(self):
        self.YearlyBudgetDAO = YearlyBudgetDAO()

    def calc_total_yearly_spend(self, username, year):
        yearly_spend = YearlyBudgetDAO.get_yearly_budget(username, year)
        total_yearly_spend = yearly_spend[2] + yearly_spend[3] + yearly_spend[4] + yearly_spend[5] + yearly_spend[6] + yearly_spend[7] + yearly_spend[8] + yearly_spend[9] + yearly_spend[10] + yearly_spend[11] + yearly_spend[12] + yearly_spend[13]
        self.YearlyBudgetDAO.edit_yearly_budget(username, year, total_yearly_spend)
        # this function will sum up

class RewardPointsService:
    def __init__(self):
        self.YearlyBudgetDAO = YearlyBudgetDAO()
        self.CreditCardDAO = CreditCardDAO()

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


        

