import csv
from Hashtable import HashTable

# Creating empty packages for csv data
class DataManager:
    def __init__(self):
        self.hash_map = HashTable()
        self.distance = []
        self.address_data = []
        self.first_delivery = []
        self.second_delivery = []
        self.third_delivery = []

    # Loading data from csv
    def load_package_data(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                package_id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]
                deadline = row[5]
                weight = row[6]
                notes = row[7]

                package_data = {
                    "address" : address,
                    "city" : city,
                    "state" : state,
                    "zip" : zip_code,
                    "deadline" : deadline,
                    "weigh" : weight,
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
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.distance_data.append([float(x) if x else 0.0 for x in row])

    # Load address
    def load_address_data(self, filename):
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
        address = package['address']
        for index, row in enumerate(self.address_data):
            return index
            # Address not found
            return -1