import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from model.user_info_form import UserInfoForm, UserInfoFormDAO
from model.user_credit_card_form import UserCreditCardForm, UserCreditCardFormDAO
from model.user_budget_form import UserBudgetForm, UserBudgetFormDAO
from model.monthly_budget_model import MonthlyBudget, MonthlyBudgetDAO
from model.yearly_budget_model import YearlyBudget, YearlyBudgetDAO
from controller.runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/userInfo', methods=['POST', 'GET'])
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

    user_budget = UserBudgetFormDAO()
    user_budget.add_user_budget_form(data)
    return "User Budget JSON Posted"


@app.route('/yearlyCategorySpend', methods=['GET', 'REQUEST'])
def get_yearly_category_user_spend():
    # will have to SELECT form data from userBudgetForm and then INSERT INTO monthlyBudget
    username = "Matt"
    year = 2020
    data = UserBudgetFormDAO()
    json_data = data.get_user_budget_form(username, year)
    total_month_spend = MonthlyBudgetService()
    ytd_budget_spend = YearlyBudgetService()
    year_cat_spend = YearlyBudgetDAO()

    # this will add the form budget data table to the monthly budget table
    user_budget_data = MonthlyBudgetDAO()
    for key in json_data.keys():
        budget = [
            json_data[key].username,
            json_data[key].month,
            json_data[key].year,
            json_data[key].restaurant_spend,
            json_data[key].grocery_spend,
            json_data[key].non_category_spend,
            json_data[key].utility_spend,
            json_data[key].gas_spend,
            0
        ]
        user_budget_data.add_monthly_budget(budget)

        # The function will total each month's spend and then edit the table to include the total month's spend
        total_month_spend.calculate_total_monthly_budget(username, key, year)

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
        print(year_spend_data)
        # Add get request logic here
        return year_spend_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
