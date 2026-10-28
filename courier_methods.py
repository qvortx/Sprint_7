import requests
import allure
from data import Urls


class CourierMethods:

    @staticmethod
    @allure.step("Отправить POST-запрос на создание курьера")
    def create_courier(payload):
        return requests.post(Urls.COURIER_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправить POST-запрос на авторизацию курьера")
    def login_courier(payload):
        return requests.post(Urls.COURIER_LOGIN_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправить DELETE-запрос на удаление курьера по id={courier_id}")
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.COURIER_ENDPOINT}/{courier_id}")
