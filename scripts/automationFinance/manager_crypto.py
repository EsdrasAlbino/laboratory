import csv
file_variation = "crypto_report_all_period.csv"
file = f"csv_crypto/{file_variation}"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
