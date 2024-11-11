import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def setUp(self):
        """Create a BookLover instance for testing."""
        self.test_lover = BookLover("Jane Doe", "jane@example.com", "fantasy")

    def test_1_add_book(self):
        """Add a book and test if it is in `book_list`."""
        self.test_lover.add_book("Harry Potter", 5)
        self.assertIn("Harry Potter", self.test_lover.book_list['book_name'].values)

    def test_2_add_book(self):
        """Add the same book twice. Test if it's in `book_list` only once."""
        self.test_lover.add_book("Harry Potter", 5)
        self.test_lover.add_book("Harry Potter", 4)  # Same book, different rating
        self.assertEqual(len(self.test_lover.book_list), 1)

    def test_3_has_read(self):
        """Pass a book in the list and test if the answer is `True`."""
        self.test_lover.add_book("The Midnight Library", 5)
        self.assertTrue(self.test_lover.has_read("The Midnight Library"))

    def test_4_has_read(self):
        """Pass a book NOT in the list and test if the answer is `False`."""
        self.assertFalse(self.test_lover.has_read("Charlotte's Webb"))

    def test_5_num_books_read(self):
        """Add some books to the list, and test num_books matches expected."""
        self.test_lover.add_book("1984", 5)
        self.test_lover.add_book("Outliers", 4)
        self.assertEqual(self.test_lover.num_books_read(), 2)

    def test_6_fav_books(self):
        """Add some books with ratings to the list, check that returned books have rating > 3."""
        self.test_lover.add_book("The Hunger Games", 2)
        self.test_lover.add_book("To Kill a Mockingbird", 4)
        self.test_lover.add_book("When Breathe Becomes Air", 5)
        
        fav_books = self.test_lover.fav_books()
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    unittest.main(verbosity=3)
