import csv
import datetime


# READ CSV
with open('./CSV/distance_data.csv') as cvs_distance:
    distance_csv = list(csv.reader(cvs_distance, delimiter=','))
with open('./CSV/name_data.csv') as cvs_name:
    distance_name_csv = list(csv.reader(cvs_name, delimiter=','))

    # Get address
    def get_address():
        return distance_name_csv

    # Get total distance
    def retrieve_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)

    # Current distance
    def current_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return float(distance)

    # Distance per truck
    def get_distance(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.splint(':')
            total += datetime.timedelta(hours=int(hrs),minutes=int(mins), seconds=int(secs))
        return total

    first_truck = []
    first_truck_indice = []
    second_truck = []
    second_truck_indice = []
    third_truck = []
    third_truck_indice = []

    def shortest_route (_list, num, curr_location):
        if not len(_list):
            return _list

        lowest_value = 50.0
        location = 0

        for i in _list:
            value = int(i[1])
            if get_distance(curr_location, value) <= lowest_value:
                lowest_value = current_distance( curr_location, value)
                location = value

        for i in _list:
            if current_distance(curr_location, int(i[1])) == lowest_value:
                if num == 1:
                    first_truck.append(i)
                    first_truck_indice.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    shortest_route(_list, 1, curr_location)
                elif num == 2:
                    second_truck.append(i)
                    second_truck_indice.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    shortest_route((_list, 2, curr_location))
                elif num == 3:
                    third_truck.append(i)
                    third_truck_indice.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    shortest_route(_list, 3, curr_location)

    # Instant of 0 for first index
    first_truck_indice.insert (0, '0')
    second_truck_indice.insert(0, '0')
    third_truck_indice.insert(0, '0')

    # Return values
    def first_truck_value():
        return first_truck_indice

    def list_first_truck():
        return first_truck

    def second_truck_value():
        return second_truck_indice

    def list_second_truck():
        return second_truck

    def third_truck_value():
        return third_truck_indice

    def list_third_truck():
        return third_truck


