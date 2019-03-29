"""
CP1404 - Practical 3 - broken_score
Enter score and check input range
"""


def main():
    score = float(input("Enter score: "))
    print("Your score is {}".format(score))
    print("That score is", determine_status(score))


def determine_status(score):
    while score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
