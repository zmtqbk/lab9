import csv
filename = r'C:\Users\Aidar\Desktop\pp2\Lab10\phonebook\book.csv'
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        surname, name, number = row
        print(surname, name, number)