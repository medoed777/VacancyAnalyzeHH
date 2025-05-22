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

    if "-" not in salary_range:
        raise ValueError("Некорректный формат диапазона зарплат. Убедитесь, что он задан в формате 'min-max'.")

    try:
        min_salary, max_salary = map(float, salary_range.split("-"))
    except ValueError:
        raise ValueError("Не удалось преобразовать значения в диапазоне зарплат. Убедитесь, что они числовые.")

    return [
        vacancy
        for vacancy in filtered_vacancies
        if vacancy.salary is not None and min_salary <= vacancy.salary <= max_salary
    ]


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
