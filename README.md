# 🧠 File Finder Bot

A smart local assistant that searches across your system and online accounts — including Chrome/Edge bookmarks, Gmail starred emails, local Excel/CSV files, and browser history — and shows results through a fast, clean GUI.

> ✅ One keyword → 💡 One search → 🔗 Clickable links  
> Built with 🐍 Python + 🖼️ Tkinter + 🔗 Web integration

---

## 🔍 Features

- ✅ Unified keyword search
- 🔖 Chrome & Edge Bookmarks scanning
- 📬 Gmail Starred Emails (via Gmail API)
- 🧾 Recent Excel & CSV files (local file system)
- 🌐 Browser history (Chrome + Edge)
- 💬 Chat-like GUI app with clickable results
- 💡 Launchable via keyboard shortcut (`Ctrl + Alt + M` or `.bat`)
- 🌙 Lightweight — no background process

---

## 🖥️ How to Use

### 1️⃣ Clone or Download

<!-- ```bash
git clone https://github.com/YOUR_USERNAME/agentic-file-finder-bot.git
cd agentic-file-finder-bot -->

2️⃣ Set Up Python
Make sure you have Python 3.7+ installed.

Install dependencies:
pip install -r requirements.txt


3️⃣ Run the GUI App
bash
python gui_app.py

Or double-click the run_gui.bat file (recommended if you’ve configured a shortcut).

You’ll see a simple search box:

Type a keyword like: sql, project, or network

Hit Enter or click Search

You’ll see results grouped by category, each one clickable!

🧠 Sources It Searches
| Source                 | Description                        |
| ---------------------- | ---------------------------------- |
| ✅ Chrome Bookmarks     | All saved bookmarks                |
| ✅ Edge Bookmarks       | (via Edge profile if integrated)   |
| ✅ Gmail Starred Emails | Searches keyword in subject/sender |
| ✅ Local Excel/CSV      | From Desktop, Downloads, Documents |
| ✅ Browser History      | Recent pages visited (Edge/Chrome) |

🎯 Keyboard Shortcut (Windows Only)
You can launch the GUI via keyboard shortcut (e.g. Ctrl + Alt + M):

Create a .bat file like run_gui.bat with:
python gui_app.py
Create a shortcut to this .bat:

1.Right-click → Create shortcut

2.Right-click shortcut → Properties

3.Under Shortcut Key, set: Ctrl + Alt + M

4.Move shortcut to Desktop

5.(Optional) To suppress black window, use run_gui_silent.vbs


💡 Future Plans
🤖 Add deeper agentic behaviors (learning-based)

📂 Add Google Drive / Sheets / Docs scanning

🌐 Optional: Chat-style AI input

📦 PyInstaller packaging for EXE

🛡️ Disclaimer
This app only runs on your local machine. No data is sent or stored externally.

🧑‍💻 Made by
Deepak — Built with love, curiosity and reduce time and madde easy for searching files when working on tasks.

Special thanks to ChatGPT for code guidance.