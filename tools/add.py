from datetime import date
from typing import Type

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
from sync import json_to_csv
from utils import order, read_json, write_json
from validate import validate


def add_entry(new_entry: EntryBase, json_path: str, EntryType: Type[EntryBase]):
    data = read_json(json_path)

    # Add the new entry
    data.append(new_entry)

    # Order the entries
    ordered_data = []
    for line in data:
        ordered_line = order(line, EntryType.__annotations__.keys())

        if "Tags" in ordered_line and isinstance(ordered_line["Tags"], list):
            ordered_line["Tags"] = sorted(ordered_line["Tags"], key=str.lower)

        ordered_data.append(ordered_line)

    data = ordered_data

    # Save back to JSON
    write_json(json_path, data)
    print(f'Entry "{new_entry["Title"]}" added successfully!')


if __name__ == "__main__":
    EntryType = MovieEntry  # MovieEntry, ShowEntry, GameEntry

    new_entry: EntryType = EntryType(
        {
            "imdbID": "tt0000000",
            "Title": "Legally",
            "Year": 2026,
            "Rating10": 7.0,
            "Review": """Teste""",
            "SafeForParents": False,
            "ForKids": False,
            "Tags": ["Vi no Cinema"],
            "Watches": [date.today().isoformat()],  # YYYY-MM-DD
        }
    )

    if EntryType == MovieEntry:
        json_path = movies_json_path
        csv_path = movies_csv_path
    elif EntryType == ShowEntry:
        json_path = shows_json_path
        csv_path = shows_csv_path
    elif EntryType == GameEntry:
        json_path = games_json_path
        csv_path = games_csv_path
    else:
        raise ValueError("Unsupported EntryType")

    add_entry(new_entry, json_path, EntryType)
    validate(json_path, EntryType)
    json_to_csv(json_path, csv_path, EntryType)
