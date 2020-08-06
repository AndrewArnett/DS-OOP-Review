'''Player class to record stats for individual players
'''


class Player:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    '''
    def __init__(self, name, yards, touchdowns, safety,
                 interceptions, field_goals):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.touchdowns
        safety_points = 2 * self.safety
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name, yards, touchdowns, completed_passes,
                 interceptions, safety, field_goals):
        super().__init__(name, yards, touchdowns, interceptions,
                         safety, field_goals)
        self.completed_passes = completed_passes
        self.interceptions = interceptions

    def passing_score(self, completed_passes, yards, touchdowns, 
                     interceptions):
        '''This is a random formula... FYI
        '''       
        score = completed_passes - (2 * interceptions) + (.25 * 
                     yards) + touchdowns
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.
