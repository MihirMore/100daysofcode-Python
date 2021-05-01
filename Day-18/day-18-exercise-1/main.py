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
colors = ["red","green","blue","orange","purple","pink","yellow","gold","cyan2","aquamarine","cornflowerblue","lavenderblush3"]

for measure in range(3, 11):
    color = random.choice(colors)
    angle = 360 // measure
    tim.color(color)    
    for travel in range(0, measure):
        tim.forward(100)
        tim.right(angle)
        
tim.pensize(width=6)
for _ in range(100):
    direction = random.randint(1, 271)
    color = random.choice(colors)
    tim.color(color)  
    tim.setheading(direction)
    tim.forward(20)



screen = Screen()
screen.exitonclick()






