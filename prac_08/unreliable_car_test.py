"""Test UnreliableCar class methods."""

from unreliable_car import UnreliableCar

car_1 = UnreliableCar('Car 1', 100, 84.3)
print(car_1)
car_1.add_fuel(1500)
print(car_1)
car_1.drive(1243)
print(car_1)
car_1.drive(30)
print(car_1)
car_1.drive(30)
print(car_1)
car_1.drive(30)
print(car_1)
car_1.drive(30)
print(car_1)
