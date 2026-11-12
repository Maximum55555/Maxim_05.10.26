""" dict= словарь\ неупорядоченный набор пар ключ-значение в которыхключ уникален
"""

d= {}

d= {'Pb': 'свинец', 'Au': 'Золото'}

print(d['Pb'])
print(d.get('Au', 'my items'))

d['Pb']='свинец'
print(d)

d['Fe']='железо'
print(d)

d.setdefault(1, 1000) #добавить значение 1000 некоему новому значениию 1
print(d)

d.update({3: 33, 1: 11}) #присвоить значение 33 некоему новому значениию 3 и 11-вместо 1000 присвоили к 1
print(d)

n=d.pop('Fe') #убрать последнюю добав ю в словарь пару
nn=d.popitem()

print(n,nn)
#d.clear()
print(d)
print(len(d)) #
print(d.keys())
print(list(d))
for i in d:
    print(i)
    
print(list(d.values()))
for v in d.values():
    print(v)
print(list(d.keys()))

print(list(d.items()))
for k,v in d.items():
    print(k,v)


