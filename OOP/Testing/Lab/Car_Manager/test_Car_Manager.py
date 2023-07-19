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

    def test_no_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_no_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_zero_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be "
                                            "zero or negative!")

    def test_zero_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be "
                                            "zero or negative!")

    def test_negative_fuel_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 10

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_with_zero_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or "
                                            "negative!")

    def test_refuel_with_correct_amount(self):
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_amount, 5)

    def test_correct_refuel_with_more_then_capacity(self):
        self.car.refuel(80)
        self.assertEqual(self.car.fuel_amount, 75)

    def test_drive_more_then_possible_raise_exception(self):
        self.car.fuel_amount = 20
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual(str(ex.exception), "You don't have enough "
                                            "fuel to drive!")





if __name__ == "__main__":
    main()