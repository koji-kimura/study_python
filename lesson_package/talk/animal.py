from lesson_package.tools import utils


def sing():
    return '???????'


def cry():
    return utils.say_twice('????')


if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)
