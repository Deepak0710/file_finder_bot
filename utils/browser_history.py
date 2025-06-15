from browser_history import get_history
import datetime

def get_recent_browser_history(limit=20):
    try:
        outputs = get_history()
        history = outputs.histories  # This is a list of tuples

        # Print sample to debug (optional)
        # print(history[:5])  # ← You can uncomment this to see what it returns

        # Each item in `history` is a tuple like: (datetime, url)
        formatted = []
        for entry in history:
            if len(entry) >= 2:
                dt, url = entry[0], entry[1]
                formatted.append({
                    "visited": dt.strftime("%Y-%m-%d %H:%M:%S"),
                    "url": url,
                    "title": None  # Not available
                })

        # Sort by most recent and return top N
        recent = sorted(formatted, key=lambda x: x["visited"], reverse=True)[:limit]
        return recent

    except Exception as e:
        print("Error fetching browser history:", e)
        return []
