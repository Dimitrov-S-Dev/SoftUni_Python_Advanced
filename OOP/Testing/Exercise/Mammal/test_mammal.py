from unittest import TestCase, main

from OOP.Testing.Exercise.Mammal.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Lia", "Cat", "Meow")

    def test_correct_initializing(self):
        self.assertEqual(self.mammal.name, "Lia")
        self.assertEqual(self.mammal.type, "Cat")
        self.assertEqual(self.mammal.sound, "Meow")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_correct_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, "Lia makes Meow")

    def test_correct_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(self.mammal._Mammal__kingdom, result)

    def test_correct_info(self):
        result = self.mammal.info()
        self.assertEqual(result, "Lia is of type Cat")


if __name__ == "__main__":
    main()
