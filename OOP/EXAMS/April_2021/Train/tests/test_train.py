from project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Pancho", 20)

    def test_correct_init(self):
        self.assertEqual(self.train.name, "Pancho")
        self.assertEqual(self.train.capacity, 20)
        self.assertEqual(self.train.passengers, [])
        self.assertEqual(self.train.TRAIN_FULL, "Train is full")
        self.assertEqual(self.train.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(self.train.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(self.train.PASSENGER_ADD, "Added passenger {}")
        self.assertEqual(self.train.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(self.train.ZERO_CAPACITY, 0)

    def test_add_len_eq_to_capacity_raise_ve(self):
        self.train.capacity = 2
        self.train.passengers = ["Pancho", "Mancho"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Fancho")

        self.assertEqual(str(ve.exception), "Train is full")

    def test_add_passenger_name_in_list_raise_ve(self):
        self.train.capacity = 3
        self.train.passengers = ["Pancho", "Mancho"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Mancho")

        self.assertEqual(str(ve.exception), "Passenger Mancho Exists")

    def test_add_correct(self):
        self.train.capacity = 5
        self.train.passengers = ["Pancho", "Mancho"]
        result = self.train.add("Fancho")

        self.assertEqual(result, "Added passenger Fancho")
        self.assertEqual(self.train.passengers, ["Pancho", "Mancho", "Fancho"])

    def test_remove_passenger_not_in_list_raise_ve(self):
        self.train.passengers = ["Pancho", "Mancho"]
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Fancho")

        self.assertEqual(str(ve.exception), "Passenger Not Found")

    def test_remove_correct(self):
        self.train.passengers = ["Pancho", "Mancho"]
        result = self.train.remove("Mancho")

        self.assertEqual(result, "Removed Mancho")
        self.assertEqual(self.train.passengers, ["Pancho"])


if __name__ == "__main__":
    main()
