from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
   

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу - это у нас задано в base_page
    page.should_be_login_link()
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина - это у нас задано в main_page
    login_page = LoginPage(browser,link)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
