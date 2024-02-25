import allure
import pytest
from generate_data import *
from data_fake import *
from data import *

class TestLoginUser:
    
    @allure.title('Проверка существующего пользователя')
    def test_login_existing_user(self, delete_user):
        email, password = generate_data_new_user()
        payload = {
            'email': email,
            'password': password
        }
        response = requests.post((Url.site + Api.login), data=payload)
        token = response.json()["accessToken"]
        assert 200 == response.status_code and response.json()["success"] == True 
    
    
    @allure.title('Создание пользователя с некорректным email')    
    def test_login_user_incorrect_login(self):
        password, token = generate_data_new_user()
        payload = {
            'email': Data.NOCORRECT_EMAIL,
            'password': password
        }
        response = requests.post((Url.site + Api.login), data=payload)
        assert 401 == response.status_code and response.json() == {
                                                                   "success": False,
                                                                   "message": "email or password are incorrect"
                                                                   }