from typing import Final, Required, Union, TypedDict

movies_json_path: Final[str] = "movies.json"
movies_csv_path: Final[str] = "movies.csv"


class MovieEntry(TypedDict, total=False):
    imdbID: Required[str]
    Title: Required[str]
    Year: Required[int]
    Rating10: float
    Review: str
    FirstWatched: Union[int, str]
    LastWatched: Union[int, str]
    SafeForParents: bool
    SafeForKids: bool
