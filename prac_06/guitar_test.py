"""
CP1404 - Practical 6 - Guitars
Create and call class guitar.py
"""

from prac_06.guitar import Guitar


def main():
    """Test for guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    print("My guitar: {0}, first made in {1}".format(name, year))
    print()

    guitar = Guitar(name, year, cost)
    other = Guitar("Another guitar", 2012, 1000)

    print("{} get_age() - Expected {}. Got {}.".format(guitar.name, 97, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}.".format(other.name, 7, other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}.".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}.".format(other.name, False, other.is_vintage()))


main()
