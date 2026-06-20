# 🗂️ FileVault — Python File Manager (CRUD App)

FileVault is a simple **file management system** built in Python, wrapped in a clean, modern **Streamlit UI**. It lets you **Create, Read, Update, and Delete** text files — entirely through an interactive web interface, with no command-line input needed.

This project started as a terminal-based CRUD script using Python's `pathlib` and `os` modules, and was later converted into a polished, presentable web app using Streamlit.

---

## ✨ Features

- **Create** — Make a new file and write initial content to it
- **Read** — View the contents and size of any existing file
- **Update** — Three ways to modify a file:
  - Rename it
  - Append new content to it
  - Overwrite its existing content
- **Delete** — Permanently remove a file (with a confirmation warning)
- **Live file list** in the sidebar showing all files currently in the workspace
- **Clean, color-coded UI** with success/error/info feedback for every action
- Built-in error handling for duplicate files, missing files, and invalid input

---

## 🛠️ Tech Stack

- **Python 3** — core logic
- **Streamlit** — web interface
- **pathlib** — object-oriented file path handling
- **os** — supporting OS-level file operations

---

## 📂 How It Works

All files created or managed through the app are stored inside a local folder called `FileVault_files/`, which is automatically created the first time you run the app. This keeps the project self-contained and prevents it from accidentally touching files elsewhere on your system.

| Operation | What happens |
|---|---|
| Create | Checks if the file already exists before creating it |
| Read | Checks if the file exists, then displays its contents |
| Update | Lets you rename, append to, or overwrite a file |
| Delete | Confirms the file exists, then removes it permanently |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/whyVitthal/Filevault---python-file-handling-project-using-streamlit-.git
cd "Filevault---python-file-handling-project-using-streamlit-"
```

### 2. Install dependencies
```bash
pip install streamlit
```

### 3. Run the app
```bash
streamlit run app.py
```

If you get a `'streamlit' is not recognized` error (common on Windows when Streamlit installs to a user directory not on PATH), use this instead:
```bash
python -m streamlit run app.py
```


## 🧠 What I Learned

- Practical use of Python's `pathlib` module for object-oriented file handling
- Structuring a CRUD application with proper error handling using `try`/`except`
- Converting a terminal-based script into an interactive, user-friendly web app
- Building and styling a UI with Streamlit, including custom CSS for a polished look
- Debugging real issues like typos in method calls and environment PATH problems

---

## 📌 Future Improvements

- Add support for multiple file types (not just `.txt`)
- Add a file upload/download option
- Add search and filter functionality for the file list
- Deploy the app live using Streamlit Community Cloud

---

## 🙋‍♂️ About

Built by Vitthal as a personal project to practice Python file handling and UI development with Streamlit.

If you found this useful, feel free to ⭐ the repo!
