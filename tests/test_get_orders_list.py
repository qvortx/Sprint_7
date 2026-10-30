import allure
from order_methods import OrderMethods


@allure.feature("Получение списка заказов (GET /api/v1/orders)")
class TestGetOrdersList:

    @allure.title("В тело ответа возвращается непустой список заказов")
    def test_get_orders_list_without_params_returns_orders_list(self):
        response = OrderMethods.get_orders_list()

        assert (
            response.status_code == 200
            and "orders" in response.json()
            and isinstance(response.json()["orders"], list)
            and len(response.json()["orders"]) > 0
        )
