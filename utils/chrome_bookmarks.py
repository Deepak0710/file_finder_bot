# utils/chrome.py
import os
import json
from typing import List, Dict

def get_chrome_bookmarks(bookmark_path: str) -> List[Dict[str, str]]:
    if not os.path.exists(bookmark_path):
        raise FileNotFoundError(f"Bookmark file not found: {bookmark_path}")

    with open(bookmark_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    urls = []

    def extract_urls(node):
        if isinstance(node, dict):
            if node.get("type") == "url":
                urls.append({"name": node.get("name"), "url": node.get("url")})
            for child in node.values():
                extract_urls(child)
        elif isinstance(node, list):
            for item in node:
                extract_urls(item)

    extract_urls(data)
    return urls

if __name__ == "__main__":
    path = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\Bookmarks")
    bookmarks = get_chrome_bookmarks(path)
    for b in bookmarks:
        print(f"{b['name']} -> {b['url']}")
