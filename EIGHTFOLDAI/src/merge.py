def merge_data(extracted_data):
    """
    Merge candidate data from multiple sources.
    """

    merged = {}

    recruiter = extracted_data.get("recruiter", [])
    ats = extracted_data.get("ats", {})
    linkedin = extracted_data.get("linkedin", {})
    github = extracted_data.get("github", {})

    if isinstance(recruiter, list) and len(recruiter) > 0:
        recruiter = recruiter[0]

    sources = [recruiter, ats, linkedin, github]

    for source in sources:
        if not isinstance(source, dict):
            continue

        for key, value in source.items():
            if value in ["", None, []]:
                continue

            if key not in merged:
                merged[key] = value

            elif key.lower() == "skills":

                existing = merged[key]

                if isinstance(existing, str):
                    existing = [x.strip() for x in existing.split(",")]

                if isinstance(value, str):
                    value = [x.strip() for x in value.split(",")]

                merged[key] = list(set(existing + value))

    return merged