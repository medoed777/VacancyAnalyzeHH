import json
from unittest.mock import mock_open, patch


def test_load_vacancies_with_empty_file(json_saver):
    """Тест загрузки вакансий из пустого файла."""
    with patch("builtins.open", mock_open(read_data="")):
        json_saver._load_vacancies()
        assert json_saver.vacancies == []


def test_load_vacancies_with_invalid_json(json_saver):
    """Тест загрузки вакансий с некорректным JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        json_saver._load_vacancies()
        assert json_saver.vacancies == []


def test_load_vacancies_with_list(json_saver):
    """Тест загрузки вакансий из файла, содержащего список."""
    data = json.dumps([{"id": "1", "name": "Vacancy 1"}, {"id": "2", "name": "Vacancy 2"}])
    with patch("builtins.open", mock_open(read_data=data)):
        json_saver._load_vacancies()
        assert len(json_saver.vacancies) == 2
        assert json_saver.vacancies[0]["id"] == "1"


def test_add_vacancy(json_saver, vacancy_instance_1):
    """Тест добавления новой вакансии."""
    result = json_saver.add_vacancy(vacancy_instance_1)

    assert result == {
        "id": 1,
        "name": "Разработчик Python",
        "link": "https://example.com/vacancy1",
        "salary": 150000.0,
        "responsibility": "Требуется опыт работы с Python.",
    }
    assert len(json_saver.vacancies) == 1


def test_add_vacancy_existing(json_saver, vacancy_instance_1):
    """Тест добавления существующей вакансии."""

    with patch("builtins.open", mock_open(read_data=json.dumps([vacancy_instance_1.to_dict()]))):
        json_saver._load_vacancies()

    result = json_saver.add_vacancy(vacancy_instance_1)

    assert result == "Вакансия с таким id уже существует"


def test_delete_vacancy(json_saver):
    """Тест удаления вакансии по id."""
    vacancy = {"id": "1", "name": "Vacancy 1"}

    with patch("builtins.open", mock_open(read_data=json.dumps([vacancy]))):
        json_saver._load_vacancies()

    json_saver.delete_vacancy("1")

    assert len(json_saver.vacancies) == 0


def test_get_vacancy_with_criteria(json_saver):
    """Тест получения вакансий по критериям."""
    vacancies = [{"id": "1", "name": "Vacancy 1"}, {"id": "2", "name": "Vacancy 2"}]

    with patch("builtins.open", mock_open(read_data=json.dumps(vacancies))):
        json_saver._load_vacancies()

    result = json_saver.get_vacancy(name="Vacancy 1")

    assert len(result) == 1
    assert result[0]["id"] == "1"


def test_get_all_vacancies(json_saver):
    """Тест получения всех вакансий."""
    vacancies = [{"id": "1", "name": "Vacancy 1"}, {"id": "2", "name": "Vacancy 2"}]

    with patch("builtins.open", mock_open(read_data=json.dumps(vacancies))):
        json_saver._load_vacancies()

    result = json_saver.get_vacancy()

    assert len(result) == 2
