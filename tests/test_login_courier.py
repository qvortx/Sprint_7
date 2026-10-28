import pytest
import allure
from courier_methods import CourierMethods
from helpers import generate_courier_payload
from data import ResponseMessages


@allure.feature("Логин курьера (POST /api/v1/courier/login)")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться, успешный запрос возвращает id")
    def test_login_courier_valid_credentials_returns_id(self, registered_courier):
        login_payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        response = CourierMethods.login_courier(login_payload)

        assert (
            response.status_code == 200
            and "id" in response.json()
            and isinstance(response.json()["id"], int)
        )

    @allure.title("Ошибка авторизации при указании неправильного логина или пароля")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_courier_wrong_credentials_shows_error(self, registered_courier, wrong_field):
        login_payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        login_payload[wrong_field] = f"{login_payload[wrong_field]}_incorrect"

        response = CourierMethods.login_courier(login_payload)

        assert (
            response.status_code == 404
            and response.json().get("message") == ResponseMessages.COURIER_ACCOUNT_NOT_FOUND
        )

    @allure.title("Ошибка при авторизации под несуществующим пользователем")
    def test_login_courier_non_existent_user_shows_error(self):
        random_user = generate_courier_payload()
        login_payload = {
            "login": random_user["login"],
            "password": random_user["password"]
        }

        response = CourierMethods.login_courier(login_payload)

        assert (
            response.status_code == 404
            and response.json().get("message") == ResponseMessages.COURIER_ACCOUNT_NOT_FOUND
        )

    @allure.title("Ошибка авторизации при передаче пустой строки в поле login или password")
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_login_courier_empty_required_field_shows_error(self, registered_courier, empty_field):
        login_payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        login_payload[empty_field] = ""

        response = CourierMethods.login_courier(login_payload)

        assert (
            response.status_code == 400
            and response.json().get("message") == ResponseMessages.COURIER_LOGIN_INSUFFICIENT_DATA
        )

    @allure.title("Ошибка авторизации при отсутствии ключа обязательного поля (login или password)")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_required_field_shows_error(self, registered_courier, missing_field):
        login_payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        del login_payload[missing_field]

        response = CourierMethods.login_courier(login_payload)

        assert (
            response.status_code == 400
            and response.json().get("message") == ResponseMessages.COURIER_LOGIN_INSUFFICIENT_DATA
        )
