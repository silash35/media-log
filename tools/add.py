from lib.config import (
    GameEntry,
    MovieEntry,
    ShortEntry,
    ShowEntry,
    games_csv_path,
    games_json_path,
    movies_csv_path,
    movies_json_path,
    shorts_csv_path,
    shorts_json_path,
    shows_csv_path,
    shows_json_path,
)
from lib.imdb import get_title_and_year
from lib.utils import add_entry, today
from sync import json_to_csv
from validate import validate

if __name__ == "__main__":
    imdb_id = "tt32890033"

    EntryType = MovieEntry  # MovieEntry, ShowEntry, GameEntry, ShortEntry

    title, year = get_title_and_year(imdb_id)

    new_entry: EntryType = EntryType(
        {
            "imdbID": imdb_id,
            "Title": title,
            "Year": year,
            "Rating10": 7.0,
            "Review": """Teste""",
            "SafeForParents": False,
            "ForKids": False,
            "Tags": ["Vi no Cinema"],
            "Watches": [today()],  # YYYY-MM-DD
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
    elif EntryType == ShortEntry:
        json_path = shorts_json_path
        csv_path = shorts_csv_path
    else:
        raise ValueError("Unsupported EntryType")

    add_entry(new_entry, json_path, EntryType)
    validate(json_path, EntryType)
    json_to_csv(json_path, csv_path, EntryType)
