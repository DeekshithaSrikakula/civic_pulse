from utils.classifier import classify_complaint

def test_garbage():
    assert classify_complaint("చెత్త ఉంది") == "Garbage"

def test_water():
    assert classify_complaint("నీరు లీకేజ్") == "Water"
