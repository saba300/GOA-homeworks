from turtle import *
speed(100)
bgcolor('blue')

#castle

penup()
goto(-500, -500)
pendown()
color('gray')
begin_fill()
forward(1000)
left(90)
forward(500)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(200)
right(90)
forward(500)
right(90)
forward(200)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(500)
end_fill()

penup()
goto(150, -500)
right(180)
color('brown')
begin_fill()
forward(200)
left(90)
forward(300)
left(90)
forward(200)
end_fill()
pensize(10)
pencolor('black')
left(180)
forward(200)
right(90)
forward(300)
right(90)
forward(200)
penup()
goto(-500, -150)
pendown()
color('black')
begin_fill()
left(90)
forward(75)
right(90)
forward(50)
right(90)
forward(75)
right(90)
forward(50)
end_fill()

penup()
goto(-500, -500)
pendown()
color('black')
begin_fill()
right(90)
forward(1000)
left(90)
forward(500)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(200)
right(90)
forward(500)
right(90)
forward(200)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(500)

penup()
goto(350, -350)
color('black')
begin_fill()
left(90)
forward(75)
right(90)
forward(50)
right(90)
forward(75)
right(90)
forward(50)
end_fill()

penup()
goto(-125, -200)
pendown()
color('gray')
begin_fill()
pencolor('black')
forward(400)
right(90)
forward(250)
right(90)
forward(400)
end_fill()
penup()
goto(-150, 200)
pendown()
color('black')
begin_fill()
left(90)
forward(300)
left(120)
forward(300)
left(120)
forward(300)
end_fill()

penup()
goto(-50, 100)
pendown()
color('black')
begin_fill()
left(30)
forward(150)
left(90)
forward(100)
left(90)
forward(150)
penup()
goto(50, 100)
pendown()
circle(50)
end_fill()


#flag

penup()
goto(-375, 0)
pendown()
color('black')
begin_fill()

forward(200)
right(90)
forward(150)
right(90)
forward(75)
right(90)
forward(150)
end_fill()

#G

pencolor('white')
penup()
goto(-360, 150)
pendown()
right(90)
forward(30)
right(90)
forward(20)
penup()
goto(-360, 150)
pendown()
forward(20)
left(90)
forward(15)
left(90)
forward(10)

#O

pencolor('white')
penup()
goto(-310, 150)
pendown()
right(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)

#A

pencolor('white')
penup()
goto(-270, 150)
pendown()
left(240)
forward(30)
right(135)
forward(30)
penup()
goto(245,660)
pendown()
right(120)
forward(30)

#queen
left(30)
pencolor('black')
penup()
goto(-230, -200)
pendown()
right(135)
forward(30)
right(105)
forward(30)
penup()
goto(-215, -175)
pendown()
right(220)
forward(40)
left(90)
left(180)
circle(20)

penup()
goto(-230, -155)
pendown()
forward(30)

pencolor('yellow')
penup()
goto(-230, -95)
pendown()
begin_fill()
forward(30)
left(90)
forward(20)
left(130)
forward(10)
right(90)
forward(10)
left(90)
forward(10)
right(90)
forward(10)
left(130)
forward(20)
end_fill()

pencolor('red')
right(30)
forward(30)
penup()
goto(-210, -95)
pendown()
left(90)
forward(30)

#king
pencolor('black')
penup()
goto(200, -200)
pendown()
left(80)
forward(30)
right(90)
forward(30)
penup()
goto(220, -180)
pendown()
left(135)
forward(60)

right(75)
circle(20)

penup()
goto(200, -150)
pendown()
right(20)
forward(40)
penup()
goto(195, -80)
pendown()
pencolor('yellow')
left(7)
forward(40)
left(90)
forward(30)
left(110)
forward(15)
right(90)
forward(15)
left(130)
forward(15)
right(90)
forward(15)
left(115)
forward(30)
screensize(1000, 1000)
exitonclick()