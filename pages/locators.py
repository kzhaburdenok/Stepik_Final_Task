from selenium.webdriver.common.by import By

# каждый селектор — это пара: как искать и что искать

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_SUBMIT_BTN = (By.NAME, "login_submit")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD = (By.NAME, "registration-password1")
    REGISTRATION_CONFIRM_PASS = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT_BTN = (By.NAME, "registration_submit")    

