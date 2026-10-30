import requests
import allure
from data import Urls


class OrderMethods:

    @staticmethod
    @allure.step("Отправить POST-запрос на создание заказа")
    def create_order(payload):
        return requests.post(Urls.ORDERS_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправить GET-запрос на получение списка заказов")
    def get_orders_list(params=None):
        return requests.get(Urls.ORDERS_ENDPOINT, params=params)

    @staticmethod
    @allure.step("Отправить PUT-запрос на отмену заказа по track={track}")
    def cancel_order(track):
        return requests.put(Urls.ORDERS_CANCEL_ENDPOINT, params={"track": track})
