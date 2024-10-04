import csv
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Specify the CSV file path
csv_file_path = "contacts_data.csv"

# Create CSV file with headers
with open(csv_file_path, "w", newline="") as csvfile:
    fieldnames = ["name", "address", "email", "phone", "date_of_birth"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Generate 100 fake records
    for _ in range(100):
        writer.writerow(
            {
                "name": fake.name(),
                "address": fake.address().replace("\n", ", "),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "date_of_birth": fake.date_of_birth(
                    minimum_age=18, maximum_age=90
                ).strftime("%Y-%m-%d"),
            }
        )

print(f"CSV file generated at {csv_file_path}")
