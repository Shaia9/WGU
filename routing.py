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
                if address_index == -1:
                    continue

                distance = self.data_manager.get_distance(current_location, address_index)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_package = package_id


            if nearest_package is not None and nearest_package in remaining_packages:
                    route.append(nearest_package)
                    remaining_packages.remove(nearest_package)
                    current_location = self.data_manager.get_address_index(nearest_package)
            else:
                    print(f"No package found Skipping.") # Debugging
                    break

        # Assigns truck number to route
        if truck_number == 1:
            self.first_truck = route
        elif truck_number == 2:
            self.second_truck = route
        elif truck_number == 3:
            self.third_truck = route

    # Delivery
    """ 
     Time Complexity: O(n): one for loop
    """
    def simulate_delivery(self, truck_route, departure_time, truck_number):
        current_time = datetime.datetime.strptime(departure_time, '%H:%M:%S')
        total_distance = 0.0
        # Set to start at hub
        current_location = 0

        for package_id in truck_route:
            self.data_manager.hash_map.retrieve_value(package_id)
            address_index = self.data_manager.get_address_index(package_id)
            distance = self.data_manager.get_distance(current_location, address_index)
            total_distance += distance

            # Calc delivery time 18mph == .3 miles/min
            travel_time = distance / 0.3
            current_time += datetime.timedelta(minutes=travel_time)

            # Update status
            package = self.data_manager.hash_map.retrieve_value(package_id)
            package.status = f"Delivered at {current_time.strftime('%H:%M:%S')}"
            package.truck = truck_number
            self.data_manager.hash_map.update(package_id, package)
            current_location = address_index

        return total_distance

    # Method for checking delivery status
    def display_package_status(self, user_time):
        user_time = datetime.datetime.strptime(user_time, '%H:%M:%S')

        # Check status of all packages/statuses
        all_packages = self.first_truck + self.second_truck + self.third_truck
        for package_id in all_packages:
            package = self.data_manager.hash_map.retrieve_value(package_id)
            package_status = package.status
            truck_assigned = package.truck if package.truck is not None else "Unknown truck"

            # Truck departure times
            truck_departure_times = {1: "08:00:00", 2: "9:05:00", 3: "10:20:00"}
            departure_time = datetime.datetime.strptime(truck_departure_times.get(truck_assigned, "23:59:59"), '%H:%M:%S')

            if "Delivered at" in package_status:
                delivery_time = datetime.datetime.strptime(package_status.split("at ")[1], '%H:%M:%S')
                if delivery_time <= user_time:
                   package_status = f"Delivered at {delivery_time.strftime('%H:%M:%S')}"
                elif user_time >= departure_time:
                    package_status = "En-route"
                else:
                    package_status = "at the hub"
            else:
                if user_time >= departure_time:
                    package_status = "En-route"
                else:
                    package_status = "At the hub"

            # Displays package status and truck info
            print(f"Package: {package_id} - Status: {package_status} - Assigned to Truck: {truck_assigned}")