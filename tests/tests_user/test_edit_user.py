import pytest
import requests
import allure
from test_data import user_helpers
from test_data.messages import MessagesData
from config.urls import Urls
from config.endpoints import Endpoints


class TestEditUser:

    url = f'{Urls.BASE_URL}{Endpoints.UPDATE_USER_DATA}'

    @allure.title('Успешное изменение данных учетной записи пользователя')
    @pytest.mark.parametrize('edit_field', ['email', 'name'],
                             ids=['edit_email', 'edit_name'])
    def test_edit_user_data_success(self, edit_field, new_user_and_authorization_data):
        headers = {'Authorization': new_user_and_authorization_data[1]['accessToken']}
        payload = {edit_field: user_helpers.generate_user_data()[edit_field]}
        with allure.step('Отправка запроса на изменение данных пользователя'):
            response = requests.patch(self.url, headers=headers, data=payload)

        assert (response.status_code == 200
                and response.json()['user'][edit_field] == payload[edit_field])


    @allure.title('Успешное изменение пароля учетной записи пользователя')
    def test_edit_user_password_success(self, new_user_and_authorization_data):
        headers = {'Authorization': new_user_and_authorization_data[1]['accessToken']}
        payload = {'password': user_helpers.generate_user_data()['password']}
        with allure.step('Отправка запроса на изменение пароля пользователя'):
            response_update = requests.patch(self.url, headers=headers, data=payload)
        payload_login = {'email': new_user_and_authorization_data[0]['email'], 'password': payload['password']}
        url_login = f'{Urls.BASE_URL}{Endpoints.LOGIN_USER}'
        with allure.step('Отправка запроса на авторизацию пользователя c измененным паролем'):
            response_login = requests.post(url_login, data=payload_login)

        assert ((response_update.status_code == 200 and response_update.json()['success'] == True) and
                (response_login.status_code == 200 and response_login.json()['success'] == True))


    @allure.title('Без авторизации неуспешное изменение данных пользователя')
    @pytest.mark.parametrize('edit_field', ['email', 'name', 'password'],
                             ids=['edit_email', 'edit_name', 'edit_password'])
    def test_edit_user_data_without_authorization_failure(self, edit_field, new_user_and_authorization_data):
        headers = {'Authorization': None}
        payload = {edit_field: user_helpers.generate_user_data()[edit_field]}
        with allure.step('Отправка запроса без авторизации на изменение данных пользователя'):
            response = requests.patch(self.url, headers=headers, data=payload)

        assert (response.status_code == 401
                and response.json()['message'] == MessagesData.MESSAGE_EDIT_USER_DATA_WITHOUT_AUTHORIZATION)
