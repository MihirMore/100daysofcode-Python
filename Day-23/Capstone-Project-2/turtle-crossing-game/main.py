import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.turtle_up, "Up")
screen.bgcolor("black")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Detect turtle collision with screen at other end
    if player.is_player_at_finish():
        player.reset_turtle()
        score.update_score()
        car.move_faster()
    car.create_car()
    car.move_car()

    # Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()            