import allure
import requests
from generate_data import *
from generate_data import generate_data_new_user, generate_random_string
from data import *

class TestCreateUser:
    
    @allure.title('Создание нового пользователя')
    def test_create_user_sicessfull(self, delete_user):
        token, email, user, password = generate_data_new_user()
        payload = {
            'email': email,
            'password': password,
            'name': user
        }
        
        response = requests.post((Url.site + Api.register), data=payload)
        token = response.json()["accessToken"]
        assert 200 == response.status_code and response.json()["success"] == True
        
        
    
    @allure.title('Создание пользователя с существующей почтой')    
    def test_create_two_same_user_error(self, delete_user):
        email, user, password = generate_data_new_user()
        payload = {
            'email': email,
            'password': password,
            'name': user 
        }
        
        response1 = requests.post((Url.site + Api.register), data=payload)
        response2 = requests.post((Url.site + Api.register), data=payload)
        assert 403 == response2.status_code and response2["message"] == 'User already exists'
    
    @allure.title('Создание пользователя без имени')    
    def test_create_user_with_empty_field(self):
        email, password = generate_data_new_user()
        payload = {
            'email': email,
            'password': password
        }
        response = requests.post((Url.site + Api.register), data=payload)
        assert 400 == response.status_code and response['message'] == 'Недостаточно данных для создания учетной записи'