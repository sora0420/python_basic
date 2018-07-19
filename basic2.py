int1 = int(input("첫 번째 숫자를 입력하시오 : "))
int2 = int(input("두 번째 숫자를 입력하시오 : "))
int3 = int(input("세 번째 숫자를 입력하시오 : "))
sum=int1+int2+int3
print(int1,int2,int3,"의 평균은",sum/3,"입니다.")


import math
math.pi
import math as m #m으로 치환 / 라이브러리에 들어가서 함수확인
radius = int(input("반지름을 입력하시오 : "))
print("반지름이",radius,"인 원의 넓이",radius*radius*m.pi)


import turtle
t=turtle.Pen()
t.shape("turtle")

radius =50
t.up()
t.goto(0,0)
t.down()
t.circle(radius)
radius =70
t.up()
t.goto(100,0)
t.down()
t.circle(radius)
radius =90
t.up()
t.goto(200,0)
t.down()
t.circle(radius)



import turtle
t=turtle.Turtle()
t.shape("turtle")
side = 100
angle = 90
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)

t.forward(100)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)

t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)