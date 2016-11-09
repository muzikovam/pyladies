from turtle import forward, left, right, speed, exitonclick, width,shape

width(4)
shape("arrow")
speed(1)

for i in range(3):
    for j in range(4):
        forward(50)
        left(90)
    left(20)

exitonclick()
