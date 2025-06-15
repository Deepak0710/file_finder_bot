import tkinter as tk
from tkinter import ttk
import webbrowser
from final import search_all  # Ensure final.py has a search_all(keyword) function

def open_link(url):
    webbrowser.open(url)

def on_search():
    # Clear previous results
    for widget in result_frame.winfo_children():
        widget.destroy()

    keyword = entry.get().strip()
    if not keyword:
        return

    results = search_all(keyword)

    has_results = False

    for section, links in results.items():
        # Section title
        ttk.Label(result_frame, text=f"{section}", font=("Arial", 10, "bold")).pack(anchor="w", pady=(5, 0))

        if links:
            has_results = True
            for link_html in links:
                # Extract URL and text from HTML <a href='...'>text</a>
                try:
                    start = link_html.index("href='") + 6
                    end = link_html.index("'", start)
                    url = link_html[start:end]
                    text_start = link_html.index(">", end) + 1
                    text_end = link_html.index("</a>", text_start)
                    link_text = link_html[text_start:text_end]
                except Exception:
                    url = link_html
                    link_text = link_html

                link_label = tk.Label(result_frame, text=link_text, fg="blue", cursor="hand2")
                link_label.pack(anchor="w")
                link_label.bind("<Button-1>", lambda e, u=url: open_link(u))
        else:
            tk.Label(result_frame, text="No files found.", fg="gray").pack(anchor="w")

    if not has_results:
        tk.Label(result_frame, text="🔍 No matching results found.", fg="red").pack(anchor="center")

    # Expand the window vertically based on content
    root.geometry("700x500")

# UI Setup
root = tk.Tk()
root.title("File Navigator")
root.geometry("480x100+1200+50")  # Compact size, top-right corner
root.attributes('-topmost', True)  # Always on top

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.X)

entry = ttk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))
entry.focus()
entry.bind("<Return>", lambda event: on_search())


ttk.Button(frame, text="Search", command=on_search).pack(side=tk.LEFT)

# Scrollable result section
result_frame = ttk.Frame(root, padding=10)
result_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
