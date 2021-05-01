from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape(name="turtle")

# for _ in range(4):
#     tim.forward(150)
#     tim.right(90)

# tim.pensize(width=3)
# for _ in range(20):
#     tim.pendown()
#     tim.forward(8)
#     tim.penup()
#     tim.forward(8)
colors = ["red","green","blue","orange","purple","pink","yellow","gold","cyan2","aquamarine","cornflowerblue","lavenderblush3",'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2']

# for measure in range(3, 11):
#     color = random.choice(colors)
#     angle = 360 // measure
#     tim.color(color)    
#     for travel in range(0, measure):
#         tim.forward(100)
#         tim.right(angle)

directions = [0, 90, 180, 270]
tim.pensize(width=6)
for _ in range(100):    
    color = random.choice(colors)
    tim.color(color)  
    tim.setheading(random.choice(directions))
    tim.forward(20)

screen = Screen()
screen.exitonclick()






