import pytest
from src.vacancy import Vacancy


def test_vacancy_initialization(vacancy_instance_1):
    assert vacancy_instance_1.name == "Разработчик Python"
    assert vacancy_instance_1.link == "https://example.com/vacancy1"
    assert vacancy_instance_1.salary == 150000.0
    assert vacancy_instance_1.description == "Требуется опыт работы с Python."


def test_vacancy_comparisons(vacancy_instance_1, vacancy_instance_2):
    assert vacancy_instance_1 > vacancy_instance_2
    assert vacancy_instance_2 < vacancy_instance_1
    assert vacancy_instance_1 != vacancy_instance_2


@pytest.mark.parametrize("salary_input, expected_output", [
    (None, "Зарплата не указана"),
    ("", "Зарплата не указана"),
    (-1000, "Зарплата не указана"),
    ("неизвестно", "Некорректный формат зарплаты"),
    ("100000 - 120000", 110000.0),
    ("100000", 100000.0),
])
def test_vacancy_salary_validation(salary_input, expected_output):
    vacancy = Vacancy("Разработчик", "link", salary_input)
    assert vacancy.salary == expected_output
