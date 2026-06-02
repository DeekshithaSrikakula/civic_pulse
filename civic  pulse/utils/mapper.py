import pandas as pd

def get_department(category):
    df = pd.read_csv("data/departments.csv")

    row = df[df["category"] == category]

    if not row.empty:
        return row.iloc[0]["department"]

    return "Department Not Found"