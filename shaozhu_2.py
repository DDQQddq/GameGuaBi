import turtle as t
import time

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
r = 20

for i in range(1, 7):
    t.penup()
    t.sety(-15*i)
    t.pendown()
    t.pencolor(colors[i-1])
    t.circle(15*i)
else:
    t.hideturtle()

time.sleep(4)
