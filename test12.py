g1= input()
g2= input()
g3= input()
Gused= input()
total={g1+g2+g3}
left={g1+g2+g3-Gused}
if 0<=g1<=1000000 and 0<=g2<=1000000 and 0<=g3<=1000000 and 0<=Gused<=total:
    print("Получено: ", total)
    print("Израсходовано: ", Gused)
    print("Осталось: ", left)
else: print("Ошибка!")
