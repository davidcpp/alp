class Row_Table():
    def __init__(self, team_name, wins, draws, losses, goals_scored, goals_lost):
        self.team_name = team_name
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_lost = goals_lost
        self.points = 0
        self.goal_balance = 0
        self.matches = 0
        self.ranking = 0

    def calculate_points(self):
        self.points = self.wins * 3 + self.draws
        return self.points

    def calculate_matches(self):
        self.matches = self.wins + self.draws + self.losses
        return self.matches

    def calculate_goal_balance(self):
        self.goal_balance = self.goals_scored - self.goals_lost
        return self.goal_balance

    def result(self, goals_scored, goals_lost):
        if goals_scored > goals_lost:
            self.wins += 1
            return self.wins
        elif goals_scored == goals_lost:
            self.draws += 1
            return self.draws
        else:
            self.losses += 1
            return self.losses

    def print(self):
        return [self.team_name, self.matches, self.wins, self.draws, self.losses,
                self.goals_scored, self.goals_lost, self.goal_balance, self.points]

    def set_ranking(self, rank):
        self.ranking = rank