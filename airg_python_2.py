import csv
import random
import string
import concurrent.futures


def generate_rows(start, end):
    """Generates a list of rows with random data."""

    rows = []

    for i in range(start, end):
        random_number = str(random.randint(1, 10_000))
        choices_string = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(choices_string, k=10))
        rows.append([random_number, random_string])

    return rows


def generate_csv(filename, total_rows, chunk_size):
    """Generates a CSV with random data."""

    filename = filename.replace(" ", "_").replace(",", "_") + ".csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            # Divide the task into chunks and run them in parallel
            chunks = [executor.submit(generate_rows, i, i + chunk_size) for i in range(0, total_rows, chunk_size)]
            for future in concurrent.futures.as_completed(chunks):
                rows = future.result()
                writer.writerows(rows)
    
    print(f"CSV file with random data has been generated and saved as {filename}")


filename = input("Enter the filename: ")
total_rows = int(input("Enter the number of rows to generate: "))
chunk_size = int(input("Enter the chunk size: "))

generate_csv(
    filename=filename,
    total_rows=total_rows,
    chunk_size=chunk_size
)