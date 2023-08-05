from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("BMW", "Van", 20000, 20000.00)

    def test_correct_init(self):
        self.assertEqual(self.car.model, "BMW")
        self.assertEqual(self.car.car_type, "Van")
        self.assertEqual(self.car.mileage, 20000)
        self.assertEqual(self.car.price, 20000.00)
        self.assertEqual(self.car.repairs, [])

    def test_set_price_lte_zero_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

    def test_set_mileage_lte_hundred_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotion_price_gte_price_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(20000.00)

        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')

    def test_set_promotion_price_correct(self):
        result = self.car.set_promotional_price(18000.00)
        self.assertEqual(result, 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 18000.00)

    def test_need_repair_price_high(self):
        result = self.car.need_repair(10001.00, "Python_OOP")
        self.assertEqual(result, 'Repair is impossible!')

    def test_need_repair_correct(self):
        result = self.car.need_repair(10000, "Python_OOP")
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 30000.00)
        self.assertEqual(self.car.repairs, ["Python_OOP"])

    def test_gt_type_mismatch(self):
        self.other = SecondHandCar("BMW", "Sport", 10000, 10000.00)
        result = self.car.__gt__(self.other)
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_gt_correct(self):
        self.other = SecondHandCar("BMW", "Van", 10000, 10000.00)
        result = self.car.__gt__(self.other)
        self.assertEqual(result, True)

    def test_str(self):
        self.assertEqual(str(self.car),
                         f'Model BMW | Type Van | Milage 20000km\n'
                         f'Current price: 20000.00 | Number of Repairs: 0')


if __name__ == "__main__":
    main()
