"""
Name: Ethan Greene
sales_force.py

Problem: creating a sales force

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file):
        opener = open(file, "r")
        line = opener.readline()
        index_val = 0
        while line != "":
            line = line.strip()
            line = line.split(",")
            create_salesperson = SalesPerson(line[0],line[1])
            line[2] = line[2].strip()
            split_sales = line[2].split(" ")
            for sales in split_sales:
                create_salesperson.enter_sale(sales)
            line = opener.readline()
            self.sales_people += [create_salesperson]
        return self.sales_people

    def quota_report(self, quota):
        final_list = []
        for salespersons in self.sales_people:
            if salespersons.met_quota(quota):
                final_list += [salespersons] + [True]
            else:
                final_list += [salespersons] + [False]
        return final_list

    def top_seller(self):
        most_sales = [self.sales_people[0]]
        for salespersons in self.sales_people:
            if salespersons.total_sales() > most_sales[0].total_sales():
                most_sales = [salespersons]
            elif salespersons.total_sales() == most_sales.total_sales:
                most_sales = [salespersons] + [most_sales]

    def individual_sales(self, employee_id):
        for salespersons in self.sales_people:
            if salespersons.get_id() == employee_id:
                return salespersons
        return None

    def get_sale_frequency(self):
        pass





