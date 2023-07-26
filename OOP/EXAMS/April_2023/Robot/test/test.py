from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("Rambo", "Military", 10, 100)

    def test_correct_init(self):
        self.assertEqual(self.robot.robot_id, "Rambo")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 10)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_set_category_not_in_list_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Robot("Rambo", "Pancho", 10, 200)

        self.assertEqual(str(ve.exception), f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_set_negative_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = - 5

        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_hardware_in_list(self):
        self.robot.hardware_upgrades = ["RAM"]
        result = self.robot.upgrade("RAM", 100)
        self.assertEqual(result, f"Robot Rambo was not upgraded.")
        self.assertEqual(self.robot.hardware_upgrades, ["RAM"])

    def test_upgrade_hardware_not_in_list(self):
        result = self.robot.upgrade("RAM", 100)
        self.assertEqual(result, f'Robot Rambo was upgraded with RAM.')
        self.assertEqual(self.robot.price, 250)
        self.assertEqual(self.robot.hardware_upgrades, ["RAM"])

    def test_update_not_update(self):
        self.robot.software_updates = [10.5]
        result1 = self.robot.update(10.4, 9)
        self.assertEqual(self.robot.software_updates, [10.5])
        self.assertEqual(result1, f"Robot Rambo was not updated.")
        self.second = Robot("Mambo", "Military", 10, 100)
        self.second.software_updates = [10.5]
        result2 = self.second.update(10.6, 11)
        self.assertEqual(self.second.software_updates, [10.5])
        self.assertEqual(result2, f"Robot Mambo was not updated.")

    def test_update_correct(self):
        self.robot.software_updates = [10.5]
        result = self.robot.update(10.6, 9)
        self.assertEqual(result, f'Robot Rambo was updated to version 10.6.')
        self.assertEqual(self.robot.available_capacity, 1)
        self.assertEqual(self.robot.software_updates, [10.5, 10.6])

    def test_gt_correct(self):
        self.second = Robot("Mambo", "Military", 10, 90)
        result = self.robot > self.second
        self.assertEqual(result, f'Robot with ID Rambo is more expensive than Robot with ID Mambo.')

    def test_gt_equal(self):
        self.second = Robot("Mambo", "Military", 10, 100)
        result = self.robot > self.second
        self.assertEqual(result, f'Robot with ID Rambo costs equal to Robot with ID Mambo.')

    def test_not_gt(self):
        self.second = Robot("Mambo", "Military", 10, 120)
        result = self.robot > self.second
        self.assertEqual(result, f'Robot with ID Rambo is cheaper than Robot with ID Mambo.')







if __name__ == "__main__":
    main()
