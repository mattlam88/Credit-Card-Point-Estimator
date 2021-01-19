import sqlite3

class UserCreditCardFormDAO:
    def __init__(self):
        self.conn = sqlite3.connect("creditCard.db")
        self.cur = self.conn.cursor()

    def add_user_credit_card_form(self, data):
        self.cur.execute()
        self.conn.commit()

    def get_user_credit_card_form(self, username):
        user_credit_card_info = self.cur.execute()
        for info in user_credit_card_info:
            user_credit_card = UserCreditCardForm()
        return user_credit_card


class UserCreditCardForm:
    def __init__(self, id=0, username=None, credit_card_issuer=None,
                 credit_card_type=None, credit_card_reward_points=None,
                 restaurant_multiplier=1, grocery_multiplier=1, non_category_multiplier=1,
                 utility_multiplier=1, gas_multiplier=1):
        self.id = id
        self.username = username
        self.credit_card_issuer = credit_card_issuer
        self.credit_card_type = credit_card_type
        self.credit_card_reward_points = credit_card_reward_points
        self.restaurant_multiplier = restaurant_multiplier
        self.grocery_multiplier = grocery_multiplier
        self.non_category_multiplier = non_category_multiplier
        self.utility_multiplier = utility_multiplier
        self.gas_multiplier = gas_multiplier
