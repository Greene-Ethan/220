"""
Name: Ethan Greene
sales_person.py

Problem: creating a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales = self.sales + [sale]

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if sum(self.sales) >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if sum(self.sales) > other:
            return 1
        elif sum(self.sales) < other:
            return -1
        else:
            return 0

    def __str__(self):
        return "{}-{}:{}".format(self.employee_id, self.name, sum(self.sales))
