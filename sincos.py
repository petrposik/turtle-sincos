import turtle

RADIUS = 100

window = turtle.Screen()
window.bgcolor(50/255, 50/255, 50/255)

main_dot = turtle.Turtle()
main_dot.pensize(5)
main_dot.shape("circle")
main_dot.color(0, 160/255, 193/255)
main_dot.penup()
main_dot.setposition(0, -RADIUS)
main_dot.pendown()

turtle.done()