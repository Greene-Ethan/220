
"""
print("hello, world!", end=" ")
print("good to see ya :)")
name, age = eval(input("hello!\nenter your name and age!"))
print("good to see you",name,"you are",age)

for i in [1, 2, 3]:
    print(i)
    print(i+3)
print(i)

for i in range(10):
    print(i,end = " ")
"""
# Calculate balance of bank account after 10 years of compounding interest
#starting balance, interest rate, after 10 years what's your balance?

principle = eval(input("How much money is in your account?"))
apr = eval(input("What's your interest rate?"))

for i in range(10):
    principle = principle * (1+apr)
print("your new balance after ten years is",principle)
