from turtle import Turtle
import random

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.refresh()
        
    
    def refresh(self):
        """Refresh the location of the food in the screen"""
        random_x = random.randint(-385, 385)
        random_y = random.randint(-285, 285)
        self.goto(random_x, random_y)
