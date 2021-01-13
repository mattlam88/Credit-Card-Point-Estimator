from flask import Flask, request, jsonify
from controller.runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService
import time

app = Flask(__name__)


@app.route('/getPieChartData', methods=['POST'])
def getPIECHART():
    data = request.json
