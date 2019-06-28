# l = ['Good morning', 'Good afternoon', 'Good night']

# for i in l:
#     print(i)


def counter(num=10):
    for _ in range(num):
      # ジェネレーターにreturnはない
        yield 'run'


print("##############")


def greeting():
    #  要素を発生させていく
    yield 'good morning'
    yield 'good afternoon'
    yield 'good night'


# for g in greeting():
#     print(g)

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
