import unittest
import os
from app.library import Library
from app.book import Book
from app.exeptions import BookNotFoundError, InvalidStatusError


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создаем временную библиотеку для тестов"""
        self.test_file = "test_library.json"
        self.library = Library()
        self.library.file_path = self.test_file

    def tearDown(self):
        """Удаляем временный файл после тестов."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")

    def test_delete_book(self):
        """Тест удаления книги."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.library.delete_book(1)
        self.assertEqual(len(self.library.books), 0)

        #Проверка удаления несуществующей книги
        with self.assertLogs('app.library', level="INFO") as log:
            self.library.delete_book(99)
        self.assertIn("Книга с ID 99 не найдена", log.output[0])

    def test_search_books(self):
        """Тест поиска книги."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.library.add_book("Скотный двор", "Джордж Оруэлл", 1945)

        results = self.library.search(title="1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

        results = self.library.search(author="Джордж Оруэлл")
        self.assertEqual(len(results), 2)

    def test_change_status(self):
        """Тест изменения статуса книги."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

        #Тест с неверным статусом
        with self.assertRaises(InvalidStatusError):
            self.library.change_status(1, "неизвестный статус")

        #Тест с несуществующим ID книги
        with self.assertRaises(BookNotFoundError):
            self.library.change_status(99, "в наличии")

    def test_load_and_save_books(self):
        """Тест загрузки и сохранения книг."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.library._save_book()

        new_library = Library()
        new_library.file_path = self.test_file
        new_library._load_book()

        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].title, "1984")


if __name__ == "__main__":
    unittest.main()