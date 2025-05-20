from src.abstract_class import AbstractJSON
import json


class JSONSaver(AbstractJSON):
    """Класс для работы с json"""
    def __init__(self, filename="../data/vacancies.json"):
        super().__init__(filename)
        self.vacancies = []
        self._load_vacancies()

    def _load_vacancies(self):
        """Загружает вакансии из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

                if isinstance(data, dict) and 'items' in data:
                    self.vacancies = data['items']
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
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в json"""

        if isinstance(vacancy, dict) and 'id' in vacancy:
            if all(isinstance(v, dict) for v in self.vacancies):
                if not any(v['id'] == vacancy['id'] for v in self.vacancies):
                    self.vacancies.append(vacancy)
                    self._save_vacancies()
                    return vacancy
                else:
                    return "Вакансия с таким id уже существует"
            else:
                return "Ошибка: данные в vacancies имеют некорректный формат"
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
        self.vacancies = [vac for vac in self.vacancies if vac.get('id') != vacancy_id]
        self._save_vacancies()


if __name__ == "__main__":
    storage = JSONSaver()
    print(storage.add_vacancy({'id': 1, 'title': 'Python Developer', 'company': 'OpenAI'}))
    print(storage.add_vacancy({'id': 2, 'title': 'Data Scientist', 'company': 'Google'}))
    print(storage.get_vacancy(title='Python Developer'))
    storage.delete_vacancy(1)
    print(storage.get_vacancy())
