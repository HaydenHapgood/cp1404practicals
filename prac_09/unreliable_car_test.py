
from unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Unreliable Car", 100, 50)

distance_driven = unreliable_car.drive(40)
print(f"Attempted to drive Unreliable Car 40 km. Actual distance driven: {distance_driven} km")
print(unreliable_car)
