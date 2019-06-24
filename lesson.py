# 辞書型
d = {'x':10,'y':20}

print(type(d))

d['z'] = 30

print(d)

# メソッド
print(d.keys())
print(d.values())

d2 = {'x':1000, 'j':500}

d.update(d2)
print(d)
print(d.get('x'))
x = d.pop('x')
print(x)
print(d)

d.clear()

d = {'a':1, 'b':2}

# inであるかどうかを確かめられる
has_a = 'a' in d

print(has_a)