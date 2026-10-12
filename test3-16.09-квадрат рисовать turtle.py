import turtle

#Ugol = 17

#turtle.begin_fill()
#for i in range(Ugol):
#    turtle.forward(50)
#    turtle.left(360 / Ugol)
#turtle.end_fill()


#turtle

#for i in range(4):
#    turtle.forward(10)
#    turtle.left(90)

Ugol = input("Введите кол-во углов
             ")
Ugol = int(Ugol)
Tsvet = input("Введите цвет заливки ")

turtle.fillcolor(Tsvet)
turtle.begin_fill()
for i in range(Ugol):
    turtle.forward(50)
    turtle.left(360 / Ugol)
turtle.end_fill()
turtle.begin_fill()
for i in range(Ugol):
    turtle.forward(50)
    turtle.left(360 / Ugol)
turtle.end_fill()


