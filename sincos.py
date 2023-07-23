import turtle

RADIUS = 100
ANGULAR_SPEED = 1
DOT_SIZE = 5
BLUE = (0, 160/255, 193/255)
YELLOW = (248/255, 237/255, 49/255)

def init_turtle_screen():
    window = turtle.Screen()
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
    vertical_dot = create_dot(YELLOW, (main_dot.xcor() + 2*RADIUS, main_dot.ycor()))
    while True:
        main_dot.circle(RADIUS, ANGULAR_SPEED)
        vertical_dot.sety(main_dot.ycor())
        window.update()

    turtle.done()