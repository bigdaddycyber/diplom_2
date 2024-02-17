import allure
import pytest
from generate_data import *
from data_fake import *

class TestLoginUser:
    
    @allure.title('Проверка существующего пользователя')
    def test_login_existing_user(self):
        email, password = generate_data_new_user()
        payload = {
            'email': email,
            'password': password
        }
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', data=payload)
        assert responce.status_code == 200 
    
    @allure.title('Создание пользователя с некорректным email')    
    def test_login_user_incorrect_login(self):
        password = generate_data_new_user()
        payload = {
            'email': Data.NOCORRECT_EMAIL,
            'password': password
        }
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', data=payload)
        assert responce.status_code == 401