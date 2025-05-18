import pytest
from src.hh_api import HeadHunterAPI
from unittest.mock import patch


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра HeadHunterAPI."""
    api = HeadHunterAPI()
    return api
