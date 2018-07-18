import turtle
t= turtle.Turtle()
t.shape("turtle")

radius = int(input("집의 한 변의 크기는 얼마로 할까요?"))

t.forward(radius)
t.right(90)
t.forward(radius)
t.right(90)
t.forward(radius)
t.right(90)
t.forward(radius)
t.right(90)

t.forward(radius)
t.left(120)
t.forward(radius)
t.left(120)
t.forward(radius)
t.left(120)