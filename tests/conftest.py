import pytest
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра HeadHunterAPI."""
    api = HeadHunterAPI()
    return api


@pytest.fixture
def vacancy_instance():
    """Фикстура для создания экземпляра Vacancy с предустановленными значениями."""
    return Vacancy("Разработчик Python", "https://example.com/vacancy1", 120000, "Требуется опыт работы с Python.")
