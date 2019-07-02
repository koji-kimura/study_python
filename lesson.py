# class Person(object):のobjectは省略できる
class Person(object):
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


person = Person('mike')
person.say_somethig()
