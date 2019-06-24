# タプルについて
# ()で囲ってあげる、省略もできる、タプルは,をつける
t = (1,2,3,4,1,2)
print(t)
print(type(t))
print(t.count(1))

num_tuple = (10,20)
print(num_tuple)
x,y = num_tuple
print(x,y)

# 入れ替えも簡単にできる
i = 10
j = 20
print(i,j)
tmp = i
i = j
j = tmp
print(i,j)

a = 100
b = 200
print(a,b)
a,b = b,a
print(a,b)

## ならどうやって使うのか？
## tuppleは配列とは異なり、appendできないのでその性質を利用する
chose_from_two = ('A','B','C')
answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)
