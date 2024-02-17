import allure
from generate_data import *

class TestChangeDataUser:
    
    @allure.tittle('Изменение почты у зарегистрированнного пользователя')
    def test_change_email_for_registry_user(self):
        email, password, user, token = create_new_user()
        change_email = email + 'test'
        payload = {
            'email': change_email
        }
        responce = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', headers={'Autorisation': token}, data=payload)
        assert responce.status_code == 200
    
    @allure.tittle('Изменения почты у незарегистрированного пользователя')    
    def test_cchange_email_for_no_registry_user(self):
        email, password, user, token = create_new_user()
        change_email = email + 'test'
        change_password = password + 'test'
        change_user = user + 'test'
        payload = {
            'email': change_email,
            'name': change_user,
            'password': change_password
        }
        response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/use', headers={"Autorisation": ""}, data=payload)
        assert response.status_code == 403
        
        