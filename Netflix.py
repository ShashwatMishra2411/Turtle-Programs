import turtle

bat = turtle.Turtle()
bat.hideturtle()
bat.penup()
bat.goto(-250, -285)
bat.pendown()
bat.pensize(3)
bat.speed(0)

wn = turtle.Screen()
wn.bgcolor("dark blue")
wn.title("NETFLIX And CHill ")

bat.color("red", "black")

bat.begin_fill()

# background
bat.forward(500)
bat.circle(40, 90)
bat.forward(500)
bat.circle(40, 90)
bat.fd(500)
bat.circle(40, 90)
bat.fd(500)
bat.circle(40, 90)

bat.end_fill()

# logo
bat.penup()
bat.goto(-150, - 200)
bat.pendown()

# left side
bat.color("dark red", "red")
bat.begin_fill()
bat.forward(100)
bat.left(90)
bat.forward(400)
bat.left(90)
bat.forward(100)
bat.left(90)
bat.forward(400)
bat.left(90)
bat.forward(100)
bat.left(90)
bat.forward(400)
bat.right(150)
bat.end_fill()

# center

bat.color("dark red", "red")
bat.begin_fill()
bat.forward(463)
bat.left(60)
bat.right(180)
bat.fd(100)
bat.right(60)
bat.forward(463)
bat.right(120)
bat.fd(100)
bat.right(60)
bat.forward(464)
bat.left(150)
bat.end_fill()

# Right

bat.color("dark red", "red")
bat.begin_fill()
bat.forward(400)
bat.left(90)
bat.forward(100)
bat.left(90)
bat.forward(400)
bat.left(90)
bat.forward(100)
bat.left(90)
bat.forward(400)
bat.end_fill()


wn.mainloop()
