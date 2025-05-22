import pytest
from src.vacancy import Vacancy


def test_vacancy_initialization(vacancy_instance_1):
    assert vacancy_instance_1.name == "Разработчик Python"
    assert vacancy_instance_1.link == "https://example.com/vacancy1"
    assert vacancy_instance_1.salary == 150000.0
    assert vacancy_instance_1.responsibility == "Требуется опыт работы с Python."
    assert vacancy_instance_1.id == 1

def test_initialization_with_id():
    vacancy = Vacancy(name="Developer", link="https://example.com", salary=100000, id=5)
    assert vacancy.id == 5

def test_to_dict():
    vacancy = Vacancy(name="Developer", link="https://example.com", salary=100000)
    expected_dict = {
            'id': 1,
            'name': "Developer",
            'link': "https://example.com",
            'salary': 100000,
            'responsibility': None,
        }
    assert vacancy.to_dict() == expected_dict

def test_vacancy_comparisons(vacancy_instance_1, vacancy_instance_2):
    assert vacancy_instance_1 > vacancy_instance_2
    assert vacancy_instance_2 < vacancy_instance_1
    assert vacancy_instance_1 != vacancy_instance_2

def test_cast_to_object_list():
    vacancies_json = [
        {
            "name": "Developer",
            "alternate_url": "https://example.com",
            "salary": {"from": 60000, "to": 80000},
            "snippet": {"responsibility": "Develop software"},
            "id": 1
        }
    ]

    vacancies = Vacancy.cast_to_object_list(vacancies_json)

    assert len(vacancies) == 1
    assert vacancies[0].name == "Developer"
    assert vacancies[0].salary == 70000

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
