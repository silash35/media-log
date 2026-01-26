import csv
import json

from config import EntryBase


def warn(message: str):
    print(f'Warning: "{message}"')


def order(data, keys_in_order):
    ordered = {}

    # Add fields in order
    for field in keys_in_order:
        if field in data:
            ordered[field] = data[field]

    return ordered


def read_json(json_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def write_json(json_path: str, data: list[EntryBase]):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_csv(csv_path: str, data: list[EntryBase], fieldnames: list[str]):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
