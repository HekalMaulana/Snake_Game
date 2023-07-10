from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_HEADING = 90
LEFT_HEADING = 180
RIGHT_HEADING = 0
DOWN_HEADING = 270
SHAPE = "square"
COLOR = 'WHITE'


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for cor_position in START_POSITION:
            self.create_snake(cor_position)

        self.segments[0].shape("triangle")
        self.segments[0].color("red")

    def create_snake(self, cor_position):
        new_segment = Turtle(shape=SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(cor_position)
        self.segments.append(new_segment)

    def extend(self):
        self.create_snake(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg_num - 1].xcor()
            y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=x_position, y=y_position)

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN_HEADING:
            self.head.setheading(UP_HEADING)

    def down(self):
        if self.head.heading() != UP_HEADING:
            self.head.setheading(DOWN_HEADING)

    def left(self):
        if self.head.heading() != RIGHT_HEADING:
            self.head.setheading(LEFT_HEADING)

    def right(self):
        if self.head.heading() != LEFT_HEADING:
            self.head.setheading(RIGHT_HEADING)
