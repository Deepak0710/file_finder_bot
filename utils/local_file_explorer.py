# utils/explorer.py
'''
import os
import glob
import datetime

# Define supported spreadsheet extensions
EXCEL_EXTENSIONS = ('.xlsx.lnk', '.xls.lnk', '.xlsm.lnk', '.csv.lnk')

def get_recent_excel_files(limit=20):
    recent_folder = os.path.expanduser(r'~\AppData\Roaming\Microsoft\Windows\Recent')
    recent_files = glob.glob(os.path.join(recent_folder, '*.lnk'))

    excel_files = []

    for file in recent_files:
        try:
            if file.lower().endswith(EXCEL_EXTENSIONS):
                file_name = os.path.basename(file).replace('.lnk', '')
                modified_time = os.path.getmtime(file)
                access_time = datetime.datetime.fromtimestamp(modified_time)
                excel_files.append({
                    'name': file_name,
                    'path': file,
                    'accessed': access_time
                })
        except Exception:
            pass  # Silently skip broken or inaccessible shortcuts

    excel_files.sort(key=lambda x: x['accessed'], reverse=True)
    return excel_files[:limit]

# For testing
if __name__ == "__main__":
    files = get_recent_excel_files()
    for f in files:
        print(f"📄 {f['name']} - Accessed: {f['accessed']} - Path: {f['path']}")
        '''
# utils/explorer.py

import os
import datetime

EXCEL_EXTENSIONS = ('.xlsx', '.xls', '.xlsm', '.csv')

# List of folders to scan
FOLDERS_TO_SCAN = [
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Documents"),
]

def get_recent_excel_files(limit=10):
    found_files = []

    for folder in FOLDERS_TO_SCAN:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(EXCEL_EXTENSIONS):
                    full_path = os.path.join(root, file)
                    try:
                        access_time = os.path.getatime(full_path)
                        found_files.append({
                            'name': file,
                            'path': full_path,
                            'accessed': datetime.datetime.fromtimestamp(access_time)
                        })
                    except Exception:
                        pass  # Skip unreadable files

    found_files.sort(key=lambda x: x['accessed'], reverse=True)
    return found_files[:limit]

# For testing
if __name__ == "__main__":
    files = get_recent_excel_files()
    for f in files:
        print(f"📄 {f['name']} - Accessed: {f['accessed']} - Path: {f['path']}")
