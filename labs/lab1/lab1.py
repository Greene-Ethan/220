"""
Name: Ethan Greene
Lab1.py

Problem: A computing program to figure out the monthly interest rates on credit cards.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def interest_rate():
    annual_interest_rate = eval(input("What's the annual interest rate?"))
    billing_cycle = eval(input("How many days are in a billing cycle?"))
    previous_net_balance = eval(input("What was the previous net balance?"))
    payment_amount = eval(input("What is the amount your paying?"))
    day_of_cycle = eval(input("What day of the cycle is it?"))

    step_1 = previous_net_balance * billing_cycle
    step_2 = payment_amount * (billing_cycle - day_of_cycle)
    step_3 = step_1 - step_2
    average_daily_balance = step_3 / billing_cycle

    annual_interest_rate = annual_interest_rate / 100
    monthly_interest = average_daily_balance * (annual_interest_rate / 12)
    monthly_interest = round(monthly_interest,2)
    print("Your monthly interest is $",monthly_interest)
