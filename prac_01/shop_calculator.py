number_of_items = int(input("Number of items: "))
items = range(0, number_of_items)
total_price = float(0)

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
    items = range(0, number_of_items)

for item in items:
    item_price = float(input("Price of item: "))
    total_price += item_price
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
