print(num[2:])
print(num[2:-1])
print(num[::-1])

nn = num
print(num, id(num))
print(nn, id(nn))
print(nn is num)
nn = num [:]
