from turtle import *

shape('turtle')
speed(0)
colormode(255)
pensize(4)
r = 255
g = 255
b = 0
color('green', (r, g, b))

for i in range(8):
    begin_fill()   # <--- Исправлено с fillcolor()
    circle(200)
    end_fill()

mainloop()
