from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.segments = []
        self.make_snake()

    def make_snake(self):
        for cor_position in START_POSITION:
            new_segment = Turtle(shape=self.shape)
            new_segment.color(self.color)
            new_segment.penup()
            new_segment.goto(cor_position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg_num - 1].xcor()
            y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=x_position, y=y_position)

        self.segments[0].forward(MOVE_DISTANCE)
