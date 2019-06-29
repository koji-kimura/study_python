"""
test test#############
"""

animal = 'cat'


def f():
    # global animal
    # print(animal)
    animal = 'dog'
    print('local:', locals())


f()
print('global:', globals())
# print(animal)
print(__name__)
