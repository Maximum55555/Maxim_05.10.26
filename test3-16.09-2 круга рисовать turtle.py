import turtle as t

# Включаем режим RGB (0-255) — это обязательно!
t.colormode(255)

# Первый круг
t.begin_fill()
t.fillcolor(255, 127, 80)  # Цвет заливки (коралловый)
t.pencolor(255, 127, 80)   # Цвет контура (можно не менять)
t.circle(50)
t.end_fill()

# Перемещаемся вправо
t.penup()
t.fd(50)
t.pendown()

# Второй круг
t.begin_fill()
t.fillcolor(255, 160, 122) # Светло-лососевый
t.pencolor(255, 160, 122)
t.circle(50)
t.end_fill()

t.done() # Чтобы окно не закрылось сразу
