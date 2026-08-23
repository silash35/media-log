import os

import requests


def load_env():
    with open(".env") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()


load_env()

API_KEY = os.environ["RAPID_API_KEY"]


def get_title_and_year(imdb_id: str) -> tuple[str, int]:
    response = requests.get(
        "https://imdb232.p.rapidapi.com/api/title/get-persisted-metadata",
        headers={
            "x-rapidapi-key": API_KEY,
            "x-rapidapi-host": "imdb232.p.rapidapi.com",
        },
        params={"tt": imdb_id},
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    title = data["data"]["titles"][0]["titleText"]["text"]
    year = data["data"]["titles"][0]["releaseYear"]["year"]

    return title, year
