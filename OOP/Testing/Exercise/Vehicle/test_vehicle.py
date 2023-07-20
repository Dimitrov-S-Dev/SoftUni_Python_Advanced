from unittest import TestCase, main

from OOP.Testing.Exercise.Vehicle.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10.25, 125.5)

    def test_correct_initializing(self):
        self.assertEqual(self.vehicle.fuel, 10.5)
        self.assertEqual(self.vehicle.capacity, 10.5)
        self.assertEqual(self.vehicle.horse_power, 125.5)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive_with_not_enough_fuel_raise_exception(self):
        self.vehicle.fuel = 1.2
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_correct_fuel_needed(self):
        self.vehicle.drive(1)
        self.assertEqual(self.vehicle.fuel, 9)

    def test_refuel_with_to_much_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_with_correct_value(self):
        self.vehicle.capacity = 100
        self.vehicle.refuel(20)
        self.assertEqual(self.vehicle.fuel, 30.25)

    def test_correct_str(self):
        self.assertEqual(str(self.vehicle), f"The vehicle has "
                                            f"125.5 horse power with "
                                            f"10.25 fuel left and "
                                            f"1.25 fuel consumption")


if __name__ == "__main__":
    main()
