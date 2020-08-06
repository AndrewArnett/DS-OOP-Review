import unittest
from players import Player, Quarterback
from possible_values import team_names, locations
from game import Game
# TODO - some things you can add...

# import the `season` file and make sure generate_random_games only
# makes games with appropriate team names (and never has a team playing itself)

# Complete the FootballGameTest


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        pass  # TODO

    def test_get_winnerr(self):
        pass  # TODO


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='dude', yards=120, touchdowns=5, safety=1, interceptions=0, 
                     field_goals=0)
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150, touchdowns=6, safety=0, interceptions=1,
                     field_goals=1)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude', yards=250, touchdowns=2, completed_passes=17, 
                     interceptions=4, safety=1, field_goals=0)
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback(name='JoeMontana', yards=355, touchdowns=4, completed_passes=20,
                     interceptions=0, safety=0, field_goals=0)
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback(name='JoeMontana', safety=0, field_goals=0, completed_passes=20, yards=355, 
                     touchdowns=4, interceptions=0)
        self.assertEqual((20 - (2 * 0) + (.25 * 355) + 4), qb.passing_score(20, 355, 4, 0))


if __name__ == '__main__':
    unittest.main()
