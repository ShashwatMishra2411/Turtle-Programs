import turtle
from turtle import *

sc = Screen()
title("YouTube")
bgcolor("white")

penup()
goto(-200, -150)
pensize(10)
color("red")
speed(0)

# back
begin_fill()
pendown()
fd(400)
circle(60, 90)
fd(200)
circle(60, 90)
fd(400)
circle(60, 90)
fd(200)
circle(60, 90)
end_fill()

# Front

penup()
color("white")

goto(-40, -70)
pendown()
begin_fill()
left(30)
fd(150)
left(120)
fd(150)
left(120)
fd(150)
left(120)
end_fill()

hideturtle()
sc.mainloop()
