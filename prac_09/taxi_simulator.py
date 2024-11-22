from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid option")
        return None

def drive_taxi(current_taxi):
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    try:
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0

def main():
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_cost = 0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        option = input(">>> ").lower()

        if option == "q":
            print(f"Total trip cost: ${total_cost:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break
        elif option == "c":
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif option == "d":
            trip_cost = drive_taxi(current_taxi)
            total_cost += trip_cost
            print(f"Bill to date: ${total_cost:.2f}")
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
