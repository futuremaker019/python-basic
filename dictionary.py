dic = {'name' : 'Jun'}

# js 객체와 같이 만들어잔다.
print(dic, dic['name']);

a = {1: '파랑구름', 2: '이현준', 3: '민준'}

print(a.keys())
print(a.values())
print(a.items())

for k in a.keys():
  print(k);

for k, v in a.items():
  print("카 : " + str(k))
  print("value : " + v)

# boolean 확인도 가능하다.
print(4 in a);