import csv
import json
from typing import Type, get_type_hints

from config import (
    EntryBase,
    GameEntry,
    MovieEntry,
    ShowEntry,
    games_csv_path,
    games_json_path,
    movies_csv_path,
    movies_json_path,
    shows_csv_path,
    shows_json_path,
)


def json_to_csv(json_file: str, csv_file: str, EntryType: Type[EntryBase]) -> None:
    # Load data from JSON
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    #  Use type hints from the TypedDict class as column headers
    fieldnames = list(get_type_hints(EntryType).keys())

    # Write CSV file
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file '{csv_file}' synchronized successfully!")


if __name__ == "__main__":
    json_to_csv(movies_json_path, movies_csv_path, MovieEntry)
    json_to_csv(shows_json_path, shows_csv_path, ShowEntry)
    json_to_csv(games_json_path, games_csv_path, GameEntry)
