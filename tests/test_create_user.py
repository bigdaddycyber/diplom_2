import allure
import requests
from generate_data import *
from data import *
from faker import Faker

fake = Faker()

class TestCreateUser:
    
    @allure.title('Создание нового пользователя')
    def test_create_user_sicessfull(self, create_new_user):    
        assert 200 == create_new_user.status_code and create_new_user.json()["success"] == True
        
        
    @allure.title('Создание пользователя с существующей почтой')    
    def test_create_two_same_user_error(self):
        email = 'testtestcucaracha@gmail.com'
        password = 'testest123'
        name = 'Cucaracha'
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        response2 = requests.post((Url.site + Api.register), data=payload)
        assert 403 == response2.status_code
        assert response2.json()["message"] == 'User already exists'
    
    @allure.title('Создание пользователя без имени')    
    def test_create_user_with_empty_field(self):
        email = fake.email()
        name = fake.first_name()
        payload = {
            'email': email,
            'name': name
        }
        response = requests.post((Url.site + Api.register), data=payload)
        assert 403 == response.status_code and response.json()['message'] == 'Email, password and name are required fields'