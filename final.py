import os
import re
import utils.chrome_bookmarks as chrome
import utils.local_file_explorer as explorer
import utils.browser_history as browser_history

def filter_by_keyword(items, keyword):
    keyword_lower = keyword.lower()
    results = []
    for item in items:
        combined = " ".join([str(v) for v in item.values()]).lower()
        if keyword_lower in combined:
            results.append(item)
    return results

def save_results_to_html(bookmarks, history, files, keyword):
    html_content = f"""
    <html>
    <head>
        <title>Search Results for '{keyword}'</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            h2 {{ color: #2c3e50; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin: 8px 0; }}
            a {{ color: #2980b9; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <h1>Search Results for: <em>{keyword}</em></h1>
    """

    def format_section(title, items, key="url"):
        html = f"<h2>{title}</h2><ul>"
        if not items:
            html += "<li>No results found.</li>"
        else:
            for item in items:
                name = item.get("name", item.get("path", item.get("url", "")))
                link = item.get(key, item.get("path", ""))
                html += f"<li><a href='{link}' target='_blank'>{name}</a></li>"
        html += "</ul>"
        return html

    html_content += format_section("📘 Bookmarks", bookmarks, key="url")
    html_content += format_section("🌐 Browser History", history, key="url")
    html_content += format_section("📁 Local Files", files, key="path")

    html_content += "</body></html>"

    with open("results.html", "w", encoding="utf-8") as f:
        f.write(html_content)

# def search_all(keyword):
#     # Step 1: Chrome/Edge Bookmarks
#     try:
#         path = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\Bookmarks")
#         bookmark_links = chrome.get_chrome_bookmarks(path)
#         filtered_bookmarks = filter_by_keyword(bookmark_links, keyword)
#     except Exception as e:
#         print("Error fetching bookmarks:", e)
#         filtered_bookmarks = []

#     # Step 2: Browser history
#     try:
#         history_links = browser_history.get_recent_browser_history(limit=50)
#         filtered_history = filter_by_keyword(history_links, keyword)
#     except Exception as e:
#         print("Error fetching browser history:", e)
#         filtered_history = []

#     # Step 3: Local Excel/CSV Files
#     try:
#         recent_files = explorer.get_recent_excel_files(limit=20)
#         filtered_files = filter_by_keyword(recent_files, keyword)
#     except Exception as e:
#         print("Error fetching local files:", e)
#         filtered_files = []

#     return filtered_bookmarks, filtered_history, filtered_files
def search_all(keyword):
    from utils import chrome_bookmarks as chrome
    from utils import local_file_explorer as explorer
    from utils import browser_history as browser_history
    import os

    bookmark_path = os.path.expanduser(
        r"~\AppData\Local\Google\Chrome\User Data\Default\Bookmarks"
    )
    bookmark_data = chrome.get_chrome_bookmarks(bookmark_path)
    bookmark_links = [
        f"<a href='{b['url']}' target='_blank'>{b['name']}</a>" for b in bookmark_data
        if keyword.lower() in b["name"].lower() or keyword.lower() in b["url"].lower()
    ]

    try:
        history_data = browser_history.get_recent_browser_history()
        history_links = [
            f"<a href='{h['url']}' target='_blank'>{h['url']}</a>" for h in history_data
            if keyword.lower() in h["url"].lower()
        ]
    except Exception:
        history_links = []

    try:
        local_files = explorer.get_recent_excel_files()
        local_links = [
            f"<a href='file:///{f['path']}' target='_blank'>{f['name']}</a>" for f in local_files
            if keyword.lower() in f["name"].lower()
        ]
    except Exception:
        local_links = []

    return {
        "Bookmarks": bookmark_links,
        "Browser History": history_links,
        "Local Files": local_links,
    }



def main():
    keyword = input("🔍 Enter a keyword to search (e.g., 'network'): ").strip()

    bookmarks, history, files = search_all(keyword)

    # Output to HTML
    save_results_to_html(bookmarks, history, files, keyword)

    result_path = os.path.abspath("results.html")
    print(f"\n✅ Results saved to: file:///{result_path.replace(os.sep, '/')}\n")
    print("📂 Click or paste the above link in your browser to view results.")

if __name__ == "__main__":
    main()
