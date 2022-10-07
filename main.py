import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

COLLISION_DISTANCE = 22

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

scoreboard = Scoreboard()

player = Player()

car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "space")

# Gameplay
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect car collision
    for car in car_manager.all_cars:
        if car.distance(player.xcor(), player.ycor()) < COLLISION_DISTANCE:
            scoreboard.game_over()
            game_is_on = False

    # Level up
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.update_level()
        car_manager.cars_speed_up()
        player.player_reset()

screen.exitonclick()
