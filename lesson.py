# 引数の頭に*を入れることで引数をタプル化できる
def say_something(word, *args):
    print('word=', word)
    for arg in args:
        print(arg)


say_something('hi', 'Mike', 'Nance')

# t = ('Mike', 'Nancy')
# say_something('hi', *t)
