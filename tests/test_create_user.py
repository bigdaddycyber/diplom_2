import allure
import requests
from generate_data import *
from generate_data import generate_data_new_user, generate_random_string

class TestCreateUser:
    
    @allure.title('Создание нового пользователя')
    def test_create_user_sicessfull(self):
        email, password, user = generate_data_new_user()
        payload = {
            'email': email,
            'password': password,
            'name': user
        }
        
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        assert 500 == response.status_code
    
    @allure.title('Создание пользователя с существующей почтой')    
    def test_create_two_same_user_error(self):
        email, password, user = generate_data_new_user()
        payload = {
            'email': email,
            'password': password,
            'name': user 
        }
        
        response1 = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        response2 = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        assert 500 == response2.status_code 
        #and response2["message"] == 'User already exists'
    
    @allure.title('Создание пользователя без имени')    
    def test_create_user_with_empty_field(self):
        email, password = generate_data_new_user()
        payload = {
            'email': email,
            'password': password
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        assert 400 == response.status_code and response['message'] == 'Недостаточно данных для создания учетной записи'