import requests
import allure
from generate_data import *


class TestOrderForUser:
    
    @allure.title('Получение списка заказов зарегистрированного пользователя')
    def test_get_orders_for_registry_user(self):
        email, user, password, token = create_new_user()
        order = create_two_orders(token)
        responce = requests.get('https://stellarburgers.nomoreparties.site/api/orders', headers={'Autorisation': token})
        assert responce.status_code == 200
    
    @allure.tittle('Получение списка заказов у незарегистрированного пользователя')   
    def test_get_order_for_noregistry_user(self):
        email, user, password, token = create_new_user()
        order = create_two_orders(token)
        responce = requests.get('https://stellarburgers.nomoreparties.site/api/orders', headers={'Autorisation': token})
        assert responce.status_code == 401
        
        