from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from controller.runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService
import time

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.get_json():
        return 'JSON post succeeded'
    return 'Failed'
    