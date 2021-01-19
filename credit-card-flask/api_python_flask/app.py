from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from controller.runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService
import time

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return "JSON Posted"

app.run(host='0.0.0.0', port= 5000)