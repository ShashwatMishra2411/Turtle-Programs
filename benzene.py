import turtle

sc = turtle.Screen()
sc.bgcolor("black")
sc.title("Kachua OP")
benzi = turtle.Turtle()
d = 0
rainbow = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
benzi.speed(0)

for i in range(360):
    benzi.color(rainbow[i % 7])

    benzi.fd(d + i)
    benzi.left(59)

sc.mainloop()

