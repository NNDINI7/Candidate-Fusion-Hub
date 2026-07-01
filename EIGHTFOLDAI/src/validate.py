def validate_data(candidate):

    # Accept Name or Full_Name
    name = candidate.get("Name") or candidate.get("Full_Name")

    if not name:
        print("Validation Failed!")
        print("Missing Field: Name")
        return False

    if not candidate.get("Email"):
        print("Validation Failed!")
        print("Missing Field: Email")
        return False

    if not candidate.get("Phone"):
        print("Validation Failed!")
        print("Missing Field: Phone")
        return False

    if not candidate.get("Skills"):
        print("Validation Failed!")
        print("Missing Field: Skills")
        return False

    print("Validation Successful!")
    return True