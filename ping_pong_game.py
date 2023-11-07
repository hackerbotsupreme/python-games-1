# simple pong  game in python
# by our amazing @hackeraloke

# getting started
# first what we wanna do is  to  steup the screen ogf the game
import turtle

wn = turtle.Screen()  # summoning  a  window for the game from the built-in module
wn.title("Pong by Aloke pramanik ")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

# now for the next step we will add our paddel on the right and paddel on the left and our ball at the centre


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape(
    "square"
)  # notice that we have not given the size yet so by default it is 20 by 20 pixels that means 20 pixels wide by 20 pixels high
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape(
    "square"
)  # notice that we have not given the size yet so by default it is 20 by 20 pixels that means 20 pixels wide by 20 pixels high
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350, 0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape(
    "circle"
)  # notice that we have not given the size yet so by default it is 20 by 20 pixels that means 20 pixels wide by 20 pixels high
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25  # what does this mean is everytime the ball moves in x axis it moves 0.25 pixels in the positive x direction
ball.dy = (
    -0.25
)  # and ehat does this means is everytume the ball moves  in y axis it moves  0.25 pixels in the positive y direction


# functions
# settting up to move up and down  when we command through keyboard
# padde_a  up and down
# keyboard binding
def paddle_a_up():
    y = paddle_a.ycor()  # here y cor returns the y co-ordinate
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # here y cor returns the y co-ordinate
    y -= 20
    paddle_a.sety(y)


# and for paddle_b
def paddle_b_up():
    y = paddle_b.ycor()  # here y cor returns the y co-ordinate
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # here y cor returns the y co-ordinate
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")  # paddke_a up
wn.onkeypress(paddle_a_down, "s")  # paddle_a down
wn.onkeypress(paddle_b_up, "o")  # paddle_b up
wn.onkeypress(paddle_b_down, "k")  # paddle_b down


# main game loop
while True:
    wn.update()  # what this does is  every time the loop runs(the condition beconmes true ) it updates the screen

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # it reverses the direction
    # border checking
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # it reverses the direction
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # paddle and ball collisin detection
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1
