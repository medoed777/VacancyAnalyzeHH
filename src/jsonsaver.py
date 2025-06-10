import json
import os

from src.abstract_class import AbstractJSON
from src.vacancy import Vacancy


class JSONSaver(AbstractJSON):
    """Класс для работы с json"""

    def __init__(self, filename=None):

        if filename is None:
            self.__filename = os.path.abspath("data/vacancies.json")
        else:
            self.__filename = os.path.abspath(filename)

        super().__init__(self.__filename)
        self.vacancies = []
        self._load_vacancies()

    def _load_vacancies(self):
        """Загружает вакансии из файла"""
        try:
            with open(self._AbstractJSON__filename, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, dict) and "items" in data:
                    self.vacancies = data["items"]
                elif isinstance(data, list):
                    self.vacancies = data
                else:
                    self.vacancies = []

        except FileNotFoundError:
            self.vacancies = []
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON. Файл может быть поврежден.")
            self.vacancies = []

    def _save_vacancies(self):
        """Сохраняет вакансии в файл."""
        with open(self._AbstractJSON__filename, "w", encoding="utf-8") as file:
            json.dump(self.vacancies, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в json"""

        if isinstance(vacancy, Vacancy):
            vacancy_dict = vacancy.to_dict()
            if "id" not in vacancy_dict:
                max_id = max((v["id"] for v in self.vacancies if "id" in v), default=0)
                vacancy_dict["id"] = max_id + 1

            if not any(v["id"] == vacancy_dict["id"] for v in self.vacancies):
                self.vacancies.append(vacancy_dict)
                self._save_vacancies()
                return vacancy_dict
            else:
                return "Вакансия с таким id уже существует"
        else:
            return "Некорректный формат вакансии"

    def get_vacancy(self, **criteria):
        """Метод для получения вакансии по указанным критериям"""

        if criteria:
            filtered_vacancies = []
            for vacancy in self.vacancies:
                for key, value in criteria.items():
                    if vacancy.get(key) == value:
                        filtered_vacancies.append(vacancy)
            return filtered_vacancies
        return self.vacancies

    def delete_vacancy(self, vacancy_id):
        """Метод для удаления вакансии по id"""
        initial_count = len(self.vacancies)
        self.vacancies = [vac for vac in self.vacancies if vac.get("id") != vacancy_id]
        self._save_vacancies()

        if len(self.vacancies) < initial_count:
            return "Вакансия успешно удалена."
        else:
            return "Вакансия с указанным id не найдена."
