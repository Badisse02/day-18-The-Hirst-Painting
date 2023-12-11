# import colorgram
from random import *
import turtle
from turtle import *
tur = Turtle()
screen = Screen()

turtle.colormode(255)

#
#
# def tuple_color(col):
#     colors_list = []
#     for i in range(len(col)):
#         red = col[i].rgb.r
#         green = col[i].rgb.g
#         blue = col[i].rgb.b
#         colors_list.append((red, green, blue))
#     return colors_list
#
#
# colors = colorgram.extract('6a00e54ecc669788330133f50c243e970b.jpg', 36)
rdg_colors = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171),
              (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86),
              (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225),
              (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145),
              (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52), (179, 199, 184), (133, 41, 39),
              (76, 63, 49), (38, 79, 82)]
tur.speed("fastest")
tur.penup()
tur.hideturtle()
tur.setpos(-300, -200)
for _ in range(10):
    for _ in range(10):
        tur.dot(20, choice(rdg_colors))
        tur.forward(10)
        tur.forward(50)
    tur.left(90)
    tur.forward(50)
    tur.right(90)
    tur.forward(-600)

screen.exitonclick()
