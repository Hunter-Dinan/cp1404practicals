TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_input = int(input("Which tariff? 11 or 31: "))

while tariff_input != 11 and tariff_input != 31:
    print("Invalid tariff input")
    tariff_input = int(input("Which tariff? 11 or 31: "))

if tariff_input == 11:
    tariff_input = TARIFF_11
elif tariff_input == 31:
    tariff_input = TARIFF_31

daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_days_in_billing = float(input("Enter number of billing days: "))
bill = (tariff_input) * daily_use_in_kWh * number_of_days_in_billing
print("Estimated bill: {:.2f}".format(bill))
