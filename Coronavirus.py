from turtle import *

wn = Screen()
bgcolor("black")

covid = Turtle()
pensize(2)
speed(0)
penup()
goto(0, 200)
pendown()

b = 0

for b in range(200):
    if b <= 150:
        color("red")
        right(b)
        forward(b*3)
    else:
        color("red")
        right(b)
        forward(b*3)
hideturtle()
wn.mainloop()
