import csv

from hashtable import HashTable
from package import Package


# Creating empty packages for csv data
class DataManager:
    def __init__(self):
        self.hash_map = HashTable()
        self.distance = []
        self.distance_data = []
        self.address_data = []
        self.first_delivery = []
        self.second_delivery = []
        self.third_delivery = []
        self.first_trip_truck1 = []
        self.first_trip_truck2 = []
        self.second_trip = []

    # Loading data from csv
    def load_package_data(self, filename):
        # Initiate delivery
        self.first_delivery = []  # departing at 8:00
        self.second_delivery = []  # departing at 9:10
        self.third_delivery = []  # delivers after 10:20 when package 9’s address is corrected

        # Define group constraint:
        group_constraints = {13, 14, 15, 16, 19, 20}

        print(f"Loading package data from {filename}...")
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 7:
                    print(f"Skipping row: {row}")
                    continue

                package_id = int(row[0].strip())
                address = row[1].strip()
                city = row[2].strip()
                state = row[3].strip()
                zip_code = row[4].strip()
                deadline = row[5].strip()
                weight = row[6].strip()
                notes = row[7].strip() if len(row) > 7 else ""

                # Create the Package object
                package_obj = Package(package_id, address, city, state, zip_code, deadline, weight, notes)
                self.hash_map.insert(package_id, package_obj)

                # ---- Assignment Logic (each truck max 16 packages) ----
                # Forced to Truck 3:
                if package_id == 9:
                    self.third_delivery.append(package_id)
                    continue

                # "Can only be on truck 2"
                if "Can only be on truck 2" in notes:
                    if len(self.second_delivery) < 16:
                        self.second_delivery.append(package_id)
                    continue

                # "Delayed on flight"
                if "Delayed on flight" in notes:
                    if len(self.second_delivery) < 16:
                        self.second_delivery.append(package_id)
                    else:
                        self.third_delivery.append(package_id)
                    continue

                # Time-sensitive packages
                if deadline != "EOD":
                    if len(self.first_delivery) < 16:
                        self.first_delivery.append(package_id)
                    elif len(self.second_delivery) < 16:
                        self.second_delivery.append(package_id)
                    else:
                        self.third_delivery.append(package_id)
                    continue

                # Group-constrained packages:
                if package_id in group_constraints:
                    if any(pid in self.first_delivery for pid in group_constraints):
                        if len(self.first_delivery) < 16:
                            self.first_delivery.append(package_id)
                        elif len(self.second_delivery) < 16:
                            self.second_delivery.append(package_id)
                        else:
                            self.third_delivery.append(package_id)
                    else:
                        if len(self.first_delivery) + len(group_constraints) <= 16:
                            self.first_delivery.append(package_id)
                        elif len(self.second_delivery) + len(group_constraints) <= 16:
                            self.second_delivery.append(package_id)
                        else:
                            self.third_delivery.append(package_id)
                    continue

                # For all remaining packages (deadline == "EOD" and no special note)
                if len(self.first_delivery) < 16:
                    self.first_delivery.append(package_id)
                elif len(self.second_delivery) < 16:
                    self.second_delivery.append(package_id)
                else:
                    self.third_delivery.append(package_id)

    """
    Lookup function (Takes Package_id and returns package object)
    """
    def lookup_package(self, package_id):
        package_obj = self.hash_map.retrieve_value(package_id)
        if package_obj is None:
            print(f"{package_id} is not found: Try re-entering package ID")
            return None
        return package_obj

    # Load distance
    def load_distance_data(self, filename):
        print(f"Loading distance data from {filename}...")
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                cleaned_row = [x.strip() for x in row]
                try:
                    self.distance_data.append([float(x) if x else 0.0 for x in cleaned_row])
                except ValueError:
                    print(f"Skipping row: {row}")
        print(f"Loaded distance data: {self.distance_data}")


    # Load address
    def load_address_data(self, filename):
        print(f"Loading address data from {filename}...") # Debugging
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.address_data.append(row)

    # Calculate distance
    def get_distance(self, row, col):
        distance = self.distance_data[row][col]
        if distance == 0.0:
            distance = self.distance_data[col][row]
        return distance

    # index by Package_id
    def get_address_index(self, package_id):
        package = self.hash_map.retrieve_value(package_id)
        if package:
            address = package.address
            for index, row in enumerate(self.address_data):
                if len(row) > 1:
                    if address.strip().lower() == row[2].strip().lower():
                        return index
            # Address not found
            print(f"Address not found for package: {package_id}")
            return -1

