r = [1,2,3,4,5,1,2,3]

print(r.index(3))
print(r.index(3,3))
print(r.count(3))

if 5 in r:
  print('exist')

r.sort()

print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)
# .joinは文字列を繋げる
x = ' '.join(to_split)
print(x)