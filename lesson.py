# class Person(object):のobjectは省略できる
class Person(object):
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        # print('First', name)

    def say_somethig(self):
        # initで入れたものは他のメソッドの中でも使える
        print('I am {}.hello'.format(self.name))
        # 自分自身の中から呼び出せる
        # selfは引数をとらないのでこの記述でOK
        self.run(10)

    def run(self, num):
        print('run' * num)

    # デストラクタ
    def __del__(self):
        print('good bye')


person = Person('mike')
person.say_somethig()
# 明示的に呼びたい場合
del person
