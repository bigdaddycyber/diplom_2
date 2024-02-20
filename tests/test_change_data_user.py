import allure
from generate_data import *

class TestChangeDataUser:
    
    @allure.title('Изменение почты у зарегистрированнного пользователя')
    def test_change_email_for_registry_user(self):
        token, email, user, password = create_new_user()
        change_email = email + 'test'
        payload = {
            'email': change_email
        }
        response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', headers={'Autorisation': token}, data=payload)
        assert 200 == response.status_code and response.json()["success"] == True
        generate_data_new_user.delete_user(token)
        
    
    @allure.title('Изменения почты у незарегистрированного пользователя')    
    def test_cchange_email_for_no_registry_user(self):
        token, email, user, password = create_new_user()
        change_email = email + 'test'
        change_password = password + 'test'
        change_user = user + 'test'
        payload = {
            'email': change_email,
            'name': change_user,
            'password': change_password
        }
        response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', headers={"Autorisation": ""}, data=payload)
        assert 403 == response.status_code and response.json() == {
                                                                   "success": False,
                                                                   "message": "User with such email already exists"
                                                                   }
        generate_data_new_user.delete_user(token) 
        