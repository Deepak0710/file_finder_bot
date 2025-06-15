import os
import sqlite3
import datetime

def get_recent_edge_history(limit=10):
    history_path = os.path.expandvars(
        r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\History"
    )

    if not os.path.exists(history_path):
        print("Edge history file not found.")
        return []

    # Copy to avoid locking issues
    temp_path = "edge_history_copy"
    try:
        with open(history_path, 'rb') as src, open(temp_path, 'wb') as dst:
            dst.write(src.read())

        conn = sqlite3.connect(temp_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT url, title, last_visit_time
            FROM urls
            ORDER BY last_visit_time DESC
            LIMIT ?
        """, (limit,))

        results = []
        for url, title, visit_time in cursor.fetchall():
            # Convert Chrome time to human-readable
            visit_dt = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=visit_time)
            results.append({
                "title": title,
                "url": url,
                "visited": visit_dt.strftime("%Y-%m-%d %H:%M:%S")
            })

        conn.close()
        os.remove(temp_path)
        return results

    except Exception as e:
        print("Error reading Edge history:", e)
        return []
