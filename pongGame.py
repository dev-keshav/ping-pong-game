import os
import turtle as tu

# for score
playerAscore = 0
playerBscore = 0

window = tu.Screen()     # for creating a window
window.title("Multiplayer Ping-Pong Game")    # giving the name
window.bgcolor("grey")   # color for the screen
# screen speed
window.setup(width=800, height=600)   # size of the pannel
window.tracer(10)    # speed up the game

# Creating left paddle
leftpaddle = tu.Turtle()
leftpaddle.speed(0)
leftpaddle.color("brown")
leftpaddle.shape("square")
leftpaddle.shapesize(stretch_wid=7, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating right paddle
rightpaddle = tu.Turtle()
rightpaddle.speed(0)
rightpaddle.color("brown")
rightpaddle.shape("square")
rightpaddle.shapesize(stretch_wid=7, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Creating ball
ball = tu.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ballxdirection = 1.5
ballydirection = 1.5

# Creating pen for score card update
pen = tu.Turtle()
pen.speed(0)
pen.color("skyblue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))


# Moving the left paddle in up
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 15
    leftpaddle.sety(y)


# Moving the lefttpaddle in down
def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 15
    leftpaddle.sety(y)


# Moving the rightpaddle in up
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 15
    rightpaddle.sety(y)


# Moving the righttpaddle in down
def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 15
    rightpaddle.sety(y)


# Assign the key to play

window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# Game loop
while True:
    window.update()

    # Moving the ball
    # ball.setx(ball.xcor() + ballxdirection)
    # ball.sety(ball.ycor() + ballydirection)

    ball.setx(ball.xcor() + (ballxdirection / 3))
    ball.sety(ball.ycor() + (ballydirection / 3))

    # Setting-up border
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A:{}   Player B:{}".format(playerAscore, playerBscore), align='center',
                  font=('Arial', 24, 'normal'))
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A:{}   Player B:{}".format(playerAscore, playerBscore), align='center',
                    font=('Arial', 24, 'normal'))
        os.system("afplay wallhit.wav&")

    # Handiling the collision

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wave&")
