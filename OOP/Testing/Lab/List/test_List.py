from OOP.Testing.Lab.List.List import IntegerList
from unittest import TestCase, main


class TestInteger(TestCase):
    def setUp(self):
        self.integer_list = IntegerList("50", 1, False, 3.5, 2, 3)

    def test_correct_initializing(self):
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3])

    def test_correct_get_data(self):
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])

    def test_add_with_non_integer_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(2.5)

        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_add_correct(self):
        result = self.integer_list.add(4)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3, 4])

    def test_remove_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(6)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_remove_index_with_correct_index(self):
        result = self.integer_list.remove_index(1)

        self.assertNotIn(2, self.integer_list._IntegerList__data)
        self.assertEqual(2, result)

    def test_get_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(6)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_get_correct_index(self):
        result = self.integer_list.get(0)
        self.assertEqual(result, 1)

    def test_insert_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(6, 1)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_insert_element_not_int_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 3.5)

        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_insert_correct(self):
        self.integer_list.insert(0, 9)
        self.assertEqual(self.integer_list.get_data(), [9, 1, 2, 3])







if __name__ == "__main__":
    main()

