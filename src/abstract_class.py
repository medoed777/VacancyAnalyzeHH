from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для подключения к API"""
    @abstractmethod
    def _connect(self):
        """Подключение к API."""
        pass

    @abstractmethod
    def get_vacancies(self, query: str, per_page: int = 10):
        """Получение списка вакансий по запросу."""
        pass
