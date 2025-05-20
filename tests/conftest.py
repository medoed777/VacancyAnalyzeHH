import pytest
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра HeadHunterAPI."""
    api = HeadHunterAPI()
    return api


@pytest.fixture
def vacancy_instance_1():
    """Фикстура для создания экземпляра Vacancy"""
    return Vacancy("Разработчик Python", "https://example.com/vacancy1", "120000 - 180000руб", "Требуется опыт работы с Python.")

@pytest.fixture
def vacancy_instance_2():
    """Фикстура для создания второго экземпляра Vacancy"""
    return Vacancy("Разработчик Java", "https://example.com/vacancy2", 100000)


