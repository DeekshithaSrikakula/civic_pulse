
def classify_complaint(text):

    text = text.lower().strip()

    if any(word in text for word in [
        "చెత్త",
        "garbage",
        "waste"
    ]):
        return "Garbage"

    elif any(word in text for word in [
        "నీరు",
        "water",
        "leakage"
    ]):
        return "Water"

    elif any(word in text for word in [
        "డ్రైనేజ్",
        "కాలువ",
        "sewage"
    ]):
        return "Drainage"

    elif any(word in text for word in [
        "రోడ్",
        "రోడ్డు",
        "గుంత",
        "pothole"
    ]):
        return "Road"

    elif any(word in text for word in [
        "లైట్",
        "వీధి లైట్",
        "street light"
    ]):
        return "Street Light"

    return "Other"