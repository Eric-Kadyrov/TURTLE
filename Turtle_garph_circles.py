import turtle as tur
import colorsys as cs
tur.speed(0)
tur.width(1)
tur.bgcolor("black")
h = 0.0
for j in range(6):
    for i in range(200):
        tur.color(cs.hsv_to_rgb(h,1,1))
        tur.circle(10+(i*1))
        h += 0.01
    tur.right(60)
tur.hideturtle()
tur.done()

