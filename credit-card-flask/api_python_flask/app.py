import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from model.user_info_form import UserInfoForm, UserInfoFormDAO
from model.user_credit_card_form import UserCreditCardForm, UserCreditCardFormDAO
from controller.runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST', 'GET'])
# def retrive_user_info():
#     print (request.is_json)
#     req_data = request.get_json()
#     print (req_data)

    # username = req_data['username']
    # first_name = req_data['firstName']
    # last_name = req_data['lastName']
    # data = [username, first_name, last_name]
    
    # user_info_DAO = UserInfoFormDAO()
    # user_info_DAO.add_user_info_form(data)
    # return "User Info JSON Posted"

def retrive_user_credit_cards():
    print (request.is_json)
    req_cc_data = request.get_json("SubmitUserCC")
    print (req_cc_data)

    username = req_cc_data['username']
    credit_card_issuer = req_cc_data['creditCardIssuer']
    credit_card_type = req_cc_data['creditCardType']
    credit_card_reward_points = req_cc_data['creditCardRewardPoints']
    restaurant_multiplier = req_cc_data['restaurantMultiplier']
    grocery_multiplier = req_cc_data['groceryMultiplier']
    non_category_multiplier = req_cc_data['nonCategoryMultiplier']
    utility_multiplier = req_cc_data['utilityMultiplier']
    gas_multiplier = req_cc_data['gasMultiplier']
    data = [username,credit_card_issuer,credit_card_type,credit_card_reward_points,restaurant_multiplier,grocery_multiplier,non_category_multiplier,utility_multiplier,gas_multiplier]

    user_credit_card = UserCreditCardFormDAO()
    user_credit_card.add_user_credit_card_form(data)
    return "User Credit Card JSON Posted"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)