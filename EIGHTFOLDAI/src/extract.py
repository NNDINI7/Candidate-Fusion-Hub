import os
from utils import read_csv, read_json


DATA_PATH = "data"


def extract_recruiter():
    """Extract data from recruiter.csv"""
    file_path = os.path.join(DATA_PATH, "recruiter.csv")

    try:
        df = read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print("Error reading recruiter.csv:", e)
        return []


def extract_ats():
    """Extract data from ats.json"""
    file_path = os.path.join(DATA_PATH, "ats.json")

    try:
        return read_json(file_path)
    except Exception as e:
        print("Error reading ats.json:", e)
        return {}


def extract_linkedin():
    """Extract data from linkedin.json"""
    file_path = os.path.join(DATA_PATH, "linkedin.json")

    try:
        return read_json(file_path)
    except Exception as e:
        print("Error reading linkedin.json:", e)
        return {}


def extract_github():
    """Extract data from github.json"""
    file_path = os.path.join(DATA_PATH, "github.json")

    try:
        return read_json(file_path)
    except Exception as e:
        print("Error reading github.json:", e)
        return {}


def extract_all():
    """
    Extract data from all available sources
    """

    return {
        "recruiter": extract_recruiter(),
        "ats": extract_ats(),
        "linkedin": extract_linkedin(),
        "github": extract_github()
    }