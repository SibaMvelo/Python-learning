# look = [1, 2, 3, 4, 5, 6, 7]
# print(look[2])
# at = [8, 9, 10]
#
# this = look + at
# print(this)
#
# now = at.append(11)
# print(at)
#
# again = [2, 5, 4, 8, 6, 5, 7, 0]
# too = sorted(again)
# print(too)
# boom = ['l', 'o', 'v', 'e']
#
# street = too + boom
# print(street.pop())
#
# print(look.pop(2))

# cList = [6, 5, 4, 3, 2]
# dList = []
# for num in cList:
#     dList.append(num)
# cList == dList
#
# cList[2] = 20
# print(cList)
testList = [1, -4, 8, -9]

#
#
# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])
#
#
# def timesFive(a):
#     return a * 5
#
#
# def full_number(whole):
#     return abs(whole)
#
#
# def decrease(change):
#     change += 1
#     return change
#
#
# def power(num):
#     ans = num ** 2
#     return ans


# applyToEach(testList, power)

# print(testList)


# ------------------------------------------------------------------

# def applyEachTo(L, x):
#     result = []
#     for i in range(len(L)):
#         result.append(L[i](x))
#     return result
#
#
# def square(a):
#     return a * a
#
#
# def halve(a):
#     return a / 2
#
#
# def inc(a):
#     return a + 1
#
#
# # applyEachTo([inc, square, halve, abs], -3)
#
# # print(applyEachTo([inc, square, halve, abs], 3.0))
#
# print(applyEachTo([inc, max, int], -3))
# ----------------------------------------------------------------

#
# animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
#
#
# def how_many(aDict):
#     return aDict
#
#
# def biggest(aDict):
#     #     if len(animals['a']) > len(animals['b']) and len(animals['c']):
#     #         print(animals['a'])
#     #     elif len(animals['b']) > len(animals['a']) and len(animals['c']):
#     #         print(animals['b'])
#     #     else:
#     #         print(animals['d'])
#
#     # result = None
#     biggestValue = 0
#     for key in aDict.keys():
#         if len(aDict[key]) >= biggestValue:
#             result = key
#             biggestValue = len(aDict[key])
#     return result
#
#
# print(biggest(animals))

#
# def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#     returns: The key with the largest number of values associated with it
#     '''
#     # Your Code Here
#     if aDict == {}:
#         return None
#     else:
#         return max(aDict, key=lambda x: len(aDict[x]))
#
#
# print(biggest(animals))

# print(how_many(animals.values()))


# print(biggest(len(animals)))
#
# def count_keys(aDict):
#     count = 0
#     for i in enumerate(aDict):
#         count += 1
#     return count
#
#
# print(count_keys(animals))

mydict = {'george': 'cat', 'amber': 'dog'}
print(list(mydict.keys())[list(mydict.values()).index('dog')])
# def please(test):

# print()
    # Prints amber
