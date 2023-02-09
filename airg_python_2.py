import csv
import random
import string

def generate_csv():
    """Generates a CSV with random data."""

    filename = input("Enter the filename: ").replace(" ", "_").replace(",", "_") + ".csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for i in range(100):
            random_number = str(random.randint(1, 10000))
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            writer.writerow([random_number, random_string])
    
    print(f"CSV file with random data has been generated and saved as {filename}")


generate_csv()