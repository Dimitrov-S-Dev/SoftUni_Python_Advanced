from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plant = Plantation(1)

    def test_correct_init(self):
        self.assertEqual(self.plant.size, 1)
        self.assertEqual(self.plant.plants, {})
        self.assertEqual(self.plant.workers, [])

    def test_set_size_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.size = -1

        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_already_in_list_raise_ve(self):
        self.plant.workers = ["Pancho"]
        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker("Pancho")

        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_worker_correct(self):
        self.plant.workers = ["Mancho"]
        result = self.plant.hire_worker("Pancho")
        self.assertEqual(result, "Pancho successfully hired.")
        self.assertEqual(self.plant.workers, ["Mancho", "Pancho"])

    def test_len(self):
        self.plant.plants = {"Pancho": ["ABC"], "Mancho": ["DFG"]}
        self.assertEqual(len(self.plant), 2)

    def test_planting_worker_not_in_list_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Pancho", "ABC")

        self.assertEqual(str(ve.exception), "Worker with name Pancho is not hired!")

    def test_plantation_full_raise_ve(self):
        self.plant.workers = ["Pancho"]
        self.plant.plants = {"Pancho": ["ABC"]}
        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Pancho", "DFG")

        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_worker_in_list_correct(self):
        self.plant.size = 10
        self.plant.workers = ["Pancho"]
        self.plant.plants = {"Pancho": ["ABC"]}
        result = self.plant.planting("Pancho", "DFG")
        self.assertEqual(result, "Pancho planted DFG.")
        self.assertEqual(len(self.plant), 2)
        self.assertEqual(self.plant.plants, {"Pancho": ["ABC", "DFG"]})

    def test_planting_worker_not_in_list_correct(self):
        self.plant.size = 8
        self.plant.workers = ["Pancho", "Mancho"]
        self.plant.plants = {"Pancho": ["ABC"]}
        result = self.plant.planting("Mancho", "DFG")
        self.assertEqual(result, "Mancho planted it's first DFG.")
        self.assertEqual(len(self.plant), 2)
        self.assertEqual(self.plant.plants, {"Pancho": ["ABC"], "Mancho": ["DFG"]})

    def test_str(self):
        self.plant.size = 10
        self.plant.workers = ["Pancho", "Mancho"]
        self.plant.plants = {"Pancho": ["ABC"], "Mancho": ["DFG"]}
        self.assertEqual(str(self.plant),
                         f"Plantation size: 10\nPancho, Mancho\nPancho planted: ABC\nMancho planted: DFG")

    def test_repr(self):
        self.plant.size = 10
        self.plant.workers = ["Pancho", "Mancho"]
        self.assertEqual(repr(self.plant),
                         f"Size: 10\nWorkers: Pancho, Mancho")


if __name__ == "__main__":
    main()
