"""
CP1404 - Practical 6 - Guitars
"""

YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar"""
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 2018-year

    def __str__(self):
        """Return string representation of guitar"""
        return "{}({}): ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get current age of guitar from constant YEAR"""
        return YEAR - self.year

    def is_vintage(self):
        """Test whether guitar is vintage or not"""
        return self.age >= VINTAGE_AGE
