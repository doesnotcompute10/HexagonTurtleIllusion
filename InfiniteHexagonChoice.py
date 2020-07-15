import turtle

loop=200
turtle.speed(20000)
turtle.showturtle()
for i in range(0,68):
    for j in range(0, 3):
        turtle.forward(loop)
        turtle.right(60)
    turtle.forward(10)
    turtle.right(1)
    loop = loop-3
turtle.penup()
turtle.home()
turtle.pendown()
loop=200
for i in range(0,68):
    for j in range(0, 3):
        turtle.forward(loop)
        turtle.left(60)
    turtle.forward(10)
    turtle.left(1)
    loop = loop-3

turtle.penup()
turtle.home()
turtle.left(120)
loop=200
turtle.forward(1)
turtle.left(90)
turtle.forward(1)
turtle.right(90)
turtle.pendown()
for i in range(0,68):
    for j in range(0, 3):
        turtle.forward(loop)
        turtle.left(60)
    turtle.forward(10)
    turtle.left(1)
    loop = loop-3

turtle.hideturtle()


