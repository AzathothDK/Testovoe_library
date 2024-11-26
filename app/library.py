import json
import logging

from app.book import Book
from app.exeptions import InvalidStatusError, BookNotFoundError


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Library:
    def __init__(self) -> None:
        self.file_path = "library.json"
        self.books: list[Book] = []
        self._load_book()

    def _load_book(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                books_data = json.load(file)
                self.books = [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            print("Ошибка чтения файла библиотеки. Начинаем с пустой базы")
            self.books = []

    def _save_book(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def _get_book_by_id(self, book_id):
            """Внутренний метод для поиска книги по ID"""
            for book in self.books:
                if book.id == book_id:
                    return book
            return None

    def add_book(self, title: str, author: str, year: int):
        book_id = len(self.books) + 1  #Уникальный айдишник
        new_book = Book(id=book_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self._save_book()

    def delete_book(self, book_id):
        book = self._get_book_by_id(book_id)
        if not book:
            logger.info(f"Книга с ID {book_id} не найдена")  #Логируем ошибку
            return
        #Логика удаления книги
        self.books = [b for b in self.books if b.id != book_id]
        logger.info(f"Книга с ID {book_id} удалена")

    def search(self, **kwargs):
        """Поиск книги в библиотеке"""
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if str(getattr(book, key, "")).lower() == str(value).lower()]
        return results

    def display_books(self):
        """Отображает все книги в библиотеке"""
        if not self.books:
            print("Библиотека пуста")
            return

        for book in self.books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                f"Год: {book.year}, Статус: {book.status}"
            )

    def change_status(self, id: int, new_status: str):
        """Изменяет статус книги"""
        if new_status not in ["в наличии", "выдана"]:
            raise InvalidStatusError(new_status)

        try:
            book = next(book for book in self.books if book.id == id)
            book.status = new_status
            self._save_book()
            print(f"Статус книги с ID {id} обновлен на '{new_status}'")
        except StopIteration:
            raise BookNotFoundError(id)
