# import lesson_package.utils
# from lesson_package.tools import utils
# from lesson_package.talk import human
# from lesson_package.talk import animal
# from lesson_package.talk import *
# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')

try:
    from lesson_package import *
except ImportError:
    from lesson_package.talk import *

print(animal.sing())
print(animal.cry())

# print(human.sing())
