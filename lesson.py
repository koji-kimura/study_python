# # よくない例
# def test_func(x, l=[]):
#     l.append(x)
#     return l

# リストとか、辞書はデフォルト引数をつけないのが通例
# この関数みたいにNoneで設定する


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)


# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

# [100]のみではなく[100,100]になる。これは参照しているから
r = test_func(100)
print(r)
