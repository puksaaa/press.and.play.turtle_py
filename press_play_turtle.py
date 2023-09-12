from turtle import*
from random import*

t1 =Turtle()
t1.shape('turtle')
t1.color('red')
t1.pensize(5)
t1.penup()
t1.goto(-190,90)
t1.pendown()

t2 = Turtle()
t2.shape('turtle')
t2.color('blue')
t2.pensize(5)
t2.penup()
t2.goto(-190,-90)
t2.pendown()

while t1.xcor() and t2.xcor()<160:
    t1.forward(randint(10,150))
    t2.forward(randint(10,150))

if t1.xcor() > t2.xcor():
    t1.penup()
    t1.goto(0,0)
    t1.pendown()
    t1.write('Я выиграл!' , font= ('Arial' , 14 , 'normal'))
    t1.hideturtle()
elif t2.xcor() > t1.xcor():
    t2.penup()
    t2.goto(0,0)
    t2.pendown()
    t2.write('Я выиграл!' , font=('Arial' , 14 , 'normal'))
    t2.hideturtle()
