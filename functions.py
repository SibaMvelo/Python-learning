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

#
# def fourthPower(x):
# '''
#   x: int or float.
#   '''
#     square = x ** 4
#     print('The answer is ', square)
#
#
# # fourthPower()

# POWER
# def powers(base, power):
#     result = base ** power
#     print(result)
#
#
# powers(2, 5)


#
# def odd(x):
#     '''
#     x: int
#
#     returns: True if x is odd, False otherwise
#     '''
#     number = x % 2
#     # return number
#
#     print(number == 1)
#
#
# odd(4)


# def odd(x):
#     print(x % 2 == 1)
#
#
# odd(4)

# MULTIPLICATION SOLUTION
#
# def multiplier(a, b):
#     result = 0
#     while b > 0:
#         result += a
#         # b -= 1
#         # return result
#     print(result)
#
#
# multiplier(2, 5)

# def multi(a, b, c):
#     ans = 0
#     while b and c > 0:
#         ans += a
#         ans += a
#
#         b -= 1
#         c -= 1
#     print(ans)
#
#
# multi(5, 2, 2)

# RECURSIVE

# def recursive(number):
#     if number == 1:
#         return 1
#     else:
#         return number * recursive(number - 1)
#
#
# print(recursive(2))


# def newpower(base = input('Please enter the Base '), exp = input('Please enter the Exponent '):
#     ans = 1
#     for i in range(exp):
#         ans *= base
#     print(ans)

# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
#     ans = 1
#     for i in range(exp):
#         ans *= base
#     return (ans)
#
#
# print(iterPower(2, 5))

# def recurPower(base, exp):
#      if exp <= 0:
#          return  1
#     else:
#     return base * recurPower(base, exp-1)
#
#
# def rec(base, exp):
#     if base


# def recurPower(base, exp):
#     if exp <= 0:
#         return 1
#     # Otherwise, exp must be > 0, so return
#     #  base* base^(exp-1). This is the recursive case.
#     return base * recurPower(base, exp - 1)
#
#
# print(recurPower(2, 5))
# # recurPower(0, 5)

# def powers(base, exp):
#     ans = 1
#     for i in range(exp):
#         ans *= base
#     return ans
#
#
# print(powers(2, 6))


# def powers2(base, exp):
#     if exp <= 0:
#         return 1
#     return base * powers2(base, exp - 1)
#
#
# print(powers2(2, 7))


# def power1(base, exp):
#     result = 1
#     for i in range(exp):
#         result *= base
#     return result
#
#
# print(power1(3, 2))
#

# def power2_a(base, exp):
#     if exp <= 0:
#         return 1
#     return base * power2_a(base, exp - 1)
#
#
# print(power2_a(4, 4))


# def p(base, exp):
#     ans = 1
#     for i in range(exp):
#         ans *= base
#     return ans
#
#
# print(p(2, 5))

#
# def b(base, exp):
#     if exp <= 0:
#         return 1
#     return base * b(base, exp - 1)
#
#
# print(b(5, 2))


# def c(base, exp):
#     n = 1
#     for i in range(exp):
#         n *= base
#     return n
#
#
# print(c(2, 8))


# def d(base, exp):
#     if exp <= 0:
#         return 3
#     return base + d(base, exp - 1)
#
#
# print(d(2, 2))

# def e(n):
#

# def e(a, b):
#     if b <= 0:
#         return 0
#     return a + e(a, b - 1)
#
#
# print(e(2, 2))


# def f(c, d):
#     if d <= 0:
#         return 1
#     return c - f(c, d - 1)
#
#
# print(f(5, 2))


# def g(a, b):
#     result = 1
#     for i in range(b):
#         result *= a
#     return result
#
#
# print(g(1, 5))


# def gcdIter(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''


#     result = 0
#     for i in range(b):
#         result //= a
#     return result
#
#
# print(gcdIter(12, 3))


# def o(a, b):
#     ans = 1
#     for i in range(b):
#      a // 2
#     return ans
#
#
# print(o(2, 12))

"""
The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value
equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a
case where the test divides both a and b without remainder, or you reach 1.
"""

# def p(a, b):
#     n = min(a, b)
#     while a % n != 0 or b % n != 0:
#         n -= 1
#     return n


#
#
# print(p(2, 12))
# print(p(6, 12))
# print(p(9, 12))
# print(p(17, 12))


# def q(a, b):
#     if b <= 0:
#         return 1
#     return a * q(a, b - 1)
#
#
# # print(q(5, 5))
#
#
# def g(a, b):
#     ans = 1
#     for i in range(b):
#         ans *= a
#     return ans
#
#
# print(g(2, 5))
from math import tan, pi

"""The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer."""

# def h(a, b):
#     n = max(a, b)
#     while a % n != 0 or b % n != 0:
#         n -= 1
#     return n
#
#
# print(h(2, 12))
# print(h(6, 12))
# print(h(9, 12))
# print(h(17, 12))


# # recursion
# def s(a, b):
#     n = max(a, b)
#     if a % n != 0 or b % n != 0:
#         n = s(b, a % b)
#     return n
#
#
# print(s(2, 12))
# print(s(6, 12))
# print(s(9, 12))
# print(s(17, 12))

# def rec(a, b):
#     n = max(a, b)
#     if b != 0:
#         return rec(b, a % b)
#     return n
#
#
# print(rec(2, 12))
# print(rec(6, 12))
# print(rec(9, 12))
# print(rec(17, 12))


# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Base case is when b = 0
#     if b == 0:
#         return a
#
#     # Recursive case
#     return gcdRecur(b, a % b)
#
#
# print(gcdRecur(2, 12))
# print(gcdRecur(6, 12))
# print(gcdRecur(9, 12))
# print(gcdRecur(17, 12))


# Fibonacci

# def fib(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 1)
#
#
# print(fib(7))

"""We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be."""

"""iteration method"""

# def isIn(char, aStr):
#     low = 0
#     high = len(aStr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if char == aStr[mid]:
#             return True
#         elif char < aStr[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return False


"""Recursive bisect method"""

# def isIn2(char, aStr) -> bool:
#     if not aStr:
#         return False
#     center = len(aStr) // 2
#     if char == center:
#         return True
#     elif char < aStr[center]:
#         return isIn2(char, aStr[:center])
#     else:
#         return isIn2(char, aStr[center + 1:])
#     return False
#
#
# print(isIn2('x', 'abcdef'))

# def is_in(char, txt) -> bool:
#     """Because we are too retarted to use the builtin bisect."""
#     if not txt:
#         return False
#     cut_off = len(txt) // 2
#     middle = txt[cut_off]
#     if char == middle:
#         return True
#     elif char < middle:
#         return is_in(char, txt[:cut_off])
#     else:
#         return is_in(char, txt[cut_off + 1:])
#
#
# assert not is_in('a', '')
# assert is_in('a', 'a')
# assert not is_in('c', 'a')
# assert is_in('a', 'ab')
# assert not is_in('c', 'ab')
# assert is_in('b', 'ab')
# assert is_in('b', 'abc')
# assert is_in('b', 'abcd')
#
# print(is_in('x', 'abcd'))

"""Assessment Answer"""

# def isIn(char, aStr):
# '''
# char: a single character
# aStr: an alphabetized string
#
# returns: True if char is in aStr; False otherwise
# '''
# # Base case: If aStr is empty, we did not find the char.
#     if aStr == '':
#         return False
#
# # Base case: if aStr is of length 1, just see if the chars are equal
#     if len(aStr) == 1:
#         return aStr == char
#
# # Base case: See if the character in the middle of aStr equals the
# #   test character
#     midIndex = len(aStr) // 2
#     midChar = aStr[midIndex]
#     if char == midChar:
#     # We found the character!
#         return True
#
# # Recursive case: If the test character is smaller than the middle
# #  character, recursively search on the first half of aStr
#     elif char < midChar:
#         return isIn(char, aStr[:midIndex])
#
# # Otherwise the test character is larger than the middle character,
# #  so recursively search on the last half of aStr
#     else:
#         return isIn(char, aStr[midIndex + 1:])
#
# def polysum(n, s):
#     n = (0.25 * n * s ** 2) / tan(pi / n)
#     s = (s * n) ** 2
#     ans = n + s
#
#     return ans
#
#
#

# x = 34

# def scope_test(x):
#     print('x == ', x)
#     x = 2
#     print('X is changed to == ', x)
# scope_test(x)
# print('x is at outer scope', x)

# def printer():
#     t = 'to PythonEasy'
#     fname = (lambda a: t + ' ' + a)
#     return fname
#
#
# foo = printer()
# print(foo('Welcome'))

# def rec(a, b):
#     if a == 0:
#         return b
#     print(rec(a - 1, a + b))
# else:
#     return rec(a - 2, a + b)


# print(rec(8, 12))

# def rec2(c):
#     if c == 0:
#         return 1
#     return rec2(c - 2)
#
#
# print(rec2(1))


# info = [1, 2, 3, 4, 5, 6]

#
# def joj(info, b):
#     low = 0
#     high = len(info) - 1
#     mid = (low + high) // 2
#     while low < high:
#         if b == info[mid]:
#             return True
#         elif b < info[mid]:
#             high = mid - 1
#             return high
#         else:
#             low = mid + 1
#             return low
#
#
# b = int(input('Input your number '))
# print(joj(info, b))

# print('Monthly payment is : {}'.format(payment(initial_amount, annualInterestRate)))

# def joy():
# a = 5
# b = 3

# def rec_multy(a, b):
#     if b != 0:
#         return 0
#     return a + rec_multy(a, b - 1)
#
#
# print(a * b)
# print(rec_multy(a, b))
#
# a = 5
# b = 5
#
#
# def rec_mul2(a, b):
#     if b == 0:
#         return print('There is noting left')
#     return rec_mul2((a * b) - 1)

# a = 5
# b = 5


# def one(a):
#     if a == 0:
#         return 1
#     return a - one(a - 1)
#
#
# print(one(5))

b = 0


# def two(b):
#     if b == 5:
#         return 5
#     print(b)
#     return two(b + 1)
#
#
# print(two(b))

# c = 5


# def three(c):
#     if c == 0:
#         return 1
#     return c * three(c - 1)
#
#
# # print(c * c)
# print(three(5))


def solution(A):
    A.sort()
    N = len(A)

    P1 = A[N - 1] * A[0] * A[1]
    P2 = A[N - 1] * A[N - 2] * A[N - 3]

    return max(P1, P2)


print(solution([-3, 1, 2, -2, 5, 6]))

