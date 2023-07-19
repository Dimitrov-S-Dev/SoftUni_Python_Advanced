from OOP.Testing.Lab.Test_Cat.Cat import Cat
from unittest import TestCase, main


class CatTest(TestCase):
    def setUp(self):
        self.cat = Cat("Lia")

    def test_correct_initializing(self):
        self.assertEqual(self.cat.name, "Lia")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_after_eat(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_eat_if_already_fed_raise_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(str(ex.exception), "Already fed.")

    def test_cannot_sleep_if_not_fed_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual(str(ex.exception), "Cannot sleep while hungry")

    def test_not_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
