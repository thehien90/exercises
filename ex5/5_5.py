from turtle import*
def draw_star(x,y,length):
    x = float(x)
    y = float(y)
    length = float(length)
    penup()
    setposition(x,y)
    pendown()
    left(72)
    forward(length)
    for i in range(4):
        right(144)
        forward(length)
    left(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
