from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-11, 0), (-22, 0)]
MOVE_DISTANCE = 11
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() 
        self.head = self.segments[0]
        self.move_speed = 0.1
    
    def create_snake(self):
        """Create the snake basead in the number of positions you in the constant STARTING_POSITIONS"""
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        """Add segments to the snake"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.shapesize(stretch_wid=0.5)
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        """Add a new segment to the snake"""
        self.add_segments(self.segments[-1].position())
        self.move_speed *= 0.9


    def move(self):
        """Move the snake forward basead in her heading"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    
    def up(self):
        """Set the heading of the snake UP"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        """Set the heading of the snake DOWN"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        """Set the heading of the snake LEFT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        """Set the heading of the snake RIGHT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)