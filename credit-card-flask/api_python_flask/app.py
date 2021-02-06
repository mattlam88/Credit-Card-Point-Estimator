import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from model.user_info_form import UserInfoForm, UserInfoFormDAO
from model.user_credit_card_form import UserCreditCardForm, UserCreditCardFormDAO
from model.credit_card_model import CreditCard, CreditCardDAO
from model.user_max_multipliers import UserMaxCreditCardMult, UserMaxCreditCardMultDAO
from model.reward_points_model import RewardPoints, RewardPointsDAO
from model.user_budget_form import UserBudgetForm, UserBudgetFormDAO
from model.monthly_budget_model import MonthlyBudget, MonthlyBudgetDAO
from model.yearly_budget_model import YearlyBudget, YearlyBudgetDAO
from controller.runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService
import jsons

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/userInfo/<username>', methods=['POST', 'GET'])
def retrieve_user_info():
    print(request.is_json)
    req_data = request.get_json()
    print(req_data)

    username = req_data['username']
    first_name = req_data['firstName']
    last_name = req_data['lastName']
    data = [username, first_name, last_name]

    user_info_DAO = UserInfoFormDAO()
    user_info_DAO.add_user_info_form(data)
    return "User info JSON Posted"


@app.route('/userCreditCard', methods=['POST', 'GET'])
def retrive_user_credit_cards():
    print(request.is_json)
    req_cc_data = request.get_json()
    print(req_cc_data)

    username = req_cc_data['username']
    credit_card_issuer = req_cc_data['creditCardIssuer']
    credit_card_type = req_cc_data['creditCardType']
    credit_card_reward_points = req_cc_data['creditCardRewardPoints']
    restaurant_multiplier = req_cc_data['restaurantMultiplier']
    grocery_multiplier = req_cc_data['groceryMultiplier']
    non_category_multiplier = req_cc_data['nonCategoryMultiplier']
    utility_multiplier = req_cc_data['utilityMultiplier']
    gas_multiplier = req_cc_data['gasMultiplier']
    data = [username, credit_card_issuer, credit_card_type, credit_card_reward_points,
            restaurant_multiplier, grocery_multiplier, non_category_multiplier, utility_multiplier, gas_multiplier]

    user_credit_card = UserCreditCardFormDAO()
    user_credit_card.add_user_credit_card_form(data)
    return "User Credit Card JSON Posted"


@app.route('/userBudget', methods=['POST', 'GET'])
def retrive_user_budget():
    print(request.is_json)
    req_data = request.get_json()
    print(req_data)

    username = req_data['username']
    month = req_data['month']
    year = req_data['year']
    restaurant_spend = req_data['restaurantSpend']
    grocery_spend = req_data['grocerySpend']
    non_category_spend = req_data['nonCategorySpend']
    utility_spend = req_data['utilitySpend']
    gas_spend = req_data['gasSpend']
    data = [username, month, year, restaurant_spend, grocery_spend,
            non_category_spend, utility_spend, gas_spend]

    monthly_data = [username, month, year, restaurant_spend, grocery_spend,
                    non_category_spend, utility_spend, gas_spend, 0]

    user_budget = UserBudgetFormDAO()
    user_budget.add_user_budget_form(data)

    month_budget = MonthlyBudgetDAO()
    month_budget.add_monthly_budget(monthly_data)

    monthly_budget_service = MonthlyBudgetService()
    monthly_budget_service.calculate_total_monthly_budget(
        username, month, year)

    # Will need to add the monthly functions here so it won't keep running 12 times in the yearlyCategorySpend function
    # or I can split up the code where it would post into the database and return the json
    return "User Budget JSON Posted"


