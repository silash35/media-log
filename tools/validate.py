from typing import get_type_hints, Union
import json
from config import MovieEntry, movies_json_path
from utils import warn


def validate(json_file_path: str) -> None:
    # Load JSON data
    with open(json_file_path, "r", encoding="utf-8") as f:
        movies = json.load(f)

    hints = get_type_hints(MovieEntry)
    seen_ids = set()

    for movie in movies:
        try:
            # Check required fields
            for field in MovieEntry.__required_keys__:
                if field not in movie:
                    warn(
                        f"Missing required field '{field}' in movie: {movie.get('Title', 'No title')}"
                    )

            # Type validation
            for field, typ in hints.items():
                if field in movie:
                    val = movie[field]
                    # Handle Optional (Union[..., NoneType])
                    if getattr(typ, "__origin__", None) is Union:
                        valid_types = [t for t in typ.__args__ if t is not type(None)]
                        if not any(isinstance(val, t) for t in valid_types):
                            warn(
                                f"Type mismatch in '{movie.get('Title', 'No title')}': Field '{field}' should be one of {valid_types}, got {type(val)}"
                            )
                    elif not isinstance(val, typ):
                        warn(
                            f"Type mismatch in '{movie.get('Title', 'No title')}': Field '{field}' should be {typ}, got {type(val)}"
                        )

            # Check for duplicate imdbID
            if "imdbID" in movie:
                if movie["imdbID"] in seen_ids:
                    warn(
                        f"Duplicate imdbID: {movie['imdbID']} in movie: {movie.get('Title', 'No title')}"
                    )
                seen_ids.add(movie["imdbID"])

        except Exception as e:
            warn(f"Error processing movie entry: {str(e)}")
            continue

    print(
        f"Validation complete for {len(movies)} movies. Check warnings for any issues."
    )


if __name__ == "__main__":
    validate(movies_json_path)
