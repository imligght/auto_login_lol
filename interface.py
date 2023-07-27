import pyautogui as pyag
import time
import json
import os

class Interface:

    def __init__(self):
        self.accounts = {}
        self.user_browser = ''
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json", 'r') as user_data_file:
                self.accounts = json.load(user_data_file)
        else:
            self.save_accounts()

    def save_accounts(self):
        with open("user_data.json", 'w') as user_data_file:
            json.dump(self.accounts, user_data_file)

    def add_account(self, account_name, username, password, two_factor_auth, user_browser):
        self.accounts[account_name] = {
            "username": username,
            "password": password,
            "two_factor_auth": two_factor_auth == 'y',    
            "user_browser": user_browser
        }
        self.save_accounts()

    def remove_account(self, account_name):
        if account_name in self.accounts:
            del self.accounts[account_name]
            self.save_accounts()

    def choose_account(self):
        print("Stored Accounts:")
        for account_name in self.accounts:
            print(account_name)

        while True:
            chosen_account = input("Choose an account to log in to (or 'new' to add a new account): ")
            if chosen_account == "new":
                self.add_new_account()

            elif chosen_account  in self.accounts:
                return chosen_account

            else:
                print("Invalid account name. Please choose a valid account or type 'new' to add a new account.")
    
    def add_new_account(self):
        account_name = input("Enter a name for the new account (e.g. 'main', 'smurf1', etc): ")
        username = input("Insert the username: ")
        password = input("Insert the password: ")
        two_factor_auth = input("Does this account use two factor authentication? (y/n): ").lower()

        if two_factor_auth == 'y':
            self.user_browser = input("Which web browser do you use? ")


        self.add_account(account_name, username, password, two_factor_auth, self.user_browser)

    # a function to open the client
    def open_client(self):
        pyag.press("win") # open the windows search
        pyag.write("league of legends") # search for league of legends
        pyag.press("enter") # open the select program, league of legends in this case
        time.sleep(7) # wait a little bit until the client is open

    # a function to login in your account
    def login(self, username, password):
        pyag.write(username) # your login username here
        pyag.press("tab") # tab to pass to the next field, the password field in this case
        pyag.write(password) # write your password
        pyag.press("enter") # enter to login

    # function to take the 2fa and copy and paste automaticaly in the client
    def take_and_apply_verification_code(self, user_browser):
        pyag.press("win") # open the windows search
        pyag.write(user_browser) # search the browser of the user
        pyag.press("enter") # open the browser
        time.sleep(5) # wait for a couple seconds until the web browser is open
        pyag.write("gmail.com") # write "gmail.com" in the search field
        pyag.press("enter") # go to gmail.com
        time.sleep(5) # wait a couple seconds until the site is open
        pyag.press("down") # press the down arrow key to select the last email you received
        pyag.press("apps") # press the "apps" key which open the menu of options
        pyag.press("up") # press the up arrow key to select the last option, which open the email in an another window
        pyag.press("enter") # open it
        time.sleep(3) # wait 3s to make sure the window has already opened
        pyag.click(x=991, y=797, clicks=2) # double click in the code to select it
        pyag.hotkey("ctrl", 'c') # copy the code
        pyag.hotkey("alt", "f4") # close the code email window
        pyag.hotkey("alt", "f4") # close the gmail.com window
        pyag.hotkey("ctrl", "v") # paste the code in the client
        pyag.press("enter") # enter the client

    # function to intitiate the program
    def run(self):
        chosen_account = self.choose_account()
        account_info = self.accounts[chosen_account]

        self.open_client()
        self.login(account_info["username"], account_info["password"])

        if account_info["two_factor_auth"]:
            self.take_and_apply_verification_code(account_info["user_browser"])