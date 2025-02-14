import CSV
import datetime
import csv

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

