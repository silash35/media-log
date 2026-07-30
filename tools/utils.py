import csv
import json
from datetime import datetime
from zoneinfo import ZoneInfo

from config import EntryBase


def today():
    return datetime.now(ZoneInfo("America/Sao_Paulo")).date().isoformat()


def warn(message: str):
    print(f'Warning: "{message}"')


def order(data, keys_in_order):
    ordered = {}

    # Add fields in order
    for field in keys_in_order:
        if field in data:
            ordered[field] = data[field]

    return ordered


def read_json(json_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def write_json(json_path: str, data: list[EntryBase]):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_csv(csv_path: str, data: list[EntryBase], fieldnames: list[str]):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


from types import UnionType
from typing import Any, Union, get_args, get_origin


def check_type(value: Any, typ: Any) -> bool:
    origin = get_origin(typ)

    # int | str | None, etc.
    if origin is UnionType or origin is Union:
        return any(check_type(value, t) for t in get_args(typ))

    # list[T]
    if origin is list:
        if not isinstance(value, list):
            return False

        (item_type,) = get_args(typ)
        return all(check_type(item, item_type) for item in value)

    # dict[K, V] (opcional, se precisar)
    if origin is dict:
        if not isinstance(value, dict):
            return False

        key_type, value_type = get_args(typ)
        return all(
            check_type(k, key_type) and check_type(v, value_type)
            for k, v in value.items()
        )

    return isinstance(value, typ)
