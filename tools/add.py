from config import movies_csv_path, movies_json_path, MovieEntry
import json
from sync import json_to_csv
from validate import validate
from utils import order


def add_movie_entry(new_entry: MovieEntry, json_file_path: str):
    # Load existing data
    with open(json_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Add the new entry
    data.append(new_entry)

    # Order the entries
    data = [order(line, MovieEntry.__annotations__.keys()) for line in data]

    # Save back to JSON
    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'Entry "{new_entry["Title"]}" added successfully!')


if __name__ == "__main__":
    new_movie: MovieEntry = MovieEntry(
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

    add_movie_entry(new_movie, movies_json_path)
    validate(movies_json_path)
    json_to_csv(movies_json_path, movies_csv_path)
