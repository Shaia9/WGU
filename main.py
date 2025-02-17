"""
Brett Shaia 011542410
C950 Task 2: WGUPS ROUTING PROGRAM IMPLEMENTATION
"""
from data_input import DataManager
from Routing import Routing


def main():
    # Initialize data manger
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
    total_distance_1 = routing.simulate_delivery(routing.first_truck, '08:00:00')
    total_distance_2 = routing.simulate_delivery(routing.second_truck, '09:10:00')
    total_distance_3 = routing.simulate_delivery(routing.third_truck, '11:00:00')

    # Print results
    print(f"Distance for Truck 1: {total_distance_1} miles")
    print(f"Distance for Truck 2: {total_distance_2} miles")
    print(f"Distance for Truck 3: {total_distance_3} miles")
    print(f"Total combined miles: {total_distance_1 + total_distance_2 + total_distance_3}")

    if __name__ == "__main__":
        main()