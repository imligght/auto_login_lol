# a function to open the client
def open_client():
    pyag.press("win") # open the windows search
    pyag.write("league of legends") # search for league of legends
    pyag.press("enter") # open the select program, league of legends in this case
    time.sleep(7) # wait a little bit until the client is open
    login() # call the login function to initializate the login process

# a function to login in your account
def login():
    pyag.write(Interface.username) # your login username here
    pyag.press("tab") # tab to pass to the next field, the password field in this case
    pyag.write(Interface.password) # write your password
    pyag.press("enter") # enter to login
    
def take_verification_code():
    pyag.press("win")
    pyag.write("brave")
    pyag.press("enter")
    time.sleep(5)
    pyag.write("gmail.com")
    pyag.press("enter")
    time.sleep(5)
    pyag.click(x=615, y=281)
    time.sleep(2)
    pyag.click(x=1058, y=742, clicks=2)
    pyag.hotkey("ctrl", 'c')
    pyag.hotkey("alt", "tab")
    pyag.hotkey("ctrl", 'v')
    pyag.press("enter")