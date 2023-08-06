# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new = (r, g, b)
#     rgb_colors.append(new)
#
# print(rgb_colors)
import turtle as tmod
import random

tmod.colormode(255)
t = tmod.Turtle()
screen = tmod.Screen()
t.speed(10)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
              (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211),
              (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220),
              (74, 213, 167),
              (77, 234, 202), (52, 234, 243), (3, 67, 40)]


b = -200
for x in range(9):
    t.penup()
    t.goto(-200, b)
    b+=50
    for i in range(9):
        t.pendown()
        t.dot(25, random.choice(color_list))
        t.penup()
        t.fd(50)


screen.exitonclick()
