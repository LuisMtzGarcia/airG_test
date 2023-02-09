import csv
import random
import string

def generate_csv():
    """Generates a CSV with random data."""

    filename = input("Enter the filename: ").replace(" ", "_").replace(",", "_") + ".csv"

    chunk_size = 10_000
    total_rows = 1_000_000


    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Starting point, endpoint, step size.
        for i in range(0, total_rows, chunk_size):
            rows = []
            for j in range(chunk_size):
                if i + j >= total_rows:
                    break
                random_number = str(random.randint(1, 10000))
                choices_string = string.ascii_letters + string.digits
                random_string = ''.join(random.choices(choices_string, k=10))
                rows.append([random_number, random_string])
            writer.writerows(rows)
    
    print(f"CSV file with random data has been generated and saved as {filename}")


generate_csv()