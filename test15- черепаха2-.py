from turtle import *

speed(0)
colormode(255)
shape('turtle')
pensize(4)

# Начальный размер (большой)
radius = 150

# Начальный цвет (желтый)
r = 255
g = 255
b = 0

# Внешний цикл: рисуем 8 слоев
for i in range(8):
    # Плавно уменьшаем радиус
    radius = radius - 15
    
    # Плавно меняем цвет: красный уходит в ноль, зеленый остается (получаем переход от желтого к зеленому)
    r = r - 32
    if r < 0:
        r = 0
    
    # Заливаем и рисуем лепестки по кругу
    color((r, g, b), (r, g, b))
    for j in range(12):
        begin_fill()
        circle(radius)
        end_fill()
        right(30)

mainloop()
