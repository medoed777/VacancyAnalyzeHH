def filter_vacancies(vacancies, filter_words):
    """Функция для фильтрации вакансий по ключевым словам"""
    if not filter_words:
        return vacancies

    return [vac for vac in vacancies if any(word.lower() in vac.name.lower() for word in filter_words)]


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция для фильтрации вакансий по диапазону зарплат"""

    if not salary_range:
        print("Диапазон зарплат не введен. Возвращаем все вакансии.")
        return filtered_vacancies

    # Убираем пробелы и разбиваем строку по тире
    salary_range = salary_range.replace(" ", "")  # Удаляем все пробелы
    salary_parts = salary_range.split("-")

    # Проверка на количество частей
    if len(salary_parts) > 2:
        raise ValueError("Некорректный формат диапазона зарплат. Убедитесь, что он задан в формате 'min-max'.")

    # Преобразование строк в числа
    try:
        min_salary = float(salary_parts[0]) if salary_parts[0] else None
        max_salary = float(salary_parts[1]) if len(salary_parts) == 2 and salary_parts[1] else None
    except ValueError:
        raise ValueError("Не удалось преобразовать значения в диапазоне зарплат. Убедитесь, что они числовые.")

    # Фильтрация вакансий по зарплате
    filtered = [
        vacancy
        for vacancy in filtered_vacancies
        if vacancy.salary is not None
        and isinstance(vacancy.salary, (int, float))
        and (min_salary is None or float(vacancy.salary) >= min_salary)
        and (max_salary is None or float(vacancy.salary) <= max_salary)
    ]

    return filtered


def sort_vacancies(vacancies):
    """Функция для сортировки вакансий"""

    def get_salary(vacancy):
        """Функция для получения зарплаты из вакансии"""
        if isinstance(vacancy.salary, str):
            salary_parts = vacancy.salary.replace(" ", "").split("-")
            try:
                return float(salary_parts[0])
            except (ValueError, IndexError):
                return 0
        elif vacancy.salary is not None:
            return float(vacancy.salary)
        else:
            return 0

    return sorted(vacancies, key=get_salary)


def get_top_vacancies(vacancies, top_n):
    """Функция для получения топа вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies_list):
    """Функция для вывода вакансий"""
    for i, vacancy in enumerate(vacancies_list, start=1):
        print(f"{i}. {vacancy}")


def parse_salary_input(salary_input):
    """Парсинг входных данных о зарплате"""
    salary_input = salary_input.replace(" ", "-")
    return salary_input
