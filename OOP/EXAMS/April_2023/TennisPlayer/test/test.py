from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Pancho", 20, 20.5)
        self.other = TennisPlayer("Mancho", 20, 24.5)

    def test_correct_init(self):
        self.assertEqual(self.player.name, "Pancho")
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.points, 20.5)
        self.assertEqual(self.player.wins, [])

    def test_set_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Pa"

        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_set_age_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_tournament_not_in_list(self):
        self.player.add_new_win("Tanganyika")
        self.assertEqual(self.player.wins, ["Tanganyika"])

    def test_add_new_win_tournament_in_list(self):
        self.player.wins = ["Tanganyika"]
        result = self.player.add_new_win("Tanganyika")
        self.assertEqual(result, "Tanganyika has been already added to the list of wins!")

    def test_lt_correct(self):
        result = self.player.__lt__(self.other)
        self.assertEqual(result, "Mancho is a top seeded player and he/she is better than Pancho")

    def test_lt_not_correct(self):
        self.other.points = 18.5
        result = self.player.__lt__(self.other)
        self.assertEqual(result, f"Pancho is a better player than Mancho")

    def test_str(self):
        self.player.wins = ["Tanganyika", "Manganyika"]
        self.assertEqual(str(self.player), f"Tennis Player: Pancho\n" \
                                           f"Age: 20\n" \
                                           f"Points: 20.5\n" \
                                           f"Tournaments won: Tanganyika, Manganyika")


if __name__ == "__main__":
    main()
