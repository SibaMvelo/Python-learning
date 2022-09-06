# n = int(input('Enter Any Size of Class You Want: '))
#
# pass_student = 0
# fail_student = 0
# sum = 0
# for i in range(n):
#     mark = int(input("Enter Marks (0 - 100): "))
#
#     if mark < 0 or mark > 100:
#         print('Invalid Marks!!!')
#         break
#     elif mark >= 50:
#         pass_student = pass_student + 1
#         sum += mark
#     else:  # 0 <= mark < 50
#         fail_student = fail_student + 1
#         sum += mark
#
# print('The Total Passed Student: ', pass_student)
# print('The Total Failed Student: ', fail_student)
# print('The Average is: ', sum // (pass_student + fail_student))
#
# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1