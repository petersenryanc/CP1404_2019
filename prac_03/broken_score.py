"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print("Your score is {}".format(score))
    print("That score is", check_score(score))


def check_score(score):
    while score < 0 or score > 100:
        return "Invalid score. Please enter a score from 0 to 100."
    if score >= 90:
        return "excellent."
    elif score >= 50:
        return "passable."
    else:
        return "bad. Try again next time!"


main()
