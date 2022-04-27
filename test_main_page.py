from .pages.main_page import MainPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
   

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу - это у нас задано в base_page
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина - это у нас задано в main_page
