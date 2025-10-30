import csv

try:
    filename = input("Enter file name: ")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except csv.Error:
    print("Error: The file you entered is not a valid CSV file.")