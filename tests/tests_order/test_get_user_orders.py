import requests
import allure
from test_data.messages import MessagesData
from config.urls import Urls
from config.endpoints import Endpoints


class TestGetUserOrders:

    url = f'{Urls.BASE_URL}{Endpoints.GET_USER_ORDERS}'

    @allure.title('Успешное получение заказов пользователя')
    def test_get_user_orders_success(self, new_user_with_orders):
        headers = {'Authorization': new_user_with_orders['accessToken']}
        with allure.step('Отправка запроса на получение заказов пользователя'):
            response = requests.get(self.url, headers=headers)

        assert response.status_code == 200 and 'orders' in response.json()


    @allure.title('Неуспешное получение заказов пользователя без авторизации')
    def test_get_user_orders_failure(self):
        headers = {'Authorization': None}
        with allure.step('Отправка запроса на получение заказов без авторизации'):
            response = requests.get(self.url, headers=headers)

        assert (response.status_code == 401
                and response.json()['message'] == MessagesData.MESSAGE_GET_USER_ORDER_WITHOUT_AUTHORIZATION)
