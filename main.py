# main.py

from utils.gmail import get_starred_email_subjects

if __name__ == "__main__":
    print("🔍 Fetching starred Gmail subjects...")

    subjects = get_starred_email_subjects()

    if not subjects:
        print("⚠️ No starred emails found.")
    else:
        print("⭐ Starred Email Subjects:")
        for i, subject in enumerate(subjects, start=1):
            print(f"{i}. {subject}")

from utils.edge_history import get_recent_edge_history

results = get_recent_edge_history()
for item in results:
    print(f"{item['visited']} - {item['title']} - {item['url']}")

from utils.browser_history import get_recent_browser_history

# history = get_recent_browser_history()
# for item in history:
#     print(f"{item['visited']} - {item['url']}")
results = get_recent_browser_history(limit=10)
for r in results:
    print(r["visited"], r["url"])


