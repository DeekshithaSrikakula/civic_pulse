def get_priority(text):

    text = text.lower()

    if "ప్రమాదం" in text:
        return "High"

    if "నీరు" in text:
        return "High"

    if "చెత్త" in text:
        return "Medium"

    return "Low"