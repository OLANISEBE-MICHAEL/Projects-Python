from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        """gets all the segments of the snake in the starting position"""
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        """adds the segment one by one to the snake"""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        # list.clear() is used to remove all the elements in a list
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_segments(self, num):
        """used to extend the snake's body as it eats more food"""
        # position() is used to get the turtle current location on the graph
        for _ in range(num):
            self.add_segments(self.segments[-1].position())


    def move(self):
        """a simple logic allowing the snake to move"""
        for seg_index in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_index - 1].xcor()
            y_cor = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(x_cor, y_cor)
        self.head.forward(20)


    def face_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def face_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def face_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def face_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


