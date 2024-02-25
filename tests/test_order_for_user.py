import requests
import allure
from generate_data import *
from data import *


class TestOrderForUser:
    
    @allure.title('Получение списка заказов зарегистрированного пользователя')
    def test_get_orders_for_registry_user(self, delete_user):
        token, email, user, password= create_new_user()
        orders = create_two_orders(token)
        response = requests.get((Url.site + Api.orders), headers={'Autorisation': token})
        assert 200 == response.status_code and response.json()['orders']['number']
        
        
    @allure.title('Получение списка заказов у незарегистрированного пользователя')   
    def test_get_order_for_noregistry_user(self):
        email, user, password, token = create_new_user()
        order = create_two_orders(token)
        response = requests.get((Url.site + Api.orders), headers={'Autorisation': token})
        assert 401 == response.status_code and response.json() == {
                                                                    "success": False, 
                                                                    "message": "You should be authorised"
                                                                   }
        
        