@app.route('/yearlyCategorySpend/<username>', methods=['GET', 'REQUEST'])
def get_yearly_category_user_spend(username):
    # will have to SELECT form data from userBudgetForm and then INSERT INTO monthlyBudget
    year = 2020
    ytd_budget_spend = YearlyBudgetService()
    year_cat_spend = YearlyBudgetDAO()

    # This will add up all the category spend from the monthly budget table and then add into yearly data table
    ytd_budget_spend.calc_total_yearly_category_spend(username, year)

    # This will retrieve data from yearly budget table and return a instance of YearlyBudget
    year_spend = year_cat_spend.get_yearly_budget(username, year)

    year_spend_data = {
        'restaurant_spend': year_spend.restaurant_spend_yearly,
        'grocery_spend': year_spend.grocery_spend_yearly,
        'non_category_spend': year_spend.non_category_spend_yearly,
        'utility_spend': year_spend.utility_spend_yearly,
        'gas_spend': year_spend.gas_spend_yearly
    }
    # Add get request logic here
    return year_spend_data


@app.route('/combinedSpendAndPoints/<username>', methods=['GET'])
def send_spend_points(username):
    json_data = {}
    year = 2020

    total_month_spend = MonthlyBudgetDAO()
    user_spend = total_month_spend.get_all_monthly_user_spend(username, year)
    json_data['user_spend'] = user_spend

    reward_response = get_credit_card_points(username)
    json_data['user_points'] = reward_response

    return jsons.dump(json_data)


@app.route('/monthlySpendAndPoints/<username>', methods=['GET', 'REQUEST'])
def get_user_monthly_spend(username):
    year = 2020

    total_month_spend = MonthlyBudgetDAO()
    user_spend = total_month_spend.get_all_monthly_user_spend(username, year)
    json_data = jsons.dump(user_spend)

    return json_data


def get_credit_card_points(username):
    # First, I need to get the credit data from the userCreditCardForm Table and send to the creditCardDetails Table
    year = 2020
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    user_credit_card_form = UserCreditCardFormDAO()
    user_cc_data = user_credit_card_form.get_user_credit_card_form(username)
    data = [
        user_cc_data.username,
        user_cc_data.credit_card_issuer,
        user_cc_data.credit_card_type,
        user_cc_data.credit_card_reward_points,
        user_cc_data.restaurant_multiplier,
        user_cc_data.grocery_multiplier,
        user_cc_data.non_category_multiplier,
        user_cc_data.utility_multiplier,
        user_cc_data.gas_multiplier
    ]

    cc_detail_DAO = CreditCardDAO()
    cc_detail_DAO.add_credit_card(data)

    # Second, once the information is in the creditCardDetails table, run the runner.py calc_rewards_points_monthly
    user_reward_points = RewardPointsDAO()

    rewards_calculator = RewardPointsService()
    monthly_reward_points = []
    for month in months:
        monthly_reward_points.append(
            rewards_calculator.calc_reward_points_monthly(username, month, year))

    print(monthly_reward_points)
    rewards_data = [username, year, 'Chase UR', monthly_reward_points[0], monthly_reward_points[1], monthly_reward_points[2], monthly_reward_points[3],
                    monthly_reward_points[4], monthly_reward_points[5], monthly_reward_points[6],
                    monthly_reward_points[7], monthly_reward_points[8], monthly_reward_points[9],
                    monthly_reward_points[10], monthly_reward_points[11]]

    user_reward_points.insert_new_user_reward_points(rewards_data)

    reward_points_data = user_reward_points.get_all_monthly_reward_points(username, year)
    reward_json = {
        "January": reward_points_data.jan_points,
        "February": reward_points_data.feb_points,
        "March": reward_points_data.mar_points,
        "April": reward_points_data.apr_points,
        "May": reward_points_data.may_points,
        "June": reward_points_data.jun_points,
        "July": reward_points_data.jul_points,
        "August": reward_points_data.aug_points,
        "September": reward_points_data.sep_points,
        "October": reward_points_data.oct_points,
        "November": reward_points_data.nov_points,
        "December": reward_points_data.dec_points
    }
    return reward_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
