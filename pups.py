import turtle
WIDTH, HEIGHT = 1000, 1000

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.bgcolor("#cdd1cf")
t = turtle.Turtle()


t.pensize(5)
t.speed(10)
# ears
t.pencolor("#a97f83")
t.fillcolor("#a97f83")
t.penup()
t.goto(-150, 150)
t.pendown()
x = 130
y = 240
z = 225
w = 245
t.begin_fill()
t.setheading(x)
t.forward(150)
t.setheading(y)
t.circle(200, 45)
t.forward(30)
t.setheading(z)
t.circle(30, 130)
t.setheading(w)
t.circle(300, -28.5)
t.end_fill()


t.penup()
t.goto(150, 150)
t.pendown()

t.begin_fill()
t.setheading(180 - x)
t.forward(150)
t.setheading(360 - y)
t.circle(200, -45)
t.forward(-30)
t.setheading(360 - z)
t.circle(30, -130)
t.setheading(360 - w)
t.circle(300, 28.5)
t.end_fill()

# patch
t.pencolor("#42311d")
t.fillcolor("#42311d")
t.penup()
t.goto(50, 119)
t.pendown()
t.begin_fill()

t.setheading(270)
t.forward(199)
t.circle(85, 180)
t.circle(200, 81)
t.end_fill()

# eyes
t.pencolor("#1a1c1b")
t.fillcolor("#1a1c1b")
t.penup()
t.goto(-80, -75)
t.pendown()
x = 120
y = 300
t.begin_fill()
t.setheading(x)
t.circle(70, 75)
t.setheading(y)
t.circle(70, 75)
t.end_fill()

t.penup()
t.goto(80, -75)
t.pendown()

t.begin_fill()
t.setheading(-x)
t.circle(70, -75)
t.setheading(-y)
t.circle(70, -75)
t.end_fill()


# nose
t.penup()
t.goto(70, -370)
t.pendown()

t.begin_fill()
t.setheading(180)
t.forward(140)
t.setheading(275)
t.circle(50, 70)
t.setheading(0)
t.forward(63)
t.setheading(10)
t.circle(50, 70)
t.end_fill()



turtle.done()