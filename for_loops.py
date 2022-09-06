# for i in range(2, 12, 2):
#     print(i)
#     if i == 10:
#         print('Goodbye!')
# # --------------------
#
# for i in range(2, 12, 2):
#     print(i)
#     if i == 10:
#         print('Goodbye!')
#
# # --------------------
# # --------------------
#
# result = 0
# end = 6
# for i in range(end + 1):
#     result += i
# print(result)


# def for_loop(x):
#     for i in range(x):
#         x -= 1
#         print('x is: ', x)
#     return x
#
#
# print(for_loop(10))

#
# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# for letter in 'hola':
#     print(letter)
#
# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!')

# num = 10
# for num in range(5):
#     print(num)
# print(num)

# divisor = 2
# for num in range(0, 10, 2):
#     print(num/divisor)

# greeting = 'Hello!'
# count = 0
#
# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print(letter)
#     print(letter)
#
# print('done')


# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1
#
# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons))

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1
#
# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#
# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break

#
# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     index = 0
#     while index < len(phrase):
#         count += 1
#         index += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))

# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     while True:
#         count += len(phrase)
#         break
# print("Iteration " + str(iteration) + "; count is: " + str(count))

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
