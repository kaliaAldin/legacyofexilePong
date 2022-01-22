#simple pong tutorial

import turtle

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



#PadlleA
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#PAddleB

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.5
ball.dy = -0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
while True:
    wn.update()

    #Move ball
    new_ballx = ball.xcor() + ball.dx
    ball.setx(new_ballx)
    new_bally = ball.ycor() + ball.dy
    ball.sety(new_bally)

    #Borderchecking
    if ball.ycor() > 290:
         ball.sety(290)
         ball.dy = ball.dy * -1

    if ball.ycor() < -290:
         ball.sety(-290)
         ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1


    #Baddle and ball collision
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx = ball.dx * -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx = ball.dx * -1
