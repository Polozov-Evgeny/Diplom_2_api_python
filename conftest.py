import pytest
from test_data import user_helpers, order_helpers


@pytest.fixture(scope='function')
def new_user_and_registration_data():
    registration_data = user_helpers.generate_user_data()
    yield registration_data
    tokens = user_helpers.login_user_and_return_tokens(registration_data)
    user_helpers.delete_user_account(tokens['accessToken'])


@pytest.fixture(scope='function')
def new_user_and_login_data():
    new_user_and_login_data = user_helpers.register_new_user_and_return_login_data()
    yield new_user_and_login_data
    tokens = user_helpers.login_user_and_return_tokens(new_user_and_login_data)
    user_helpers.delete_user_account(tokens['accessToken'])


@pytest.fixture(scope='function')
def new_user_and_tokens():
    new_user_and_tokens = user_helpers.register_new_user_and_return_tokens()
    yield new_user_and_tokens
    user_helpers.delete_user_account(new_user_and_tokens['accessToken'])


@pytest.fixture(scope='function')
def login_new_user():
    new_user = user_helpers.register_new_user_and_return_login_data()
    tokens = user_helpers.login_user_and_return_tokens(new_user)
    yield new_user, tokens
    user_helpers.delete_user_account(tokens['accessToken'])


@pytest.fixture(scope='function')
def new_user_with_orders(new_user_and_tokens):
    order_helpers.add_user_orders(new_user_and_tokens)
    yield new_user_and_tokens
