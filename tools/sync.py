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
from utils import read_json, write_csv


def json_to_csv(json_file: str, csv_file: str, EntryType: Type[EntryBase]):
    data = read_json(json_file)

    #  Use type hints from the TypedDict class as column headers
    fieldnames = list(get_type_hints(EntryType).keys())

    # Add FirstWatched and LastWatched to facilitate sort
    if "Watches" in fieldnames:
        fieldnames.remove("Watches")
        fieldnames.append("FirstWatched")
        fieldnames.append("LastWatched")

        processed_data: list[EntryBase] = []
        for entry in data:
            row = entry.copy()

            watches = row.pop("Watches", None)
            if isinstance(watches, list) and watches:
                row["FirstWatched"] = watches[0]
                row["LastWatched"] = watches[-1]

            processed_data.append(row)
    else:
        processed_data = data

    # Write CSV file
    write_csv(csv_file, processed_data, fieldnames)
    print(f"CSV file '{csv_file}' synchronized successfully!")


if __name__ == "__main__":
    json_to_csv(movies_json_path, movies_csv_path, MovieEntry)
    json_to_csv(shows_json_path, shows_csv_path, ShowEntry)
    json_to_csv(games_json_path, games_csv_path, GameEntry)
