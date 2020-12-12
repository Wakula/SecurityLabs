def export_to_csv(file_name, lines):
    with open(file_name, "w") as csv_file:
        for line in lines:
            csv_file.write(f'{line}\n')
