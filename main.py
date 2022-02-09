import time
from  turtle import Turtle, Screen
from  player import Player
from cars import Cars
from scoreboard import Scoreboard
screen = Screen()
#screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Road")
screen.tracer(0)

tim = Player()
car = Cars()
lvl = Scoreboard()
gm_over = Scoreboard()

screen.listen()
screen.onkey(tim.move, "Up")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move_car()
    #detect colision with car
    for auto in car.all_cars:
        if tim.distance(auto) < 20:
            game_is_on = False
            gm_over.game_over()
    lvl.update_level()



#detect turtle crossed the road
    if tim.ycor() > 280:
        lvl.level += 1
        car.speed()
        tim.go_to_start()






screen.exitonclick()
