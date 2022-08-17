# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
# Result
# Your
# Code
# Should
# Generate
# Below:
# Remaining
# balance: 361.61


#
# def payment(UnpaidBalance, annualInterestRate, monthlyPaymentRate):
#     annualInterest = (annualInterestRate * UnpaidBalance)
#     monthlyInterest = (annualInterest // 12.0)
#     monthlyPayment = (monthlyPaymentRate * UnpaidBalance)
#     year = 0
#     while year != 12:
#         year += 1
#         balance = UnpaidBalance - monthlyPayment
#         balance = monthlyInterest + balance
#         print(year)
#     return round(balance, 2)


# print('Remaining balance:', payment(5000, 0.18, 0.02))

# value = input('Enter the amount you borrowed: ')
# monthlyPaymentRate = input('What is the monthly rate you are paying? ')
# annualInterestRate = input('What is the annual interest rate for charged? ')
# numberOfMonths = input('How many months do you want to check the balance after payment? ')


# def balance(value, monthlyPaymentRate, annualInterestRate):
#     for i in range(12):
#         interest = (value - (value * monthlyPaymentRate)) * annualInterestRate / 12
#         newValue = value - (value * monthlyPaymentRate)
#         value = newValue + interest
#     return value
#
#
# #
# #
# # # print("After " + numberOfMonths + " month the value is "+ balance(42, 0.04, 0.2))
# #
# print(balance(484, 0.04, 0.2))

# def balance(Value, annualInterestRate):
#     MonthlyPayment = 0
#     for i in range(12):
#         interest = annualInterestRate / 12
#         newValue = Value - MonthlyPayment
#         MonthlyPayment = newValue + Value
#         Value = newValue + (interest * newValue)
#     return MonthlyPayment
#
#
# print(balance(3329, 0.2))


# def payment(initial_amount, annualInterestRate, years):
#     n = years / 12
#     r = (annualInterestRate / 12)
#     monthly_payment = (r * initial_amount * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
#     return monthly_payment
#
#
# #
# #
# years = int(input('Input Years of the loan '))
# annualInterestRate = float(input('Input annual interest rate '))
# initial_amount = int(input('Input amount of loan '))
# #
# print('Monthly payment is : {}'.format(payment(initial_amount, annualInterestRate, years)))
#
# def payment(initial_amount, annualInterestRate):
#     for i in range(12):
#         monthlyInterestRate = (annualInterestRate / 12)
#         monthly_payment = monthlyInterestRate * (1 / (1 - (1 + monthlyInterestRate) ** (-12))) * initial_amount
#
#         # monthly_payment = (initial_amount * monthlyInterestRate * (1 + monthlyInterestRate)** (-12)) - 1
#
#     # monthly_payment = (monthlyInterestRate * initial_amount * ((1 + monthlyInterestRate) ** n)) / (((1 +
#     # monthlyInterestRate) ** monthlyInterestRate) - 1)
#     return round(monthly_payment / 10) * 10
#
#
# #
# #
# # years = int(input('Input Years of the loan '))
# annualInterestRate = float(input('Input annual interest rate '))
# initial_amount = int(input('Input amount of loan '))
# #
# print('Monthly payment is : {}'.format(payment(initial_amount, annualInterestRate)))
"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""


# interest = annualInterestRate / 12.0
# balance = balance - MonthlyPayment
# balance = balance + (interest * balance)
# MonthlyPayment = 0
#
# def payment(balance, annualInterestRate):

# def payment_amount(monthlyPaymentRate,init_balance,):
#     monthlyPaymentRate = 0
#     init_balance = balance
#     monthlyInterestRate = 0.2 / 12
#
#     while balance > 0:
#         for i in range(12):
#             balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
#         if balance > 0:
#             monthlyPaymentRate += 10
#             balance = init_balance
#         elif balance <= 0:
#             break
#     print('Lowest Payment:', monthlyPaymentRate)


def smallest_pay(initial_amount, annualInterestRate):
    for i in range(12):
        mid = initial_amount // 2
        monthlyInterestRate = (annualInterestRate / 12)
        monthly_payment = monthlyInterestRate * (1 / (1 - (1 + monthlyInterestRate) ** (-12))) * initial_amount
        if monthly_payment < initial_amount[mid]:
            return round(monthly_payment / 10) * 10
        return


annualInterestRate = float(input('Input annual interest rate '))
initial_amount = int(input('Input amount of loan '))
print('Monthly payment is : {}'.format(smallest_pay(initial_amount, annualInterestRate)))
