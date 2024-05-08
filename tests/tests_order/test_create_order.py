import requests
import allure
from test_data import order_helpers
from test_data.data import Data
from test_data.messages import MessagesData
from config.urls import Urls
from config.endpoints import Endpoints


class TestCreateOrder:

    url = f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}'

    @allure.title('Успешное создание заказа с авторизацией и ингиридиентами')
    def test_create_order_success(self, new_user_and_authorization_data):
        headers = {'Authorization': new_user_and_authorization_data[1]['accessToken']}
        payload = {'ingredients': order_helpers.generate_ingredient_list()}
        with allure.step('Отправка запроса на создание заказа пользователя'):
            response = requests.post(self.url, headers=headers, data=payload)

        assert response.status_code == 200 and 'number' in response.json()['order']


    @allure.title('Успешное создание заказа без авторизации')
    def test_create_order_without_authorization_success(self):
        headers = {'Authorization': None}
        payload = {'ingredients': order_helpers.generate_ingredient_list()}
        with allure.step('Отправка запроса на создание заказа без авторизации'):
            response = requests.post(self.url, headers=headers, data=payload)

        assert response.status_code == 200 and 'number' in response.json()['order']


    @allure.title('Неуспешное создание заказа без ингредиентов')
    def test_create_order_without_ingredients_failure(self, new_user_and_authorization_data):
        headers = {'Authorization': new_user_and_authorization_data[1]['accessToken']}
        payload = {'ingredients': None}
        with allure.step('Отправка запроса на создание заказа без ингредиентов'):
            response = requests.post(self.url, headers=headers, data=payload)

        assert (response.status_code == 400
                and response.json()['message'] == MessagesData.MESSAGE_CREATED_ORDER_WITHOUT_INGREDIENTS)


    @allure.title('Неуспешное создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_wrong_ingredient_hash_failure(self, new_user_and_authorization_data):
        headers = {'Authorization': new_user_and_authorization_data[1]['accessToken']}
        payload = {'ingredients': Data.wrong_ingredient_hash}
        with allure.step('Отправка запроса на создание заказа с неверным хешем ингредиентов'):
            response = requests.post(self.url, headers=headers, data=payload)

        assert (response.status_code == 400
                and response.json()['message'] == MessagesData.MESSAGE_CREATED_ORDER_WITH_WRONG_INGREDIENT_HASH)
