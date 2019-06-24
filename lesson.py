i = [1,2,3,4,5]
# 参照渡しになってしまう
j = i
i[0] = 100
print(i)
print(j)

x = [1,2,3,4,5]
y = x.copy()
x[0] =100
print(x)
print(y)
print(id(x))
print(id(y))