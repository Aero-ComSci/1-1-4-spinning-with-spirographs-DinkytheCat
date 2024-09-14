import turtle as t
t.speed(0)
t.pensize(1)
t.goto(0,0)
t.bgcolor('black')
blah = 0
def square():
    size = 4
    for i in range(4):
    
        for color in ('white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white','white'):

            t.color(color)
            for i in range(4):
                t.forward(size)
                t.right(90)

            size += 5
for i in range(4):
    t.setheading(0+blah)
    square()
    t.penup
    t.goto(0,0)
    t.pendown
    blah +=90
t.done()
