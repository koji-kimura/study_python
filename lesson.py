def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.1415)

print(ca1(10))
print(ca2(10))

# def outer(a, b):
#     def inner():
#         return a+b
#     # 関数を返しているだけ
#     return inner


# f = outer(1, 2)
# r = f()
# print(r)
