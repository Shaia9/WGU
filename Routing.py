from data_input import DataManager
import datetime

class Routing:
    # Initialize data from data_manager
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.first_truck = []
        self.second_truck = []
        self.third_truck = []

    """
    Nearest neighbor algorithm
    Time Complexity : 0(n^2), where n is the number of packages in truck.
    """
    def nearest_neighbor(self, truck_packages, truck_number):
        route = []
        # Default index of 0
        current_location = 0
        remaining_packages = truck_packages.copy()

        while remaining_packages:
            nearest_distance = float('inf')
            nearest_package = None

            for package_id in remaining_packages:
                address_index = self.data_manager.get_address_index(package_id)
                distance = self.data_manager.get_distance(current_location, address_index)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_package = package_id

                route.append(nearest_package)
                remaining_packages.remove(nearest_package)
                current_location = self.data_manager.get_address_index(nearest_package)

        if truck_number == 1:
            self.first_truck = route
        elif truck_number == 2:
            self.second_truck = route
        elif truck_number == 3:
            self.third_truck = route

    # Delivery
    # Time Complexity: O(n): one for loop
    def simulate_delivery(self, truck_route, departure_time):
        current_time = datetime.datetime.strptime(departure_time, '%H:%M:%S')
        total_distance = 0.0
        # Set to start at hub
        current_location = 0

        for package_id in truck_route:
            address_index = self.data_manager.get_address_index(package_id)
            distance = self.data_manager.get_distance(current_location, address_index)
            total_distance += distance

            # Calc delivery time 18mph == .3 miles/min
            travel_time = distance / 0.3
            current_time += datetime.timedelta(minutes=travel_time)

            # Update status
            package = self.data_manager.hash_map.retrieve_value(package_id)
            package["status"] = f"Delivered at {current_time.strftime('%H:%M:%S')}"
            self.data_manager.hash_map.update(package_id, package)
            current_location = address_index

        return total_distance

