import turtle
from collections import deque
import time

RADIUS = 100
ANGULAR_SPEED = 5
DOT_SIZE = 5
BLUE = (0, 160/255, 193/255)
YELLOW = (248/255, 237/255, 49/255)
RED = (242/255, 114/255, 124/255)

FPS = 12
TIME_PER_FRAME = 1 / FPS

class MovingData:
    def __init__(self, x):
        self.x = x
        self.y = deque(None for _ in x)
        
    def add(self, item):
        self.y.pop()
        self.y.appendleft(item)
        
    def items(self):
        for x,y in zip(self.x, self.y):
            if y is not None:
                yield x,y

class Trace(turtle.Turtle):
    def __init__(self, color, x_values):
        super().__init__()
        self.color(*color)
        self.pensize(5)
        self.hideturtle()
        self.data = MovingData(x_values)
        
    def add(self, item):
        self.data.add(item)
    
    def draw(self, transf=None):
        transf = transf or (lambda x, y: (x, y))
        self.clear()
        self.penup()
        self.goto(transf(self.data.x[0], self.data.y[0]))
        self.pendown()
        for x, y in self.data.items():
            self.goto(transf(x, y))
            self.dot(5)


def init_turtle_screen():
    window = turtle.Screen()
    window.setup(800, 800)
    window.tracer(0)
    window.bgcolor(50/255, 50/255, 50/255)
    return window

def create_dot(color, position, size=DOT_SIZE):
    dot = turtle.Turtle()
    dot.pensize(size)
    dot.shape("circle")
    dot.color(*color)
    dot.penup()
    dot.setposition(*position)
    return dot


if __name__ == "__main__":
    window = init_turtle_screen()
    main_dot = create_dot(BLUE, (0, -RADIUS))
    main_dot.pendown()
    main_dot.circle(RADIUS)
    main_dot.penup()
    
    vertical_dot = create_dot(YELLOW, (main_dot.xcor() + 2*RADIUS, main_dot.ycor()))
    start_x = int(vertical_dot.xcor())
    vertical_plot = Trace(YELLOW, range(start_x, window.window_width() // 2 + 1))
    vertical_plot.add(vertical_dot.ycor())
    
    horizontal_dot = create_dot(RED, (main_dot.xcor(), main_dot.ycor() - RADIUS))
    start_y = int(horizontal_dot.ycor())
    horizontal_plot = Trace(RED, range(start_y, -window.window_height() // 2 - 1, -1))
    horizontal_plot.add(horizontal_dot.xcor())
    
    while True:
        frame_start = time.time()
        main_dot.circle(RADIUS, ANGULAR_SPEED)
        
        vertical_dot.sety(main_dot.ycor())
        vertical_plot.add(vertical_dot.ycor())
        vertical_plot.draw()
        
        horizontal_dot.setx(main_dot.xcor())
        horizontal_plot.add(horizontal_dot.xcor())
        horizontal_plot.draw(transf=lambda x, y: (y, x))
        
        time.sleep(max(0, TIME_PER_FRAME - (time.time() - frame_start)))
        window.update()

    turtle.done()