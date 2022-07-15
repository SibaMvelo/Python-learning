# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!')

# --------------------

# num = 10
# for num in range(5):
#         print(num)
# print(num)
#
# divisor = 2
# for num in range(0, 10, 2):
#     print(num/2)

# --------------------

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# num = 10
# for num in range(5):
#     print(num)
# print(num)

# divisor = 2
# for num in range(0, 10):
#     print(num)

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
#     print(count)


# greeting = 'Hello!'
# count = 0
#
# for letter in 'Hello!':
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

# cube = -28
#
# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
#     if guess**3 != abs(cube):
#         print(cube, 'is not a perfect cube')
#     else:
#         if cube < 0:
#             guess = -guess
#         print('Cube root of ', str(cube), 'is ', str(guess))

# cube = 5
#
# for guess in range(cube + 1):
#     if guess ** 3 == cube:
#         print('Cube root of ', str(cube), 'is ', str(guess))
#     # else:
#     #     print(str(cube), 'is not a perfect cube')
#     if guess ** 3 != cube:
#         print(str(cube), 'is not a perfect cube')

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     # iteration += 1
#
# for letter in "hello, world":
#     while iteration < 3:
#         count += 1
#         iteration += 1
# print('Iteration', str(iteration), '; count is:', str(count))

# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break

# count = 0
# # phrase = "hello, world"
# for iteration in range(5):
#     count += len("hello, world")
#     print("Iteration " + str(iteration) + "; count is: " + str(count))

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in 'hello, Siba':
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print('Iteration ', str(iteration), '; count is: ', str(count))


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1
# loop = ['Siba', 'Michelle', 'Sibo', 'Sihle']
# for r in loop:
#     print(len(r))
#
# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     index = 0
#     while index < len(phrase):
#         count += 1
#         index += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count), '; and index is:', str(index))

# count = 0
# for i in 'Siba':
#     count += 1
# print('Iteration is:', str(i), 'and count is: ', str(count))

# letter = 0
# count = 0
# while letter < 5:
#     for iteration in 'Siba':
#         count += 1
#         letter += 1
#     print('Iteration is:', str(iteration), '; count is:', str(count), 'and letter is:', str(letter))

# count = 0
# for iteration in range(5):
#     name = 0
#     while name < len('Siba'):
#         count += 1
#         name += 1
#     print('Iteration is:' + str(iteration) + '; count is:' + str(count))
#     iteration += 1

# vowels = ('a', 'e', 'i', 'o', 'u')
# s = input('Please enter a word!')
# count = 0
# for word in s:
#     if word in vowels:
#         count += 1
# print('Number of vowels:', count)

# words = ('boy', 'girl', 'ball')
# sentence = input('Please enter a sentence with the words boy, girl and ball.')
# count = 0
# for selected_words in sentence:
#     if selected_words in words:
#         count += 1
# print('The words are:', count)


# letters = ('a', 'b', 'c')
# name = input('Please enter your name:')
# number_of_abc = 0
#
# for check_abc in name:
#     if check_abc in letters:
#         number_of_abc += 1
# print('The number of abc is:', number_of_abc)

# number = ('1', '2', '3')
# phone_number = input('Please enter your phone number:')
# one_two_three = 0
#
# for digits in phone_number:
#     if digits in number:
#         one_two_three += 1
# print('The number of  one two three is:', one_two_three)
#
# bob = 'bob'
# s = input()
# count = 0
#
# for number_of_times in s:
#     if number_of_times in bob:
#         count += 1
# print('Number of times bob occurs is:', count)

#
# word = input('What is the word?')
# alphabetic = sorted(word)
# count = 0
#
# for is_alphabetic in word:
#     if is_alphabetic in alphabetic:
#     print('Longest substring in alphabetical order is', count)

#
# iteration = 0
# # while iteration < 2:
#     count = 0
#     # for letter in "Siba":
#         count += 1
#         # if iteration % 2 == 0:
#         #     break
#     iteration += 1
#     print("iteration is: ", str(iteration), "and count is: ", str(count))
#
# i = 0
# while i < 8:
#     count = 0
#     for name in "Green":
#         count += 1
#         if i % 4 == 2:
#             break
#     i += 1
#     print("i is: ", str(i), "and count is: ", str(count))

# nums = [1, 2, 3, 4, 5]
# count = 0
# while count != 1:
#     for num in nums:
#         if num == 4:
#             print("Found 4")
#             continue
#         print(num)
#     count += 1

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every
#     # character, including spaces and commas!
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         iteration += 1

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
        print("letter is: ", str(letter), "count is", str(count), "iteration is:", str(iteration))
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
#
# iteration = 0
# while iteration < 5:
#     count = 0
#     for 1234567
