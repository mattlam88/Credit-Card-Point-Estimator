from flask import Flask

from .runner import MonthlyBudgetService, YearlyBudgetService, RewardPointsService, FMVRewardsPointsService


class Controller:
    def __init__(self):
        pass

    @app.route('/')
    def start():
        #will start the program once the website is up and running and return some JSON information
        pass

app = Flask(__name__)

if __name__ == '__main__':
    Controller.start()