from typing import Final, Union, TypedDict

movies_json_path: Final[str] = "movies.json"
movies_csv_path: Final[str] = "movies.csv"


class MovieEntry(TypedDict):
    imdbID: str
    Title: str
    Year: int
    Rating10: float
    Review: str
    WatchedDate: Union[int, str]
    SafeForParents: bool
    SafeForKids: bool
