# 集合について
# {}でキーをつけないで値を入れればいい
# 重複が消える
a = {1,2,3,4,5,5,6}
b = {2,3,3,6,7}
# print(a)
# print(a-b)
# print(b-a)
# print(a&b)
# print(a|b)
# print(a^b)

# methods
# s = {1,2,3,4,5}
# s.add(6)
# print(s)
# s.remove(6)
# print(s)

# どんな時に使うのか?

my_friends = {'A','C','D'}
A_friends = {'B','D','E','F'}

print(my_friends & A_friends)

# setで集合にできる
f = ['apple','banana','apple','banana']
kind = set(f)
print(kind)