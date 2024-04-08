import csv
file_variation = "relatorio-consolidado-anual-2023.csv"
file = f"csv_investing/{file_variation}"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
