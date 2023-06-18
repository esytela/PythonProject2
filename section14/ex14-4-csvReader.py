import csv

with open('차량관리.csv', 'r', newline='', encoding='UTF-8') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    for x in csv_reader:
        print(x)