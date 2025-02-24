"""
Brett Shaia 011542410
C950 Task 2: WGUPS ROUTING PROGRAM IMPLEMENTATION
"""
import datetime
from data_manager import DataManager
from routing import Routing

# Input for time to get a specific time for package status
def ask_user_for_time(routing_instance):
    while True:
        user_time = input("Enter a time (HH:MM:SS) for package status or type 'exit' to quit: ")
        if user_time.lower() == 'exit':
            break

        try:
            datetime.datetime.strptime(user_time, "%H:%M:%S")
            routing_instance.display_package_status(user_time)
        except ValueError:
            print(f"Invalid format. Pleaser enter time in HH:MM:SS format.")

# Input for package ID lookup
def lookup_package(data_manager):
    try:
        package_id = int(input("Enter a package ID to lookup: "))
        package = data_manager.lookup_package(package_id)
        if package:
            print(package)
    except ValueError:
        print ("Invalid. Please enter a valid integer for the package ID.")

def main():
    # Initialize data manager
    data_manager = DataManager()
    data_manager.load_package_data('./CSV/input_data.csv')
    data_manager.load_distance_data('./CSV/distance_data.csv')
    data_manager.load_address_data('./CSV/name_data.csv')

    # Initialize routing file
    routing = Routing(data_manager)

    # Assign to trucks
    routing.nearest_neighbor(data_manager.first_delivery, 1)
    routing.nearest_neighbor(data_manager.second_delivery, 2)
    routing.nearest_neighbor(data_manager.third_delivery, 3)

    # Delivery simulation
    total_distance_1 = routing.simulate_delivery(routing.first_truck, '08:00:00', 1)
    total_distance_2 = routing.simulate_delivery(routing.second_truck, '09:10:00', 2)
    total_distance_3 = routing.simulate_delivery(routing.third_truck, '11:00:00', 3)

    # Print results
    print(f"Distance for Truck 1: {total_distance_1} miles")
    print(f"Distance for Truck 2: {total_distance_2} miles")
    print(f"Distance for Truck 3: {total_distance_3} miles")
    print(f"Total combined miles: {total_distance_1 + total_distance_2 + total_distance_3}")

    # Interactive menu
    while True:
        print("\nSelect an option:\n")
        print("1: Check status for packages at a given time\n")
        print("2: Lookup package detail by ID\n")
        print("3: Exit\n")
        choice = input("Enter (1, 2, or 3): ")
        if choice == "1":
            ask_user_for_time(routing)
        elif choice == "2":
            lookup_package(data_manager)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()
