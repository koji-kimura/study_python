# 引数もっと追加したい
# def menu(entree='beef', drink='wine'):
#     print(entree, drink)

# **で辞書化できる


# def menu(**kwargs):
#     # print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)

# 引数を文字列タプル辞書と併用できる
def menu(food, *args, **kwargs):
    # print(kwargs)
    print(food)
    print(args)
    print(kwargs)


# menu(entree="beef", drink="coffee")
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
# **で辞書を展開している
# menu(**d)
menu('banana', 'appe', 'orange', entree="beef", drink="coffee")
