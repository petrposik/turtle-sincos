import turtle

RADIUS = 100
ANGULAR_SPEED = 1

window = turtle.Screen()
window.tracer(0)
window.bgcolor(50/255, 50/255, 50/255)

main_dot = turtle.Turtle()
main_dot.pensize(5)
main_dot.shape("circle")
main_dot.color(0, 160/255, 193/255)
main_dot.penup()
main_dot.setposition(0, -RADIUS)
main_dot.pendown()

while True:
    main_dot.circle(RADIUS, ANGULAR_SPEED)
    window.update()

turtle.done()