import random

class Game:
    
    def __init__(self):
        self.player_scores = [0, 0]
        self.player_names = ["Player 1", "Player 2"]
    
    def roll_dice(self):
        dice = [random.randint(1, 6) for _ in range(3)]
        return dice
    
    def is_421(self, roll):
        return roll == [4, 2, 1]
    
    def is_pair(self, roll):
        return len(set(roll)) == 1
    
    def is_run(self, roll):
        return sorted(roll) == [1, 2, 3]
    
    def get_score(self, roll):
        if self.is_421(roll):
            return 7
        elif self.is_pair(roll):
            return roll[0] + 2
        elif self.is_run(roll):
            return 6
        else:
            return max(roll)
    
    def play_game(self):
        print("Let's play 421!")
        while True:
            for i, name in enumerate(self.player_names):
                input(f"{name}, press Enter to roll the dice...")
                roll = self.roll_dice()
                score = self.get_score(roll)
                self.player_scores[i] += score
                print(f"{name} rolled {roll} and scored {score} points. Total score: {self.player_scores[i]}")
                if self.player_scores[i] >= 10:
                    print(f"{name} wins!")
                    return

class combinaison:
    
    def combinaison(self):
        self.n1 = "421"
        self.n2 = "3 as"
        self.n3 = "2 as-six"
        self.n4 = "3 six"
        self.n5 = "2 as-cinq"
        self.n6 = "3 cinq"
        self.n7 = "2 as - quatre"
        self.n8 = "3 Quatre"
        self.n9 = "2 As – Trois"
        self.n10 = "3 Trois"
        self.n11 = "2 As – Deux"
        self.n12 = "3 Deux"
        self.n13 = "Six – Cinq – Quatre"
        self.n14 = "Cinq – Quatre – Trois"
        self.n15 = "Quatre – Trois – Deux"
        self.n16 = "Trois – Deux – As"
    
class pot:
    
    def pot(self):
        
        

game = Game()
game.play_game()

        
