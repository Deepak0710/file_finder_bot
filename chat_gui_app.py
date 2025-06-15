import tkinter as tk
from tkinter import scrolledtext
from final import search_all  # Uses the `search_all` function from final.py


def format_results(results):
    response = ""
    for section, links in results.items():
        response += f"\n{section}:\n"
        if links:
            for i, link in enumerate(links, 1):
                response += f"  {i}. {link}\n"
        else:
            response += "  No results found.\n"
    return response.strip()


def on_send():
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"\nYou: {user_input}\n")
    entry.delete(0, tk.END)

    results = search_all(user_input)
    bot_response = format_results(results)

    chat_area.insert(tk.END, f"Bot:\n{bot_response}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)


# Initialize main window
root = tk.Tk()
root.title("Agentic File Finder Bot - Chat Mode")
root.geometry("700x500")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Segoe UI", 10))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=5)

entry = tk.Entry(frame, font=("Segoe UI", 10))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry.bind("<Return>", lambda event: on_send())

send_button = tk.Button(frame, text="Send", command=on_send)
send_button.pack(side=tk.RIGHT)

chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hello! Enter a keyword like 'sql' or 'network' and I'll find relevant links for you.\n")
chat_area.config(state=tk.DISABLED)

root.mainloop()
