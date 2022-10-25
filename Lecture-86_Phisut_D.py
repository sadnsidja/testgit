import csv

with open("hello.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} like {row[1]}, pet is {row[2]}.')
            line_count += 1