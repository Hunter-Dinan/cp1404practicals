"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = 0.15 * sales
    else:
        bonus = 0.10 * sales
    print("Bonus = {}".format(bonus))
    sales = float(input("Enter sales: $"))
print("Sales cannot be negative")