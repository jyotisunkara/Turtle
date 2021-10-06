import turtle
WIDTH, HEIGHT = 1000, 1000

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  
screen.bgcolor("#fdc477")

t = turtle.Turtle()


t.pensize(5)
t.speed(10)


# ears
t.pencolor("#c88b52")
t.fillcolor("#c88b52")
t.penup()
t.goto(-150, 350)
t.pendown()

t.begin_fill()
t.setheading(170)
t.forward(60)
t.setheading(200)
t.circle(200, 85)
t.setheading(250)
t.circle(95, -55)
t.setheading(65)
t.forward(135)
t.setheading(38)
t.forward(79)
t.end_fill()

t.penup()
t.goto(150, 350)
t.pendown()

t.begin_fill()
t.setheading(180 - 170)
t.forward(60)
t.setheading(360 - 200)
t.circle(200, -85)
t.setheading(360 - 250)
t.circle(95, 55)
t.setheading(180 - 65)
t.forward(135)
t.setheading(180 - 38)
t.forward(79)
t.end_fill()

# patch
t.pencolor("#4e341d")
t.fillcolor("#4e341d")
t.penup()
t.goto(0, 0)
t.pendown()

t.begin_fill()
t.setheading(0)
t.circle(80, -45)
t.setheading(135)
t.circle(15, 135)
t.setheading(95)
t.circle(110, -85)
t.setheading(190)
t.circle(10, 90)
t.setheading(265)
t.circle(102.5, 145)

t.setheading(310)
t.circle(102.5, 145)
t.setheading(80)
t.circle(10, 90)
t.setheading(345)
t.circle(110, -85)
t.setheading(90)
t.circle(15, 167)
t.setheading(45)
t.circle(80, -46)
t.end_fill()

# eyes
t.pencolor("#1a1c1b")
t.fillcolor("#1a1c1b")
t.penup()
t.goto(-220, 10)
t.pendown()

t.begin_fill()
t.setheading(35)
t.forward(125)
t.setheading(140)
t.circle(35, -190)
t.setheading(23)
t.backward(60)
t.end_fill()

t.penup()
t.goto(220, 10)
t.pendown()

t.begin_fill()
t.setheading(180 - 35)
t.forward(125)
t.setheading(360 - 140)
t.circle(35, 190)
t.setheading(180 - 23)
t.backward(60)
t.end_fill()


# nose
t.penup()
t.goto(55, -125)
t.pendown()

t.begin_fill()
t.setheading(135)
t.circle(75, 90)
t.setheading(315)
t.circle(75,90)
t.end_fill()



turtle.done()