#for i in range(5):
#    for j in range(5):
#        print(i,j, end =' - ')
#    print()

""" 
Data Types:
"Hello, world!" - string 
3 - int/integer -/+ but whole numbers (choose over binary)
3.0 - float/floating point -/+ but decimals (hard to convert to binary)
% = = Use to check if it's even or odd with variable % 2 and if it's 0 even if 1 odd
    great for repeating things


x = 10.5
y = .86
z = 62
a = (x + y) * z
print(a)
b = x * z + y * z
print(b)

my_range = range(20, 3, -2)
#print(list(my_range))

my_sum = 0
for i in range(101):
    my_sum = my_sum + i
print(my_sum)

user_input = eval(input("What value would you like?"))
fact = 1
for i in range(user_input, 0, -1):
    fact = fact * i
print(fact)

import math
variable_a = eval(input("What's the value of a?"))
variable_b = eval(input("What's the value of b?"))
variable_c = eval(input("What's the value of c?"))

numbers = math.sqrt((variable_b ** 2) - 4 * variable_a * variable_b)
negative_answer = (-variable_b - numbers) / (2 * variable_a)
positive_answer = (-variable_b + numbers) / (2 * variable_a)
print("x =",negative_answer,",",positive_answer)
"""
int()
age = 3.5
print(type(age))
int_age = int(age)
float(3)
stringy = "3"
stringy_2 = int(age)

