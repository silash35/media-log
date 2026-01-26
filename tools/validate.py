from typing import Type, Union, get_type_hints

from config import (
    EntryBase,
    GameEntry,
    MovieEntry,
    ShowEntry,
    games_json_path,
    movies_json_path,
    shows_json_path,
)
from utils import read_json, warn


def validate(json_path: str, EntryType: Type[EntryBase]) -> None:
    entries = read_json(json_path)

    hints = get_type_hints(EntryType)
    seen_ids = set()

    for entry in entries:
        try:
            # Check required fields
            for field in EntryType.__required_keys__:
                if field not in entry:
                    warn(
                        f"Missing required field '{field}' in entry: {entry.get('Title', 'No title')}"
                    )

            # Type validation
            for field, typ in hints.items():
                if field in entry:
                    val = entry[field]
                    # Handle Optional (Union[..., NoneType])
                    if getattr(typ, "__origin__", None) is Union:
                        valid_types = [t for t in typ.__args__ if t is not type(None)]
                        if not any(isinstance(val, t) for t in valid_types):
                            warn(
                                f"Type mismatch in '{entry.get('Title', 'No title')}': Field '{field}' should be one of {valid_types}, got {type(val)}"
                            )
                    elif not isinstance(val, typ):
                        warn(
                            f"Type mismatch in '{entry.get('Title', 'No title')}': Field '{field}' should be {typ}, got {type(val)}"
                        )

            # Check for duplicate imdbID
            if "imdbID" in entry:
                if entry["imdbID"] in seen_ids:
                    warn(
                        f"Duplicate imdbID: {entry['imdbID']} in entry: {entry.get('Title', 'No title')}"
                    )
                seen_ids.add(entry["imdbID"])

        except Exception as e:
            warn(f"Error processing entry: {str(e)}")
            continue

    print(
        f"Validation complete for {len(entries)} entries. Check warnings for any issues."
    )


if __name__ == "__main__":
    print("Validating movies...")
    validate(movies_json_path, MovieEntry)
    print("Validating shows...")
    validate(shows_json_path, ShowEntry)
    print("Validating games...")
    validate(games_json_path, GameEntry)
