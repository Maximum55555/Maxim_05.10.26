num = [1, 2, [32, 4]]
# nn = num
# nn = num[:]
nn = num.copy()
num[1] = 3333
num[-1][1] = 400
print(num, id(num))
