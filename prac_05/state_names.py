"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                "WA": "Western Australia", "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# Print all states.
for state in CODE_TO_NAME:
    print("{:3} is {}".format(state, CODE_TO_NAME[state]))

state_code = input("Enter short state: ")
while state_code != "":
    if state_code.upper() in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code.upper()])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
