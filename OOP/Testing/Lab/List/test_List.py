from OOP.Testing.Lab.List.List import IntegerList
from unittest import TestCase, main


class TestInteger(TestCase):
    def setUp(self):
        self.integer_list = IntegerList("50", 1, False, 3.5, 2, 3)

    def test_correct_initializing(self):
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3])




if __name__ == "__main__":
    main()

