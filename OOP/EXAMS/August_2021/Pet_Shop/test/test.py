from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPepShop(TestCase):
    def setUp(self):
        self.shop = PetShop("Pancho")

    def test_correct_init(self):
        self.assertEqual(self.shop.name, "Pancho")
        self.assertEqual(self.shop.food, {})
        self.assertEqual(self.shop.pets, [])

    def test_add_food__qty_lte_to_zero_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("Mushmuli", 0)

        self.assertEqual(str(ve.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_food_name_not_in_list(self):
        result = self.shop.add_food("Mushmuli", 2.450)
        self.assertEqual(result, f"Successfully added 2.45 grams of Mushmuli.")
        self.assertEqual(self.shop.food, {"Mushmuli": 2.450})

    def test_add_food_name_in_list(self):
        self.shop.food = {"Mushmuli": 2.5}
        result = self.shop.add_food("Mushmuli", 2.500)
        self.assertEqual(result, f"Successfully added 2.50 grams of Mushmuli.")
        self.assertEqual(self.shop.food, {"Mushmuli": 5.000})

    def test_add_pet_name_in_list_raise_ex(self):
        self.shop.pets = ["Mancho"]
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Mancho")

        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_add_pet_name_not_in_list(self):
        self.shop.pets = ["Mancho"]
        result = self.shop.add_pet("Fancho")
        self.assertEqual(result, "Successfully added Fancho.")
        self.assertEqual(self.shop.pets, ["Mancho", "Fancho"])

    def test_feed_pet_not_valid_name_raise_ex(self):
        self.shop.pets = ["Mancho"]
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("Mushmuli", "Fancho")

        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_feed_pet_food_not_in_list(self):
        self.shop.food = {"Mushmuli": 2.500}
        self.shop.pets = ["Mancho"]
        result = self.shop.feed_pet("Mamuli", "Mancho")
        self.assertEqual(result, 'You do not have Mamuli')

    def test_feed_pet_adding_food(self):
        self.shop.pets = ["Mancho"]
        self.shop.food = {"Mushmuli": 2.500}
        result = self.shop.feed_pet("Mushmuli", "Mancho")
        self.assertEqual(result, "Adding food...")
        self.assertEqual(self.shop.food, {"Mushmuli": 1002.5})

    def test_feed_pet_remove_food(self):
        self.shop.pets = ["Mancho"]
        self.shop.food = {"Mushmuli": 102.500}
        result = self.shop.feed_pet("Mushmuli", "Mancho")
        self.assertEqual(result, "Mancho was successfully fed")
        self.assertEqual(self.shop.food, {"Mushmuli": 2.500})

    def test_repr(self):
        self.shop.pets = ["Mancho", "Fancho"]
        self.assertEqual(repr(self.shop), f"Shop Pancho:\n"
                                          f"Pets: Mancho, Fancho")


if __name__ == "__main__":
    main()
