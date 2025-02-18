import csv
from hashtable import HashTable
from datetime import datetime

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

    # Loading data from csv
    def load_package_data(self, filename):
        print(f"Loading package data from {filename}...")
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 7:
                    print (f"Skipping row: {row}")
                    continue
                package_id = int(row[0].strip())
                address = row[1].strip()
                city = row[2].strip()
                state = row[3].strip()
                zip_code = row[4].strip()
                deadline = row[5].strip()
                weight = row[6].strip()
                notes = row[7].strip() if len(row) > 7 else ""

                package_data = {
                    "address" : address,
                    "city" : city,
                    "state" : state,
                    "zip" : zip_code,
                    "deadline" : deadline,
                    "weight" : weight,
                    "notes" : notes,
                    # Set default status
                    "status" : "Not shipped: At hub"
                }

                # Insert into Hash Table
                self.hash_map.insert(package_id, package_data)

                #Assign based on constraints
                if '84104' in zip_code and '10:30' not in deadline:
                    self.third_delivery.append(package_id)
                elif deadline != 'EOD' and ('Must' in notes or "None" in notes):
                    self.first_delivery.append(package_id)
                else:
                    if len(self.second_delivery) < len(self.third_delivery):
                        self.second_delivery.append(package_id)
                    else:
                        self.third_delivery.append(package_id)

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
            address = package['address']
            for index, row in enumerate(self.address_data):
                if len(row) > 1:
                    if address.strip().lower() == row[2].strip().lower():
                        return index
            # Address not found
            print(f"Address not found for package: {package_id}")
            return -1
