import turtle

turtle.color("blue")
turtle.begin_fill()


for x in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.end_fill()

turtle.color("red")
turtle.begin_fill()


for x in range(1):
    turtle.left(60)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)


turtle.end_fill()





















turtle.exitonclick()