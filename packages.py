import distance
import input_data
from input_data import first_delivery, second_delivery, third_delivery

# Create empty lists
first_delivery = []
second_delivery = []
third_delivery = []
first_distance = []
second_distance = []
third_distance = []

# Time for departure
first_departure = ['8:00:00']
second_departure = ['9:10:00']
third_departure = ['11:00:00']

# Set departure times
for index, value in enumerate(input_data.retrieve_first_delivery()):
    input_data.retrieve_first_delivery()[index][9] = first_departure[0]
    first_delivery.append(input_data.retrieve_first_delivery()[index])

for index, outer in enumerate(first_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            first_distance.append(outer[0])
            first_delivery[index][1] = inner[0]

# Call algorithm to sort packages for first truck
distance.shortest_route(first_delivery, 1, 0)
total_distances_1 = 0

# Total distance of first truck and packages
for index in range(len(distance.first_truck_value())):
    try:
        total_distances_1 = distance.get_distance(int(distance.first_truck_value()[index]), int (distance.first_truck_value()[index + 1]), total_distances_1)
        deliver_package = distance.get_time(distance.get_distance(int(distance.first_truck_value()[index]), int(distance.first_truck_value()[index + 1])), first_departure)distance.list_first_truck()[index][10] = (str(deliver_package))
        input_data.get_hash_map().update(int(distance.first_truck_value()[index][0]), first_delivery)
    except IndexError:
        pass



