import allure
import pytest
from generate_data import *
from data_fake import *
from data import *

class TestLoginUser:
    
    @allure.title('Проверка существующего пользователя')
    def test_login_existing_user(self, login_user):
        assert 200 == login_user.status_code and login_user.json()["success"] == True 
    
    
    @allure.title('Создание пользователя с некорректным email')    
    def test_login_user_incorrect_login(self, create_new_user):
        email = Data.NOCORRECT_EMAIL
        password = 'testest123'
        name = 'Cucaracha'
        payload = {
            "email": email,
            "password": password,
            "name" : name
        }
        response = requests.post((Url.site + Api.login), data=payload)
        assert 401 == response.status_code and response.json() == {
                                                                   "success": False,
                                                                   "message": "email or password are incorrect"
                                                                   }