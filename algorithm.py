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


data = [1, 2, 3, 4, 5, 6, 7, 8]
number = 5
while_looping = 0
while while_looping < number:
    for i in range(len(data)):
        if data[i] == number:
            print("number of loops is: ", str(i), 'and the number is: ', str(data[i]))
        else:
            print('Still looking!')
    while_looping += 1
