from unittest import TestCase, main

from OOP.Testing.Exercise.Hero.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Carabas", 1, 100, 100)
        self.enemy = Hero("Barabas", 1, 50, 50)

    def test_correct_initialize(self):
        self.assertEqual(self.hero.username, "Carabas")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 10.5)
        self.assertEqual(self.hero.damage, 1.5)

    def test_battle_cannot_fight_yourself_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_self_health_to_zero_raise_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ve.exception), "Your health is lower than "
                                            "or equal to 0. You need to rest")

    def test_battle_enemy_health_to_zero_raise_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ve.exception), "You cannot fight Barabas. "
                                            "He needs to rest")

    def test_battle_correct_health_is_draw(self):
        self.hero.health = 50
        result = self.hero.battle(self.enemy)

        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy.health, -50)
        self.assertEqual(result, "Draw")

    def test_battle_win(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual(result, "You win")

    def test_battle_loose(self):
        self.hero, self.enemy = self.enemy, self.hero
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual(result, "You lose")

    def test_correct_str(self):
        self.assertEqual(str(self.hero), f"Hero Carabas: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 100\n")


if __name__ == "__main__":
    main()
