import requests
from src.abstract_class import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """Класс для подключения к API"""

    BASE_URL = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.__session: None = None
        self.__is_connected: bool = False

    def _connect(self):
        """Приватный метод подключения к API hh.ru."""
        self.__session = requests.Session()
        response = self.__session.get(self.BASE_URL)
        if response.status_code == 200:
            self.__is_connected = True
            print("Подключение к API hh.ru успешно!")
        else:
            raise ConnectionError(f"Ошибка при подключении к API: {response.status_code}")

    def get_vacancies(self, keyword: str, per_page: int = 10, country: int = 113):
        """Получение списка вакансий по запросу."""
        if not self.__is_connected:
            self._connect()

        params = {
            'text': keyword,
            'per_page': per_page,
            'area': country
        }

        response = self.__session.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            vacancies_data = response.json()
            return vacancies_data.get('items', [])
        else:
            raise RuntimeError(f"Ошибка при получении вакансий: {response.status_code}")


if __name__ == "__main__":
    hh_api = HeadHunterAPI()

    try:
        search_query = input("Введите поисковый запрос: ")
        vacancies = hh_api.get_vacancies(search_query)

        print(f"Найдено вакансий: {len(vacancies)}")
        for item in vacancies:
            print(f"Название: {item['name']}, Ссылка: {item['alternate_url']}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
