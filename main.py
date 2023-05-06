from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)


snake = Snake()
food = Food()
score= Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


if screen.onkey(snake.space,"space"):
    pass
elif screen.onkey(snake.unpause,"a"):
    snake.move()






game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    
    snake.move()

    #detect the collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        


    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        
        score.reset()
        time.sleep(4)
        snake.reset()

    #detect collision with tail.

    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment)<10:
            
            score.reset()
            time.sleep(4)
            snake.reset()





screen.exitonclick()