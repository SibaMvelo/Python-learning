# def f(x):
#     x -= 1
#     print('in f (x): x =', x)
#     return x
#
#
# x = 5
# f(x)
#
#
# def example_one():
#     print(' Inside example one', example_one())
#
#
# def example_two(y):
#     print(' Inside example two', example_two())
#     return y
#
#
# def example_three(z):
#     print('inside example three', example_three())
#     return z()
#
#
# print('Example one is', example_one())
# print('Example two is', 5 + example_two(2))
# print('Example three is ', example_three(example_one))

# def full_name(name, last_name, reverse=True):
#     if reverse:
#         print(name, last_name)
#     else:
#         print(last_name, name)
#
#
# full_name(1, 2)
#
# def foo(x, y=5):
#     def bar(x):
#         return x + 1
#
#     return bar(y * 2)
#
#
# foo(3)

# def is_even(i):
#     print(i)
#     return i % 2 == 0
#
#
# is_even(7)

# def foo(x, y=5):
#     def bar(x):
#         return x + 1
#
#     return bar(y * 2)
#
#
# foo(3, 0)

# x = 34
#
#
# def scope_test(x):
#     print('x == ', x)
#     x = 2
#     print('X is changed to == ', x)
#
#
# scope_test(x)
# print('x is at outer scope', x)

# def foo(p=5, *args):
#     print(type(args))
#
#
# foo(5, 6, 7, 8)


def fourthPower(x):
    square = x ** 4
    print('The square is', square)


fourthPower(5)
