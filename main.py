from turtle import Turtle, Screen #importing the required modules
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
'''
Note: the size of turtle is 20x20

'''
screen = Screen()
screen.title("Snake Game") #Game title 
screen.setup(width = 600, height=600) #Game window size
screen.bgcolor("black") #background color is black
screen.tracer(0)

snake = Snake()
snake.create_snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")




#game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()
        scoreboard.score_update()
    #collision with wall
    if (int(snake.head.xcor())) > 280 or (int(snake.head.xcor())) < -280 or (int(snake.head.ycor())) > 280 or (int(snake.head.ycor()))< -280:
        game_is_on = False
        scoreboard.game_over()

    #collision with itself
    for body in snake.num_snake_body[1:]:
        if snake.head.distance(body)<10:
            game_is_on=False
            scoreboard.game_over()
        
    
    

    
    
    
        

        
        
        














screen.exitonclick() #the screen will only exit on clicking
