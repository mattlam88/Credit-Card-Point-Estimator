from flask import Flask, request, jsonify
from controller.runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService
import time

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/getPieChartData', methods=['POST'])
def getPIECHART():
    data = request.json
    x = jsonify(data)