import re


def atoi(text: str):
    return int(text) if text.isdigit() else text


def natural_keys(val):
    return [atoi(c) for c in re.split(r'(\d+)', str(val))]


def naturally_sorted(elements: list):
    return sorted(elements, key=natural_keys)
