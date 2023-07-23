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

vertical_dot = turtle.Turtle()
vertical_dot.shape("circle")
vertical_dot.color(248/255, 237/255, 49/255)
vertical_dot.penup()
vertical_dot.setposition(main_dot.xcor() + 2*RADIUS, main_dot.ycor())

while True:
    main_dot.circle(RADIUS, ANGULAR_SPEED)
    vertical_dot.sety(main_dot.ycor())
    window.update()

turtle.done()