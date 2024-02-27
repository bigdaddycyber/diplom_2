import allure
from generate_data import *
from data import *
from faker import Faker

fake = Faker()

class TestChangeDataUser:
    
    @allure.title('Изменение почты у зарегистрированнного пользователя')
    def test_change_email_for_registry_user(self, create_new_user):
        change_email = fake.email()
        payload_change = {
            'email': change_email
        }
        response = requests.patch((Url.site + Api.user), data=payload_change)
        assert 200 == response.status_code and response.json()["success"] == True
        
    
    @allure.title('Изменения почты у незарегистрированного пользователя')    
    def test_cchange_email_for_no_registry_user(self):
        change_email = fake.email()
        change_user = fake.first_name()
        payload = {
            'email': change_email,
            'name': change_user
        }
        response = requests.patch((Url.site + Api.user), headers={"Autorisation": ""}, data=payload)
        assert 401 == response.status_code and response.json()['success'] == False
        