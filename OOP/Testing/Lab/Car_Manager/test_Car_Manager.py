from OOP.Testing.Lab.Car_Manager.Car_Manager import Car
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_correct_initializing(self):
        self.assertEqual(self.car.make, "Nissan")
        self.assertEqual(self.car.model, "GT-R")
        self.assertEqual(self.car.fuel_consumption, 15)
        self.assertEqual(self.car.fuel_capacity, 75)
        self.assertEqual(self.car.fuel_amount, 0)







if __name__ == "__main__":
    main()