from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboarch
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

pd1 = Paddle((350, 0))
pd2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboarch()


screen.listen()
screen.onkey(pd1.go_up,"Up")
screen.onkey(pd1.go_down,"Down")

screen.onkey(pd2.go_up,"w")
screen.onkey(pd2.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(pd1) < 50 and ball.xcor() > 320 or ball.distance(pd2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()