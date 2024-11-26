class LibraryError(Exception):
    """Базовое исключение для библиотеки"""
    pass


class BookNotFoundError(LibraryError):
    """Книга не найдена"""
    def __init__(self, book_id):
        super().__init__(f"Книга с ID {book_id} не найдена")


class InvalidStatusError(LibraryError):
    """Недопустимый статус книги"""
    def __init__(self, status):
        super().__init__(f"Статус '{status}' недопустим. Используйте 'в наличии' или 'выдана'")