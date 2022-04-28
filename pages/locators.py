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

class ProductPageLocators():
    PPODUCT_NAME = (By.XPATH, "//div[contains(@class,'product_main')]/child::h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product_main')]/child::p[@class='price_color']")
    PRODUCT_ADD_TO_CART_BTN = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    PRODUCT_ADDED_TO_CART_ALLERT = (By.XPATH, "//div[contains(@class,'alertinner')]/child::strong")
    BASKET_TOTAL_PRICE = (By.XPATH, "//div[contains(@class,'alertinner')]/child::p/strong")

