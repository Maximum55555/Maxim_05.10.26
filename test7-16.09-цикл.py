temp = l[0]
n = len(l)
for i in range(n-1):
    l[i] = l[i + 1]
l[-1] = temp
print(temp)
l.append(temp)
print(l)
