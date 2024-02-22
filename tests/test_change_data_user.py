import allure
from generate_data import *
from data import *


class TestChangeDataUser:
    
    @allure.title('Изменение почты у зарегистрированнного пользователя')
    def test_change_email_for_registry_user(self):
        token, email, user, password = create_new_user()
        change_email = email + 'test'
        payload = {
            'email': change_email
        }
        response = requests.patch((Url.site + Api.user), headers={'Autorisation': token}, data=payload)
        assert 200 == response.status_code and response.json()["success"] == True
        
    
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
        response = requests.patch((Url.site + Api.user), headers={"Autorisation": ""}, data=payload)
        assert 403 == response.status_code and response.json() == {
                                                                   "success": False,
                                                                   "message": "User with such email already exists"
                                                                   }
        