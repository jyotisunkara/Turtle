import turtle
WIDTH, HEIGHT = 1000, 1000

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  
screen.bgcolor("#d2a470")

t = turtle.Turtle()


t.pensize(5)
t.speed(10)


# ears
t.pencolor("#deb4b5")
t.fillcolor("#deb4b5")
t.penup()
t.goto(-150, 170)
t.pendown()
t.begin_fill()
t.setheading(100)
t.circle(600, 30)
t.circle(60, 135)
t.setheading(260)
t.circle(700, 40)
t.setheading(270)
t.circle(235, -70)
t.end_fill()

t.penup()
t.goto(150, 170)
t.pendown()
t.begin_fill()
t.setheading(260)
t.circle(600, -30)
t.circle(60, -135)
t.setheading(100)
t.circle(700, -40)
t.setheading(90)
t.circle(235, 70)
t.end_fill()

# patch
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(40, 100)
t.pendown()

t.begin_fill()
t.setheading(90)
t.circle(40,180)

t.forward(200)

t.setheading(90)
t.circle(400,-25)

t.setheading(245)
t.circle(300,10)

t.setheading(270)
t.circle(90, 180)

t.setheading(95)
t.circle(300,10)

t.setheading(295)
t.circle(400,-25)
t.setheading(270)
t.backward(200)
t.end_fill()


# eyes
t.pencolor("#35332f")
t.fillcolor("#35332f")

t.penup()
t.goto(-110, -50)
t.pendown()

t.begin_fill()
t.setheading(135)
t.circle(70, 100)
t.setheading(300)
t.circle(60, 126)
t.end_fill()

t.penup()
t.goto(110, -50)
t.pendown()

t.begin_fill()
t.setheading(180 + 45)
t.circle(70, -100)
t.setheading(60)
t.circle(60, -126)
t.end_fill()

# nose
t.penup()
t.goto(50, -300)
t.pendown()

t.begin_fill()
t.setheading(180)
t.forward(100)
t.setheading(275)
t.circle(50, 70)
t.setheading(0)
t.forward(22)
t.setheading(10)
t.circle(50, 70)
t.end_fill()

turtle.done()