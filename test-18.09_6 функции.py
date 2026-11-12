"""функции"""

def summator(a=10, b=4):
    #print(a + b)
    return a * b

n = 45
cc = 'qwerty'
n = summator(2, 3) #позиционные аргументы 
#n = summator(2)
#print(summator(2, 3))
print('функция', n)
#print(summator(5, 10))
print(summator(2))
print(summator(b=8))

#def printing(*args):
def printing(*kwargs):
    #print(args)
    #return sum(args)
    print(kwargs)

printing()
printing(1)
printing('Name1', 'Name2', 'Name3')
printing('Name1', 'Name2')

print(printing())
print(printing(1, 3, nn=16, y=45))
