from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "accounts/login/" in self.browser.current_url, "We are not on the login page"

    def should_be_login_form(self):
        login_username = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_submit_btn = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN)
        assert login_username and login_pass and login_submit_btn, "There is no Login form" 

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        reg_username = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_confirm_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASS)
        reg_submit_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN)
        assert reg_username and reg_pass and reg_confirm_pass and reg_submit_btn, "There is no Registration form"

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        user_email.send_keys(email)
        user_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        user_pass.send_keys(password)
        user_pass_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASS)
        user_pass_confirm.send_keys(password)
        confirm_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN)
        confirm_button.click()

