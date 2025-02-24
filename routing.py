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
            package = self.data_manager.hash_map.retrieve_value(package_id)
            address_index = self.data_manager.get_address_index(package_id)
            distance = self.data_manager.get_distance(current_location, address_index)
            total_distance += distance

            # Calc delivery time 18mph == .3 miles/min
            travel_time = distance / 0.3
            current_time += datetime.timedelta(minutes=travel_time)

            # Special handling: if package is delayed on flight, wait until 09:05.
            if "Delayed on flight" in package.notes:
                delay_time = datetime.datetime.strptime("09:05:00", "%H:%M:%S")
                if current_time < delay_time:
                    current_time = delay_time

            # Special handling for package 9 on Truck 3:
            if package_id == 9 and truck_number == 3:
                cutoff_time = datetime.datetime.strptime("10:20:00", "%H:%M:%S")
                if current_time < cutoff_time:
                    current_time = cutoff_time
                # Update the address only when it's time for delivery.


            package.delivery_time = current_time
            package.truck = truck_number
            self.data_manager.hash_map.update(package_id, package)

            current_location = address_index

        return total_distance

    # Method for checking delivery status
    def display_package_status(self, user_time):
        user_dt = datetime.datetime.strptime(user_time, '%H:%M:%S')

        # Check status of all packages/statuses
        all_packages = self.data_manager.first_delivery + self.data_manager.second_delivery + self.data_manager.third_delivery


        truck_departure_times = {1: "08:00:00", 2: "09:10:00", 3: "10:20:00"}

        for package_id in all_packages:
            package = self.data_manager.hash_map.retrieve_value(package_id)

            # For package 9: if user time is >= 10:20, update the address for display.
            if package.package_id == 9:
                cutoff_dt = datetime.datetime.strptime("10:20:00", "%H:%M:%S")
                if user_dt >= cutoff_dt:
                    package.address = "410 S State St"  # Correct address

            # Determine the truck's departure time.
            truck_assigned = package.truck if package.truck is not None else None
            if truck_assigned in truck_departure_times:
                dep_time = datetime.datetime.strptime(truck_departure_times[truck_assigned], '%H:%M:%S')
            else:
                dep_time = None

            # Now, compute status dynamically:
            # If the package has a delivery_time, then:
            #  - If user_dt >= delivery_time: it's Delivered.
            #  - Else if user_dt is after departure time: it's En-route.
            #  - Otherwise: it's At the hub.
            if package.delivery_time is not None:
                if user_dt >= package.delivery_time:
                    computed_status = f"Delivered at {package.delivery_time.strftime('%H:%M:%S')}"
                elif dep_time is not None and user_dt >= dep_time:
                    computed_status = "En-route"
                else:
                    computed_status = "At the hub"
            else:
                computed_status = "At the hub"

            # Print all package details.
            print(f"Package ID: {package.package_id} - "
                  f"Address: {package.address} - "
                  f"City: {package.city} - State: {package.state} - Zip: {package.zip_code} - "
                  f"Deadline: {package.deadline} - Weight: {package.weight} - "
                  f"Notes: {package.notes} - "
                  f"Status at {user_time}: {computed_status} - "
                  f"Assigned to Truck: {truck_assigned if truck_assigned is not None else 'Unknown'}")