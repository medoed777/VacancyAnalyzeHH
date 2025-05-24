import os
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для подключения к API"""

    @abstractmethod
    def _connect(self) -> None:
        """Подключение к API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 10) -> list:
        """Получение списка вакансий по запросу."""
        pass


class AbstractJSON(ABC):
    """Абстрактный класс для работы с json"""

    def __init__(self, filename=None):
        if filename is None:
            filename = "data/vacancies.json"
        self.__filename = os.path.abspath(filename)

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавление вакансий в json"""
        pass

    @abstractmethod
    def get_vacancy(self, **criteria):
        """Критерии для поиска в json"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        """Удаление вакансии из json"""
        pass
