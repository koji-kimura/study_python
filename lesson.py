def say_something():
    print('hi')


def say_something_return():
    return 'hi return'


say_something()

print(type(say_something))

result = say_something_return()
print(result)

# 引数の話


def what_is_this(color):
    if(color == 'red'):
        return 'tomato'
    elif(color == 'green'):
        return 'green pepper'
    else:
        return "I don't know"


color_result = what_is_this('red')
color_result2 = what_is_this('green')
color_result3 = what_is_this('blue')

print(color_result)
print(color_result2)
print(color_result3)
