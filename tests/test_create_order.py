import pytest
import allure
from order_methods import OrderMethods
from helpers import generate_order_payload


@allure.feature("Создание заказа (POST /api/v1/orders)")
class TestCreateOrder:

    @allure.title("Создание заказа с различными вариантами цветов возвращает track")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors_returns_track(self, color, order_cleanup):
        payload = generate_order_payload(color=color)
        response = OrderMethods.create_order(payload)
        order_cleanup.append(response.json().get("track"))

        assert (
            response.status_code == 201
            and "track" in response.json()
            and isinstance(response.json()["track"], int)
        )
