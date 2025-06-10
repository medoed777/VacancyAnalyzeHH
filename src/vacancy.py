import re
from typing import Any, Optional


class Vacancy:
    """Класс для работы с вакансиями"""

    slots = ("name", "link", "salary", "responsibility", "id")
    _id_counter = 1

    def __init__(
        self,
        name: str,
        link: str,
        salary: Optional[float | str] = None,
        responsibility: Optional[str | None] = None,
        id: Optional[int] = None,
    ) -> None:
        if id is None:
            self.id = Vacancy._id_counter
            Vacancy._id_counter += 1
        else:
            self.id = id

        self.name = name
        self.link = link
        self.salary = self._validate_salary(salary)
        self.responsibility = responsibility

    def __str__(self) -> str:
        return f"Название: {self.name}, Ссылка: {self.link}, Зарплата: {self.salary}, Описание: {self.responsibility}, id: {self.id}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        """Преобразует объект Vacancy в словарь."""
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link,
            "salary": self.salary,
            "responsibility": self.responsibility,
        }

    @classmethod
    def cast_to_object_list(cls, vacancies_json):
        """Преобразует JSON-данные вакансий в список объектов Vacancy."""
        vacancies = []
        for item in vacancies_json:
            name = item.get("name")
            link = item.get("alternate_url")
            salary = item.get("salary", "salary_range")
            responsibility = item.get("snippet", {}).get("responsibility", "")
            id = item.get("id")
            vacancy = cls(name, link, salary, responsibility, id)
            vacancies.append(vacancy)
        return vacancies

    @staticmethod
    def _validate_salary(salary: float | str) -> float | str:
        if isinstance(salary, dict):
            # Извлекаем значения из словаря
            salary_from = salary.get("from", 0)
            salary_to = salary.get("to", 0)

            salary_from = salary_from if salary_from is not None else 0
            salary_to = salary_to if salary_to is not None else 0

            if salary_from and salary_to:
                return (salary_from + salary_to) / 2
            else:
                return max(salary_from, salary_to)
            # Вычисляем среднюю зарплату

        else:
            if (
                salary is None
                or (isinstance(salary, (int, float)) and salary <= 0)
                or (isinstance(salary, str) and salary.strip() == "")
            ):
                return "Зарплата не указана"

            if isinstance(salary, str):
                salary = salary.replace(" ", "").replace("руб.", "").replace("руб", "")
                salary_range = re.findall(r"\d+", salary)

                if len(salary_range) == 2:
                    return (float(salary_range[0]) + float(salary_range[1])) / 2
                elif len(salary_range) == 1:
                    return float(salary_range[0])
                else:
                    return "Некорректный формат зарплаты"

            return float(salary)

    def __lt__(self, other) -> Any:
        """Метод для операции сравнения (меньше)"""
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return NotImplemented

    def __gt__(self, other) -> Any:
        """Метод для операции сравнения (больше)"""
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        return NotImplemented

    def __eq__(self, other) -> Any:
        """Сравнение по зарплате (равно)"""
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False
