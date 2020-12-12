import csv


def export_to_csv(file_name, data):
    with open(file_name, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
