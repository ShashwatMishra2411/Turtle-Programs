import turtle

bat = turtle.Turtle()


bat.pensize(3)

wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Batman logo")

bat.color("yellow", "black")
bat.speed(6)

bat.begin_fill()

# turn 1
bat.left(90)
bat.circle(50, 85)
bat.circle(15, 110)
bat.right(180)


# turn 2
bat.circle(30, 150)
bat.right(5)
bat.forward(10)

# turn 3
bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)

#turn 4
bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

#turn 5
bat.forward(30)
bat.left(55)
bat.forward(10)

#reverse

#turn 5
bat.forward(10)
bat.left(55)
bat.forward(30)

#turn 4
bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)

#turn 3
bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)

#turn 2
bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)

#turn 1
bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)

#end color filling
bat.end_fill()


bat.hideturtle()
wn.mainloop()
