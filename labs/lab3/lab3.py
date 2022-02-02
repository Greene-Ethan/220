"""
Name: Ethan Greene
Lab3.py

Problem: A python program that tracks traffic trends

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():
    roads_surveyed = eval(input("How many roads were surveyed?"))
    roads_surveyed = roads_surveyed + 1
    total_cars = 0
    total_cars_per_day = 0
    for days in range(1,roads_surveyed):
        print("How many days was road",days,"surveyed?", end = "\t")
        days_surveyed = eval(input(""))
        days_surveyed = days_surveyed + 1
        average_cars = 0
        for i in range(1, days_surveyed):
            print("How many cars were seen on day",i,"?", end = "\t")
            cars_per_day = eval(input(""))
            average_cars = average_cars + cars_per_day
        days_surveyed = days_surveyed - 1
        total_cars = total_cars + average_cars
        average_cars = round(average_cars / days_surveyed, 2)
        print("Road",days,"average vehicles a day:",average_cars)
    roads_surveyed = roads_surveyed - 1
    total_cars_per_day = round(total_cars / roads_surveyed,2)
    print("Total number of vehicles traveled on all roads:", total_cars)
    print("Average number of vehicles per road:",total_cars_per_day)

