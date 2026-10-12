""" Множество (set) неупорядоченный
набор уникальных объектов"""
ls = [22, 22, 22, 33, 33]
st = set(ls)
print(st)
st.clear()
st = {22, 33, 44}
print(st)
st.add('100')
st.add((2,3))
st.update({2,3})
st.update((545,685,777))
print(st)

#метод удаления 1
n = st.pop()
st.remove(3)
#метод удаления 2 discard

st.discard(3)


st1={3, 4, 33}
st2={3, 4, 44}
#res = st1.union(st2)
#res = st1 | st2
