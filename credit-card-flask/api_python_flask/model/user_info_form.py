import sqlite3

class UserInfoFormDAO:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/mattlam/Documents/Coding Bootcamp/Final-Project-Individual-Matt/creditCard.db')
        self.cur = self.conn.cursor()
    
    def add_user_info_form(self, data):
        self.cur.execute(f"INSERT INTO userInfoForm (username, firstName, lastName) VALUES (?,?,?);", data)
        self.conn.commit()

    def get_user_info_form(self, username):
        user_info = self.cur.execute(f"SELECT username, firstName, lastName FROM userInfoForm WHERE username={username};")
        self.conn.commit()
        for info in user_info:
            user = UserInfoForm(info[0], info[1], info[2])
        return user
        

class UserInfoForm:
    def __init__(self, id=0, username=None, first_name=None, last_name=None):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
