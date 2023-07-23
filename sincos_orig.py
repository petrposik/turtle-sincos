import collections
import time
import turtle

radius = 100
angular_speed = 2

fps = 12  # Frames per second
time_per_frame = 1 / fps

window = turtle.Screen()
window.setup(1000, 1000)
window.tracer(0)
window.bgcolor(50 / 255, 50 / 255, 50 / 255)

main_dot = turtle.Turtle()
main_dot.pensize(5)
main_dot.shape("circle")
main_dot.color(0, 160 / 255, 193 / 255)
main_dot.penup()
main_dot.setposition(0, -radius)
main_dot.pendown()

vertical_dot = turtle.Turtle()
vertical_dot.shape("circle")
vertical_dot.color(248 / 255, 237 / 255, 49 / 255)
vertical_dot.penup()
vertical_dot.setposition(
    main_dot.xcor() + 2 * radius,
    main_dot.ycor(),
)

vertical_plot = vertical_dot.clone()
vertical_plot.hideturtle()
start_x = int(vertical_plot.xcor())
# Get range of x-values from position of dot to edge of screen
x_range = range(start_x, window.window_width() // 2 + 1)
# Create a list to store the y-values to draw at each
# point in x_range.
vertical_values = collections.deque(None for _ in x_range)
# You can populate the first item in this list
# with the dot's starting height
vertical_values[0] = vertical_plot.ycor()

horizontal_dot = turtle.Turtle()
horizontal_dot.shape("circle")
horizontal_dot.color(242 / 255, 114 / 255, 124 / 255)
horizontal_dot.penup()
horizontal_dot.setposition(
    main_dot.xcor(),
    main_dot.ycor() - radius,
)

horizontal_plot = horizontal_dot.clone()
horizontal_plot.hideturtle()
start_y = int(horizontal_plot.ycor())
y_range = range(start_y, -window.window_height() // 2 - 1, -1)
horizontal_values = collections.deque(None for _ in y_range)
horizontal_values[0] = horizontal_plot.xcor()

while True:
    frame_start = time.time()
    main_dot.circle(radius, angular_speed)

    vertical_dot.sety(main_dot.ycor())
    vertical_plot.clear()
    # Add new value at the start, and delete last value
    vertical_values.appendleft(vertical_dot.ycor())
    vertical_values.pop()
    # Plot all the y-values
    for x, y in zip(x_range, vertical_values):
        if y is not None:
            vertical_plot.setposition(x, y)
            vertical_plot.dot(5)

    horizontal_dot.setx(main_dot.xcor())
    horizontal_plot.clear()
    horizontal_values.appendleft(horizontal_dot.xcor())
    horizontal_values.pop()
    for x, y in zip(horizontal_values, y_range):
        if x is not None:
            horizontal_plot.setposition(x, y)
            horizontal_plot.dot(5)

    # Wait until minimum frame time reached
    while time.time() - frame_start < time_per_frame:
        pass
    window.update()