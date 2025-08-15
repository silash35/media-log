import json
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
from utils import order
from validate import validate


def add_entry(new_entry: EntryBase, json_path: str, EntryType: Type[EntryBase]):
    # Load existing data
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Add the new entry
    data.append(new_entry)

    # Order the entries
    data = [order(line, EntryType.__annotations__.keys()) for line in data]

    # Save back to JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'Entry "{new_entry["Title"]}" added successfully!')


if __name__ == "__main__":
    EntryType = MovieEntry  # MovieEntry, ShowEntry, GameEntry

    new_entry: EntryType = EntryType(
        {
            "imdbID": "tt0000000",
            "Title": "Legally",
            "Year": 2025,
            "Rating10": 6.0,
            "Review": """Teste""",
            "FirstWatched": 2025,
            "LastWatched": 2025,
            "SafeForParents": False,
            "SafeForKids": False,
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
