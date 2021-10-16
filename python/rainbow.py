import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'white', 'maroon', 'navy', 'aqua']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%10])
    t.width(x/100 +1)
    t.forward(x)
    t.left(59)