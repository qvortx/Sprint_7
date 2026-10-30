import pytest
import allure
from courier_methods import CourierMethods
from helpers import generate_courier_payload
from data import ResponseMessages


@allure.feature("Создание курьера (POST /api/v1/courier)")
class TestCreateCourier:

    @allure.title("Успешное создание нового курьера при передаче всех обязательных полей")
    def test_create_courier_valid_data_returns_ok_true(self, new_courier_payload):
        response = CourierMethods.create_courier(new_courier_payload)

        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_courier_duplicate_courier_shows_error(self, registered_courier):
        response = CourierMethods.create_courier(registered_courier)

        assert (
            response.status_code == 409
            and response.json().get("message") == ResponseMessages.COURIER_LOGIN_ALREADY_USED
        )

    @allure.title("Нельзя создать курьера с логином, который уже используется")
    def test_create_courier_existing_login_shows_error(self, registered_courier):
        payload_with_same_login = generate_courier_payload()
        payload_with_same_login["login"] = registered_courier["login"]

        response = CourierMethods.create_courier(payload_with_same_login)

        assert (
            response.status_code == 409
            and response.json().get("message") == ResponseMessages.COURIER_LOGIN_ALREADY_USED
        )

    @allure.title("Ошибка при создании курьера без одного из обязательных полей (login или password)")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field_shows_error(self, missing_field):
        payload = generate_courier_payload()
        del payload[missing_field]

        response = CourierMethods.create_courier(payload)

        assert (
            response.status_code == 400
            and response.json().get("message") == ResponseMessages.COURIER_CREATE_INSUFFICIENT_DATA
        )
