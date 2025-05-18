from unittest.mock import patch, MagicMock
import pytest


def test_connect_success(hh_api) -> None:
    """Тест успешного подключения к API."""
    with patch('requests.Session.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        hh_api._connect()
        assert hh_api._HeadHunterAPI__is_connected is True


def test_connect_failure(hh_api) -> None:
    """Тест неуспешного подключения к API."""
    with patch('requests.Session.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with pytest.raises(ConnectionError):
            hh_api._connect()


def test_get_vacancies_success(hh_api) -> None:
    """Тест успешного получения вакансий."""
    with patch('requests.Session.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [{'name': 'Вакансия 1', 'alternate_url': 'http://example.com/1'},
                      {'name': 'Вакансия 2', 'alternate_url': 'http://example.com/2'}]
        }
        mock_get.return_value = mock_response

        hh_api._connect()
        vacancies = hh_api.get_vacancies('разработчик')

        assert len(vacancies) == 2
        assert vacancies[0]['name'] == 'Вакансия 1'


def test_get_vacancies_no_items(hh_api) -> None:
    """Тест получения вакансий с пустым списком."""
    with patch('requests.Session.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': []
        }
        mock_get.return_value = mock_response

        hh_api._connect()
        vacancies = hh_api.get_vacancies('несуществующий запрос')

        assert len(vacancies) == 0
