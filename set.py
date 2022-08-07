# 집합
# 

#선언 방법
s1 = set([1 ,2, 3]);
s2 = {1,2,3}

print(s1)
print(s2)
print(type(s1))

# 중복된 값을 지우고 list로 만들어줄수 있다.
l = [1,2,2,3,3]
newList = list(set(l))
print(newList)

# String 값도 set으로 만들어주면 중복을 피할수 있다.
s3 = set("hello")
print(s3)

# 교집합
s4 = set([1,2,3,4,5,6])
s5 = set([4,5,6,7,8,9])
print(s4 & s5)
print(s4.intersection(s5))

# 합집합
print(s4 | s5)
print(s4.union(s5))

# 차집합
print(s4 - s5);
print(s4.difference(s5))

# 값 추가
s1.add(7)
print(s1)

# 여러개 값 추가
s1.update([7,8,9,])
print(s1);

# 값 제거
s1.remove(7)
print(s1)

