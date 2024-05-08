import pytest
import requests
import allure
from test_data import user_helpers
from test_data.messages import MessagesData
from config.urls import Urls
from config.endpoints import Endpoints


class TestLoginUser:

    url = f'{Urls.BASE_URL}{Endpoints.LOGIN_USER}'

    @allure.title('Успешная авторизация пользователя')
    def test_login_user_success(self, new_user_and_authorization_data):
        payload = new_user_and_authorization_data[0]
        with allure.step('Отправка запроса на авторизацию пользователя'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 200 and response.json()['success'] == True)


    @allure.title('Невозможность авторизоваться пользователем с некорректными данными')
    @pytest.mark.parametrize('wrong_field', ['email', 'password', 'all'],
                             ids=['wrong_email', 'wrong_password', 'all_wrong_fields'])
    def test_login_user_with_wrong_fields_failure(self, wrong_field, new_user_and_authorization_data):
        payload = user_helpers.generate_user_login_data_with_wrong_field(wrong_field, new_user_and_authorization_data[0])
        with allure.step('Отправка запроса на авторизацию пользователя с некорректными данными'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 401
                and response.json()['message'] == MessagesData.MESSAGE_CREATE_USER_WITH_WRONG_FIELDS)
