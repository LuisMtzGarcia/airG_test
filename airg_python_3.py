import csv

def normalize_csv(filename):
    filename_csv = filename + ".csv"
    with open(filename_csv, 'r') as pipe_file, open(f'{filename}_comma.csv', 'w', newline='') as comma_file:
        reader = csv.reader(pipe_file, delimiter='|')
        writer = csv.writer(comma_file)

        for row in reader:
            print(row)
            writer.writerow(row)


normalize_csv("pipe")