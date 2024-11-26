from library import Library


def main():
    library = Library()

    while True:
        print("""
        Меню:
        1. Добавить книгу
        2. Удалить книгу
        3. Искать книгу
        4. Показать все книги
        5. Изменить статус книги
        6. Выйти
        """)
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            year = int(input("Введите год издания: ").strip())
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: ").strip())
            library.delete_book(book_id)

        elif choice == "3":
            field = input("Искать по (title, author, year): ").strip()
            query = input("Введите запрос: ").strip()
            results = library.search(**{field: query})
            if results:
                for book in results:
                    print(
                        f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                        f"Год: {book.year}, Статус: {book.status}"
                    )
            else:
                print("Книги не найдены")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги: ").strip())
            new_status = input("Введите новый статус (в наличии/выдана): ").strip()
            library.change_status(book_id, new_status)

        elif choice == "6":
            print("Выход из программы")
            break

        else:
            print("Некорректный выбор. Попробуйте снова")


if __name__ == "__main__":
    main()