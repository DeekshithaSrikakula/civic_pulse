import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_NAME = "database/civic.db"
print("DATABASE PATH:", os.path.abspath(DB_NAME))

def create_table():

    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tracking_id TEXT,
        complaint TEXT,
        category TEXT,
        department TEXT,
        priority TEXT,
        status TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def generate_tracking_id():

    conn = sqlite3.connect(DB_NAME)

    count = conn.execute(
        "SELECT COUNT(*) FROM complaints"
    ).fetchone()[0]

    conn.close()

    return f"CP{count+1:04d}"



def insert_complaint(
    complaint,
    category,
    department,
    priority
):

    try:

        tracking_id = generate_tracking_id()

        conn = sqlite3.connect(DB_NAME)

        conn.execute(
            """
            INSERT INTO complaints
            (
                tracking_id,
                complaint,
                category,
                department,
                priority,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                tracking_id,
                complaint,
                category,
                department,
                priority,
                "Pending",
                datetime.now().strftime("%Y-%m-%d %H:%M")
            )
        )

        conn.commit()

        print("INSERT SUCCESSFUL")
        print("TRACKING ID:", tracking_id)

        conn.close()

        return tracking_id

    except Exception as e:

        print("DATABASE ERROR:", e)

        return None


def get_all_complaints():

    create_table()

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    return df
create_table()