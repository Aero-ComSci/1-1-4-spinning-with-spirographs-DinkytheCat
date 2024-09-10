import turtle as t
t.speed(0)
t.pensize(10)
t.goto(0,0)
t.bgcolor('black')
blah = 0
def square():
    size = 4
    for i in range(6):
        for color in ('red','blue','green','purple'):#, 'cyan', 'green', 'white','yellow'):
            t.color(color)
            for i in range(4):
                t.forward(size)
                t.right(90)

            size += 18
for i in range(4):
    t.setheading(0+blah)
    square()
    t.penup
    t.goto(0,0)
    t.pendown
    blah +=90
t.done()
