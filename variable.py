from copy import copy

a = [1,2,3]
b = a     # 같은 주소의 값을 넣어준다.

print(id(a))
print(id(b))
print(b is a)

c = [1,2,3]
d = c[:]  # 슬라이싱으로 새로운 주소에 값을 넣어준다.
print(id(c))
print(id(d))
print(d is c)

e = copy(a);  # 새로운 주소에 값을 할당해주는 api
print(id(e))

# 튜플, 리스트를 이용하여 각각의 변수에 값을 할당한다.
a, b = ('python', 'life')
(c, d) = ('python', 'life')
[e, f] = ['python', 'life']

# temp 변수를 이용하지 않고 직관적으로 변수를 변경할 수 있다.
a = 3
b = 5
a,b = b,a
print(a)
print(b)


