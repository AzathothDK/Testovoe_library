# Структура проекта:


* app/ - основное приложение

* tests/ - тесты

- app/library.py - Бизнес логика

- app/book.py - Модель книги

- app/main.py - Запуск программы

## Функционал:


### Модуль Library

Здесь написана вся логика. Реализованы следующие методы:

`add_book(title, author, year):` Добавление книги

`delete_book(book_id):` Удаление книги по ID

`search(self, **kwargs):` Поиск книги

`change_status(self, id: int, new_status: str):` Обновление статуса книги

`display_books(self):` Вывод всез книг, что есть в библиотеке

### Логирование

Используется встроенный модуль logging для ведения логов операций


## Запускаем программу:

`python3 main.py`

## Запускаем тесты:

`python3 -m unittest discover tests`

### Если вылетает ошибка во время зауска тестов, то:

`PYTHONPATH=$(pwd) python3 -m unittest tests/test_library.py`

`PYTHONPATH=$(pwd) python3 -m unittest discover -s tests -p "*.py"`
