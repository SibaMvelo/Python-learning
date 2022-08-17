# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# while guess <= x:
#     if abs(guess ** 2 - x) >= epsilon:
#         guess += step
#
# if abs(guess ** 2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))

#
# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# while abs(guess**2-x) >= epsilon:
#     if guess <= x:
#         guess += step
#     else:
#         break
#
# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))

# Linear search
# data = [1, 2, 3, 4, 5, 6, 7, 8]
# number = 5
# while_looping = 0
# while while_looping < number:
#     for i in range(len(data)):
#         if data[i] == number:
#             print("number of loops is: ", str(i), 'and the number is: ', str(data[i]))
#         else:
#             print('Still looking!')
#     while_looping += 1

# interactive search
# shelve = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# book = int(input())
# left = 0
# right = len(shelve) - 1
#
# while left < right:
#     mid = (left + right) // 2
#     if book == shelve[mid]:
#         print(book)
#         break
#     elif book < shelve[mid]:
#         left = shelve[mid] - 1
#         print(left)
#     else:
#         right = shelve[mid] + 1
#         print(right)
#     break

# biselection search
# cube = int(input())
# epsilon = 0.01
# num_of_guesses = 0
# left = 0
# right = cube
# guess = (right + left) // 2
#
# while abs(guess ** 3 - cube) > epsilon:
#     if guess ** 3 < cube:
#         left = guess
#     else:
#         right = guess
#         guess = (right + left) // 2
#         num_of_guesses += 1
#     print('number of guesses:', num_of_guesses)
#     print(guess, 'is close to the cube root of', cube)


# guessed_numbers = range(100)
# low_numbers = 0
# high_numbers = len(guessed_numbers) - 1
# users_guess = input('Enter l if your number is < 50 and h if it is > than 50:')
# number_of_guesses = 0
# while low_numbers < high_numbers:
#     mid = (low_numbers + high_numbers) // 2
#     if users_guess == 'l':
#         print('Please think of a number between 0 and 100!')
#         guessed_numbers[mid] - 1
#     elif users_guess == 'h':
#         mid = (low_numbers + high_numbers) // 2
#         print('Please think of a number between 0 and 100!')
#         guessed_numbers[mid] + 1
#         print('Is your number:', str(guessed_numbers[mid] + 1))
#         break
#     number_of_guesses += 1

# from random import randint
#
# number = randint(0, 99)
#
# print("think of a number from 0-100")
#
# while number:
#     guess = str(input(f"is your number : {number} "))
#     if guess == "h":
#         number = randint(number, 99)
#     elif guess == "l":
#         number = randint(0, number)
#     elif guess == "c":
#         print("yay")
#         exit()

# low = 0
# high = len(range(100))
#
# print('Please think of a number between 0 and 100!')
# while high:
#     guess = (low + high) // 2
#     number = input(f'Is your secret number {guess} ')
#     if number == 'l':
#         low = guess - 1
#     elif number == 'h':
#         high = guess + 1
#     elif number == 'c':
#         print('Yay')
#         break
#     else:
#         print("please enter valid input - l,h or c")
# print('Game over. Your secret number was: ' + str(guess))


# print("Please think of a number between 0 and 100!")
#
# # At the start the highest the number could be is 100 and the lowest is 0.
# hi = 100
# lo = 0
# guessed = False
#
# # Loop until we guess it correctly
# while not guessed:
#     # Bisection search: guess the midpoint between our current high and low guesses
#     guess = (hi + lo) // 2
#     print("Is your secret number " + str(guess) + "?")
#     user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter "
#                      "'c' to indicate I guessed correctly. ")
#
#     if user_inp == 'c':
#         # We got it right!
#         guessed = True
#     elif user_inp == 'h':
#         # Guess was too high. So make the current guess the highest possible guess.
#         hi = guess
#     elif user_inp == 'l':
#         # Guess was too low. So make the current guess the lowest possible guess.
#         lo = guess
#     else:
#         print("Sorry, I did not understand your input.")
#
# print('Game over. Your secret number was: ' + str(guess))
