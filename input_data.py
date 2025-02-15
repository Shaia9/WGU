import csv
from Hashtable import HashTable

# Read CSV files
with (open('./CSV/input_data.csv') as csvfile):
    read_csv = csv.reader(csvfile, delimiter = ',')

    # Instance of HashTable class
    hash_map = HashTable()
    first_delivery = []
    second_delivery = []
    third_delivery = []

    # Insert from CSV to Hash Table
    for row in read_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = ''

        value = [id, address_location, address, city, state, zip, delivery, size, note, delivery_start, delivery_status]

        # Conditional statements to determine which truck to use

        # Fix incorrect package
        if '84104' in value[5] and '10:30' not in value[6]:
            third_delivery.append(value)

        # Set first truck
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_delivery.append(value)

        # Set second truck
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            second_delivery.append(value)

        # Check packages
        if value not in first_delivery and value not in second_delivery and value not in third_delivery:
            second_delivery.append(value) if len(second_delivery) < len(third_delivery) else third_delivery.append(value
                                                                                                                   )
        # Retrieve packages from first delivery
        def retrieve_first_delivery():
            return first_delivery

        # Retrieve packages from second delivery
        def retrieve_second_delivery():
            return second_delivery

        # Retrieve packages from third delivery
        def retrieve_third_delivery():
            return third_delivery

        # Retrieve all packages
        def retrieve_all():
            return hash_map