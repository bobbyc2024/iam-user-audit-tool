import csv

filename = "sample_users.csv"

with open(filename, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    users = list(reader)

print(f"Total user accounts: {len(users)}")
