import time
from turtle import Screen
from player import Player
from carmanager import CarManager

from scoreboard import  Scoreboard
# screen setup
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)

#Objects
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move_up, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)

    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

# Detect collision

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            is_game_on = False
            scoreboard.game_over()
# Crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
