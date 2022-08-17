# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:33:30 2016

@author: ericgrimson
"""

# def isPalindrome(s):
#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans = ans + c
#         return ans
#
#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#
#     return isPal(toChars(s))
#
#
# print("")
# print('Is llew a palindrome?')
# print(isPalindrome('siba'))
#
# print('')
# print('Is able was I ere I saw Elba a palindrome?')
# print(isPalindrome('siba'))


# def pal(b):
#     if b == str and pal(b[1:-1]):
#         return True
#     else:
#         return b[0] == b[-1] and pal(b[1:-1])
#
#
# print(pal('eve'))

# def ispal(c):
#     reads = ispal(c[1:-1])
#     if c <= 0:
#         return True
#     return reads
#
#
# ispal('eve')


def isIn(char, aStr):
    low = 0
    high = len(aStr) - 1
    while low <= high:
        mid = (low + high) // 2
        if char == aStr[mid]:
            return True
        elif char < aStr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


print(isIn('c', 'abc'))
