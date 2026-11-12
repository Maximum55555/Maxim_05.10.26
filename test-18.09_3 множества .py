st1 = {3, 4, 33}
st2 = {3, 4, 44}

res = st1.union(st2) #oб'единение множеств
res = st1 | st2
print(res)

res = st1.intersection(st2) #пересечение множеств- выяв 2х разных субьектов
res = st1 & st2
print(res)

res = st1.difference(st2) #вычитание множеств
res = st2 - st1

print(res)

res = st1.symmetric_difference(st2) #Симметричная разность
res = st1 ^ st2
print(res)

st3 = {3, 4} #подмножество от мн ва 1 и 2
print(st3.issubset(st2))
print(st1.issuperset(st3))
