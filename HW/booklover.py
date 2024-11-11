import pandas as pd

class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list: pd.DataFrame = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})

    def add_book(self, book_name: str, rating: int):
        if book_name in self.book_list['book_name'].values:
            print(f"You have already read '{book_name}'.")
            return
        
        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5.")
            return

        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [rating]
        })

        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1

    def has_read(self, book_name: str) -> bool:
        return book_name in self.book_list['book_name'].values

    def num_books_read(self) -> int:
        return self.num_books

    def fav_books(self) -> pd.DataFrame:
        return self.book_list[self.book_list['book_rating'] > 3]
