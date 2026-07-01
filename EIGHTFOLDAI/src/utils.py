import json
import pandas as pd


def read_csv(file_path):
    """Read CSV file."""
    return pd.read_csv(file_path)


def read_json(file_path):
    """Read JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


def write_json(data, file_path):
    """Write JSON output."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)