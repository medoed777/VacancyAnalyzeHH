from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.jsonsaver import JSONSaver
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies, parse_salary_input


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")

    # Обработка ввода количества вакансий с установкой значения по умолчанию
    while True:
        try:
            top_n_input = input("Введите количество вакансий для вывода в топ N (по умолчанию 10): ")
            if not top_n_input:
                top_n = 10
                break

            top_n = int(top_n_input)

            if top_n <= 0:
                print("Пожалуйста, введите положительное целое число.")
                continue

            break

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (например, '100000 - 150000', оставьте пустым для всех): ")

    salary_tuple = parse_salary_input(salary_range)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    if salary_tuple is not None:
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_tuple)
    else:
        ranged_vacancies = filtered_vacancies

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)
if __name__ == "__main__":
    user_interaction()
