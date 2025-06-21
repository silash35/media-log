from config import movies_csv_path, movies_json_path
import json
import csv


def json_to_csv(json_file: str, csv_file: str) -> None:
    # Load data from JSON
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Use keys from first object as column headers
    fieldnames = list(data[0].keys())

    # Write CSV file
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file '{csv_file}' synchronized successfully!")


if __name__ == "__main__":
    json_to_csv(movies_json_path, movies_csv_path)
