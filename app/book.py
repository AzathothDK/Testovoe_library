class Book:
    def __init__(self, id: int, title: str, author: str, year: str, status: str = ["В наличии"]):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def to_dict(self) -> dict:
        """Преобразование книги в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }
    

    @staticmethod
    def from_dict(data: dict):
        """Создание объекта класса книги из словаря"""
        return Book (
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        )