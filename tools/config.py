from typing import Final, TypedDict, Union

movies_json_path: Final[str] = "database/movies.json"
movies_csv_path: Final[str] = "database/movies.csv"
shows_json_path: Final[str] = "database/shows.json"
shows_csv_path: Final[str] = "database/shows.csv"
games_json_path: Final[str] = "database/games.json"
games_csv_path: Final[str] = "database/games.csv"


class EntryBase(TypedDict):
    imdbID: str
    Title: str
    Year: int


class MovieEntry(EntryBase, total=False):
    Rating10: float
    Review: str
    FirstWatched: Union[int, str]
    LastWatched: Union[int, str]
    SafeForParents: bool
    SafeForKids: bool


class ShowEntry(EntryBase, total=False):
    Rating10: float
    Review: str
    SafeForParents: bool
    SafeForKids: bool


class GameEntry(EntryBase, total=False):
    Rating10: float
    Review: str
    SafeForParents: bool
    SafeForKids: bool
