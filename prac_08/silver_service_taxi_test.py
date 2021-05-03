"""Test program for SilverServiceTaxi class."""

from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi('Hummer', 200, 4)
print(hummer)

silver_service_taxi_1 = SilverServiceTaxi('Silver Service Taxi', 18, 2)
silver_service_taxi_1.drive(18)
print(silver_service_taxi_1)
fare = silver_service_taxi_1.get_fare()
print(f"{silver_service_taxi_1.name} current fare price is ${fare:.2f}")
