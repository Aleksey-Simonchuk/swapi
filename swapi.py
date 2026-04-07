import requests
from pathlib import Path


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, added_request=''):
        try:
            response = requests.get(f'{self.base_url}{added_request}')
            response.raise_for_status()
            return response
        except Exception:
            print("Возникла ошибка при выполнении запроса")


class SWRequester(APIRequester):

    def __init__(self, base_url):
        super().__init__(base_url)

    def get_sw_categories(self):
        response = requests.get(f'{self.base_url}/')
        return response.json().keys()

    def get_sw_info(self, sw_type):
        response = requests.get(f'{self.base_url}/{sw_type}/')
        return response.text


def save_sw_data(url='https://swapi.dev/api', path='data'):
    object = SWRequester(url)
    Path(path).mkdir(exist_ok=True)
    categories = object.get_sw_categories()
    for category in categories:
        with open(f'{path}/{category}.txt', 'a', encoding='utf-8') as f:
            f.write(object.get_sw_info(category))
