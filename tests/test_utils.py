import pytest
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


def test_filter_vacancies(vacancies):
    filtered = filter_vacancies(vacancies, ["Developer"])
    assert len(filtered) == 3
    assert all("Developer" in vac.name for vac in filtered)

    filtered = filter_vacancies(vacancies, [])
    assert len(filtered) == len(vacancies)

def test_get_vacancies_by_salary(vacancies):
    filtered = get_vacancies_by_salary(vacancies, "60000-100000")
    assert len(filtered) == 3

    filtered = get_vacancies_by_salary(vacancies, "100000-150000")
    assert len(filtered) == 2

    with pytest.raises(ValueError) as excinfo:
        get_vacancies_by_salary(vacancies, "abc")
    assert "Некорректный формат диапазона зарплат" in str(excinfo.value)

def test_sort_vacancies(vacancies):
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies == [
        Vacancy("Junior Developer", "https://example.com/vacancy1",50000),
        Vacancy("Middle Developer", "https://example.com/vacancy2", 75000),
        Vacancy("DevOps Engineer", "https://example.com/vacancy5", 90000),
        Vacancy("Senior Developer", "https://example.com/vacancy3", 100000),
        Vacancy("Data Scientist", "https://example.com/vacancy4", 120000),
    ]

def test_get_top_vacancies(vacancies):
    top_vacancies = get_top_vacancies(vacancies, 3)
    assert len(top_vacancies) == 3
    assert top_vacancies == [
        Vacancy("Junior Developer", "https://example.com/vacancy1",50000),
        Vacancy("Senior Developer", "https://example.com/vacancy3", 100000),
        Vacancy("Middle Developer", "https://example.com/vacancy2", 75000),
    ]


def test_print_vacancies(capsys, vacancies):
    print_vacancies(vacancies)
    captured = capsys.readouterr().out

    expected_output = (
        "1. Название: Junior Developer, Ссылка: https://example.com/vacancy1, Зарплата: 50000.0, Описание: None, id: 29\n"
        "2. Название: Senior Developer, Ссылка: https://example.com/vacancy2, Зарплата: 100000.0, Описание: None, id: 30\n"
        "3. Название: Middle Developer, Ссылка: https://example.com/vacancy3, Зарплата: 75000.0, Описание: None, id: 31\n"
        "4. Название: Data Scientist, Ссылка: https://example.com/vacancy4, Зарплата: 120000.0, Описание: None, id: 32\n"
        "5. Название: DevOps Engineer, Ссылка: https://example.com/vacancy5, Зарплата: 90000.0, Описание: None, id: 33\n"
    )

    assert captured == expected_output
