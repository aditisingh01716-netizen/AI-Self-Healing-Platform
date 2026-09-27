import sqlite3
from datetime import datetime

DATABASE_NAME = "reliability.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu REAL,
            memory REAL,
            disk REAL,
            risk_level TEXT,
            problem TEXT,
            action TEXT,
            recovery_status TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_incident(
    cpu,
    memory,
    disk,
    risk_level,
    problem,
    action,
    recovery_status
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO incidents
        (
            timestamp,
            cpu,
            memory,
            disk,
            risk_level,
            problem,
            action,
            recovery_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        cpu,
        memory,
        disk,
        risk_level,
        problem,
        action,
        recovery_status
    ))

    connection.commit()
    connection.close()


def get_incidents():

    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM incidents
        ORDER BY id DESC
    """)

    incidents = cursor.fetchall()

    connection.close()

    return incidents


if __name__ == "__main__":

    create_database()

    print("Database ready.")