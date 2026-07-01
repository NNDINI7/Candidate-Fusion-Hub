import json
import os
import sys

# Add src folder to Python path
sys.path.append("src")

from extract import extract_all
from merge import merge_data
from normalize import normalize_data
from validate import validate_data


def main():
    print("========== Candidate Data Transformer ==========\n")

    # Step 1: Extract Data
    extracted_data = extract_all()
    print("Data extracted successfully.")

    # Step 2: Merge Data
    merged_data = merge_data(extracted_data)
    print("Data merged successfully.")

    # Step 3: Normalize Data
    normalized_data = normalize_data(merged_data)
    print("Data normalized successfully.")
    print(normalized_data)

    # Step 4: Validate Data
    if validate_data(normalized_data):

        os.makedirs("output", exist_ok=True)

        with open("output/candidate_profile.json", "w") as file:
            json.dump(normalized_data, file, indent=4)

        print("\nCandidate profile saved to output/candidate_profile.json")

    else:
        print("\nValidation Failed!")


if __name__ == "__main__":
    main()