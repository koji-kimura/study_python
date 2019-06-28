# このリストの頭文字を大文字にするためのプログラミング
l = ['Mon', 'tus', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

# ラムダは簡単に関数を定義できる
sample_func(word): lambda word: word.capitalize()


change_words(l, sample_func)
