from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal') 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()    
        self.score = 0
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    
    def update_scoreboard(self):
        """Update the score of the player"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        """Write game over in the screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


    def increse_score(self):
        """Increse the score of the player"""
        self.score += 1
        self.clear()
        self.update_scoreboard()