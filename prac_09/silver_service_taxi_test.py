

from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 2)

hummer.drive(18)
expected_fare = (hummer.price_per_km * 18) + hummer.flagfall
assert hummer.get_fare() == expected_fare, f"Expected fare to be {expected_fare}, but got {taxi.get_fare()}"
print(f"Fare for the trip: ${hummer.get_fare():.2f}")


