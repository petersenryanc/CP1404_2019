"""
CP1404 - Practical 6 - Guitars
"""

YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 2018-year

    def __str__(self):
        return "{}({}): ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return YEAR - self.year

    def is_vintage(self):
        return self.age >= VINTAGE_AGE
