def warn(message: str):
    print(f'Warning: "{message}"')


def order(data, keys_in_order):
    ordered = {}

    # Add fields in order
    for field in keys_in_order:
        if field in data:
            ordered[field] = data[field]

    return ordered
