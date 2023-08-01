from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Pancho")

    def test_correct_init(self):
        self.assertEqual(self.library.name, "Pancho")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_name_setter_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book_author_not_in_list(self):
        self.library.books_by_authors = {"James": ["Shogun"]}
        self.library.add_book("King", "It")
        self.assertEqual(self.library.books_by_authors, {"James": ["Shogun"], "King": ["It"]})

    def test_add_book_title_not_in_list(self):
        self.library.books_by_authors = {"James": ["Shogun"], "King": ["It"]}
        self.library.add_book("King", "Misery")
        self.assertEqual(self.library.books_by_authors, {"James": ["Shogun"], "King": ["It", "Misery"]})

    def test_add_reader_name_not_in_list(self):
        self.library.readers = {"Mancho": []}
        self.library.add_reader("Fancho")
        self.assertEqual(self.library.readers, {"Mancho": [], "Fancho": []})

    def test_add_reader_name_in_list(self):
        self.library.readers = {"Mancho": []}
        result = self.library.add_reader("Mancho")
        self.assertEqual(result, "Mancho is already registered in the Pancho library.")

    def test_rent_book_reader_not_in_list(self):
        self.library.books_by_authors = {"James": ["Shogun"]}
        self.library.readers = {"Mancho": []}
        result = self.library.rent_book("Fancho", "James", "Shogun")
        self.assertEqual(result, f"Fancho is not registered in the Pancho Library.")

    def test_rent_book_author_not_in_list(self):
        self.library.books_by_authors = {"James": ["Shogun"]}
        self.library.readers = {"Mancho": []}
        result = self.library.rent_book("Mancho", "King", "It")
        self.assertEqual(result, "Pancho Library does not have any King's books.")

    def test_rent_book_title_not_in_list(self):
        self.library.books_by_authors = {"James": ["Shogun"]}
        self.library.readers = {"Mancho": []}
        result = self.library.rent_book("Mancho", "James", "King Rat")
        self.assertEqual(result, """Pancho Library does not have James's "King Rat".""")

    def test_rent_book_correct(self):
        self.library.books_by_authors = {"James": ["King Rat"]}
        self.library.readers = {"Mancho": [{"James": "Shogun"}], "Fancho": []}
        self.library.rent_book("Mancho", "James", "King Rat")
        self.assertEqual(self.library.books_by_authors, {"James": []})
        self.assertEqual(self.library.readers, {"Fancho": [], "Mancho": [{"James": "Shogun"}, {"James": "King Rat"}]})




if __name__ == "__main__":
    main()
