a = True
print(type(a), a)

a = [1,2,3,4]
while a:
  a.pop()
  print(a)

# True, False는 대문자로 시작한다.
# "", [], {} 등 빈자료형은 모두 False
# "Stinrg" 등 데이터가 들어있는 자료형은 True
# 1은 True, 0은 False