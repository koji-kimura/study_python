# dictでも参照渡しになってしまう
x = {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a':1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# どういうタイミングで使うのか？
# listでもデータ持てるけれど、keyでさっと取ってこれない
# dictの方が早い
fruits = {
  'apple':100,
  'banana':200,
  'orange':300
}

print('apple %d'%fruits['apple'])