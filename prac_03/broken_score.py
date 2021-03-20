"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    grade = calculate_grade(score)
    print(grade)

    random_score = random.randint(0, 100)
    random_score_grade = calculate_grade(random_score)
    print(random_score_grade)


def calculate_grade(score):
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50 and score >= 0:
        return "Bad"
    else:
        return "Invalid score"


main()
