from turtle import Turtle
MOVE_DISTANCE = 20
POSTIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.num_snake_body = []
        self.create_snake()
        self.head = self.num_snake_body[0]

    def create_snake(self):
        #creating the initial 3 block body of the snake
        for positions in POSTIONS:
            self.add_segment(positions)


    def add_segment(self,positions):
            snake_body = Turtle("square")
            snake_body.penup()
            snake_body.color("white")
            snake_body.goto(positions)
            self.num_snake_body.append(snake_body)
    
    def extend(self):
        self.add_segment(self.num_snake_body[-1].position())

    def move(self):
          #using this loop we can move the blocks in any direction
        for snake_num in range(len(self.num_snake_body)-1,0,-1):
            new_x = self.num_snake_body[snake_num-1].xcor()
            new_y = self.num_snake_body[snake_num-1].ycor()
            self.num_snake_body[snake_num].goto(x = new_x,y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
