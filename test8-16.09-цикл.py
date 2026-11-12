# print(arr)
ls = []
for i in range(10):
    if i > 1:
        if i+1 // 2 == 0:
            ls.append(i + 1)
        else:
            ls.append(i)
print(ls)
print(5 if len(ls) < 7 else 125)
ls = [1 + 1 if (1 + 1) % 2 == 0 else i for i in range(10) if i > 4]
print(ls)
""" кортеж (Tuple) """
