import csv

with open('../mappings/players.csv', 'r') as file:
    # Create a DictReader object
    reader = csv.DictReader(file)

    # Convert the reader to a list of dictionaries
    dict_list = list(reader)

print(dict_list)