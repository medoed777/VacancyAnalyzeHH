import re


class Vacancy:
    __slots__ = ('name', 'link', 'salary', 'description')

    def __init__(self, name: str, link: str, salary: float | str = None, description: str = None):
        self.name = name
        self.link = link
        self.salary = self._validate_salary(salary)
        self.description = description

    def __repr__(self):
        return f"Vacancy(name={self.name}, link={self.link}, salary={self.salary}, description={self.description})"


    def __str__(self):
        return f"{self.name}, {self.link}, {self.salary}, {self.description}"

    @staticmethod
    def _validate_salary(salary: float | str) -> float | str:
        """Приватный метод для валидации зарплаты."""
        if salary is None or salary == "" or (isinstance(salary, (int, float)) and salary <= 0):
            return "Зарплата не указана"

        if isinstance(salary, str):

            salary_range = re.findall(r'\d+', salary)

            if len(salary_range) == 2:
                return (float(salary_range[0]) + float(salary_range[1])) / 2
            elif len(salary_range) == 1:
                return float(salary_range[0])
            else:
                return "Некорректный формат зарплаты"

        return float(salary)


    def __lt__(self, other):
        """Метод для операции сравнения (меньше)"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Метод для операции сравнения (больше)"""
        return self.salary > other.salary

    def __eq__(self, other):
        """Сравнение по зарплате (равно)"""
        return self.salary == other.salary



if __name__ == "__main__":
    vacancy1 = Vacancy("Разработчик Python", "https://example.com/vacancy1", 120000, "Требуется опыт работы с Python.")
    vacancy2 = Vacancy("Разработчик Java", "https://example.com/vacancy2", "100000 - 120000руб.", "Требуется опыт работы с Java.")

    print(vacancy1)
    print(vacancy2)

