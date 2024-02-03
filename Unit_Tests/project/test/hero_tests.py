from unittest import TestCase

from Tasks.hero import Hero


class TestHeroClass(TestCase):
    def setUp(self):
        self.hero_data = {
            'username': 'some_username',
            'level': 10,
            'health': 100,
            'damage': 50,
        }

        self.enemy_hero_data = {
            'username': 'enemy_username',
            'level': 10,
            'health': 100,
            'damage': 50,
        }

        self.hero = Hero(
            self.hero_data['username'],
            self.hero_data['level'],
            self.hero_data['health'],
            self.hero_data['damage']
        )

        self.enemy_hero = Hero(
            self.enemy_hero_data['username'],
            self.enemy_hero_data['level'],
            self.enemy_hero_data['health'],
            self.enemy_hero_data['damage']
        )

    # __init__()
    def test_init_expect_correct_instance_attributes(self):
        self.assertEqual(self.hero_data['username'], self.hero.username)
        self.assertEqual(self.hero_data['level'], self.hero.level)
        self.assertEqual(self.hero_data['health'], self.hero.health)
        self.assertEqual(self.hero_data['damage'], self.hero.damage)

    # battle()
    def test_battle_hero_username_equals_enemy_username_expect_raises(self):
        message = 'You cannot fight yourself'
        self.enemy_hero.username = self.hero.username
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(message, str(ex.exception))

    def test_battle_when_hero_health_is_zero_or_below_expect_raises(self):
        message = 'Your health is lower than or equal to 0. You need to rest'
        with self.assertRaises(ValueError) as ex:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual(message, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.hero.health = -1
            self.hero.battle(self.enemy_hero)
        self.assertEqual(message, str(ex.exception))

    def test_battle_when_enemy_hero_health_is_zero_or_below_expect_raises(self):
        message = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        with self.assertRaises(ValueError) as ex:
            self.enemy_hero.health = 0
            self.enemy_hero.battle(self.hero)
            self.assertEqual(message, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.enemy_hero.health = -1
            self.enemy_hero.battle(self.hero)
            self.assertEqual(message, str(ex.exception))

    def test_hero_health_after_battle_expect_correct_hero_health(self):
        expected_hero_health = self.hero.health - self.enemy_hero.damage
        self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_hero_health, self.hero.health)

    def test_enemy_hero_health_after_battle_expect_correct_hero_health(self):
        expected_enemy_hero_health = self.enemy_hero.health - self.hero.damage
        self.enemy_hero.battle(self.hero)
        self.assertEqual(expected_enemy_hero_health, self.enemy_hero.health)

    def test_battle_when_draw_expect_draw_result(self):
        self.hero.damage = 100
        self.enemy_hero.damage = 100
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, 'Draw')
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)

    def test_battle_when_enemy_hero_health_becomes_0_or_negative_expect_hero_to_win(self):
        self.enemy_hero.health = 50
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, 'You win')

        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(60, self.hero.damage + 5)
        self.assertEqual(0, self.enemy_hero.health)

    def test_battle_when_hero_health_becomes_0_or_negative_expect_enemy_hero_to_win(self):
        self.hero.health = 50
        result = self.enemy_hero.battle(self.hero)
        self.assertEqual(result, 'You win')
        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(55, self.enemy_hero.health)
        self.assertEqual(55, self.enemy_hero.damage)
        self.assertEqual(0, self.hero.health)

    # __str__()
    def test_str_expect_valid_data(self):
        expected = [
            f'Hero {self.hero_data["username"]}: {self.hero_data["level"]} lvl',
            f'Health: {self.hero_data["health"]}',
            f'Damage: {self.hero_data["damage"]}\n'
        ]
        self.assertEqual('\n'.join(expected), str(self.hero))

        expected = [
            f'Hero {self.enemy_hero_data["username"]}: {self.enemy_hero_data["level"]} lvl',
            f'Health: {self.enemy_hero_data["health"]}',
            f'Damage: {self.enemy_hero_data["damage"]}\n'
        ]
        self.assertEqual('\n'.join(expected), str(self.enemy_hero))
