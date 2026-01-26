from typing import Final, Required, TypedDict

movies_json_path: Final[str] = "database/movies.json"
movies_csv_path: Final[str] = "database/movies.csv"
shows_json_path: Final[str] = "database/shows.json"
shows_csv_path: Final[str] = "database/shows.csv"
games_json_path: Final[str] = "database/games.json"
games_csv_path: Final[str] = "database/games.csv"


class EntryBase(TypedDict, total=False):
    imdbID: Required[str]
    Title: Required[str]
    Year: Required[int]

    Rating10: float
    Review: str

    SafeForParents: bool
    ForKids: bool

    Tags: list  # [str]


class MovieEntry(EntryBase, total=False):
    Watches: list  # [Union[int, str]]


ShowEntry = EntryBase

GameEntry = EntryBase
