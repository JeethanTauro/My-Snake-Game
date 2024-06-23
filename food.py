from turtle import Turtle
import random

# the food class inherits from turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5) #reduce the size of food
        self.color("red")
        self.speed("fastest")
        
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(x=random_x,y=random_y)



