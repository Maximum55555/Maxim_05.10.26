g1= int(input())
g2= int(input())
g3= int(input())
Gused= int(input())
total=g1+g2+g3
left=g1+g2+g3-Gused
if 0<=g1<=1000000 and 0<=g2<=1000000 and 0<=g3<=1000000 and 0<=Gused<=total:
    print("Получено: ", total)
    print("Израсходовано: ", Gused)
    print("Осталось: ", left)
