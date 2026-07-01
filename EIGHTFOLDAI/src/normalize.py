import phonenumbers


def normalize_email(email):
    """Convert email to lowercase."""
    if email:
        return email.strip().lower()
    return ""


def normalize_phone(phone):
    """Convert phone number to international format."""
    try:
        phone = str(phone)
        parsed = phonenumbers.parse(phone, "IN")
        return phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.E164
        )
    except:
        return phone


def normalize_skills(skills):
    """Remove duplicate skills and standardize names."""
    if isinstance(skills, str):
        skills = [s.strip().title() for s in skills.split(",")]

    elif isinstance(skills, list):
        skills = [s.strip().title() for s in skills]

    return list(set(skills))


def normalize_experience(exp):
    """Normalize experience format."""
    if exp:
        exp = str(exp).replace("+", "").strip()
    return exp


def normalize_data(candidate):
    """Normalize complete candidate profile."""

    if "Email" in candidate:
        candidate["Email"] = normalize_email(candidate["Email"])

    if "Phone" in candidate:
        candidate["Phone"] = normalize_phone(candidate["Phone"])

    if "Skills" in candidate:
        candidate["Skills"] = normalize_skills(candidate["Skills"])

    if "Experience" in candidate:
        candidate["Experience"] = normalize_experience(candidate["Experience"])

    return candidate