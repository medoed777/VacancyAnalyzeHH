import json
from unittest.mock import mock_open, patch

import pytest

from src.hh_api import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра HeadHunterAPI."""
    api = HeadHunterAPI()
    return api


@pytest.fixture
def vacancy_instance_1():
    """Фикстура для создания экземпляра Vacancy."""
    return Vacancy(
        id=1,
        name="Разработчик Python",
        link="https://example.com/vacancy1",
        salary=150000.0,
        responsibility="Требуется опыт работы с Python.",
    )


@pytest.fixture
def vacancy_instance_2():
    """Фикстура для создания второго экземпляра Vacancy"""
    return Vacancy(
        "Разработчик Java",
        "https://example.com/vacancy2",
        100000,
    )


@pytest.fixture
def vacancies():
    return [
        Vacancy("Junior Developer", "https://example.com/vacancy1", 50000),
        Vacancy("Senior Developer", "https://example.com/vacancy2", 100000),
        Vacancy("Middle Developer", "https://example.com/vacancy3", 75000),
        Vacancy("Data Scientist", "https://example.com/vacancy4", 120000),
        Vacancy("DevOps Engineer", "https://example.com/vacancy5", 90000),
    ]


@pytest.fixture
def json_saver():
    """Фикстура для создания экземпляра JSONSaver."""
    with patch("builtins.open", mock_open(read_data=json.dumps({"items": []}))):
        saver = JSONSaver()
        yield saver
