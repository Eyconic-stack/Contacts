# 📱 Contact Book

> A command-line contact manager that **never forgets**. Close it, reopen it, and every contact is still there.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-F7B731)
![Status](https://img.shields.io/badge/Status-Working-2EA44F)

---

## ✨ What it does

Most beginner programs forget everything the moment they close. This one saves your contacts to a file, so your data **survives restarts**.

| Feature | What happens |
|---|---|
| ➕ **Add** | Save a name, phone number and email |
| 📋 **Show all** | See every saved contact |
| 🔍 **Search** | Type part of a name (`tun` finds `Tunde`), upper or lower case |
| ✏️ **Edit** | Update a contact in place |
| 🗑️ **Delete** | Remove a contact for good |
| 💾 **Auto-save** | Every change is written to `contacts.json` immediately |

---

## 🎬 See it in action

```text
1. Add  2. Show all  3. Search  4. Delete  5. Quit  6. Edit
Choose: 1
Name: Ada
Phone: 08012345678
Email: ada@example.com
Saved!

Choose: 3
Search name: ad
Ada - 08012345678
```

---

## 🚀 Run it in 30 seconds

You need [Python 3](https://www.python.org/downloads/) installed. No extra packages.

```bash
git clone https://github.com/YOUR-USERNAME/contact-book.git
cd contact-book
python contacts.py
```

> 💡 On Windows, if `python` is not recognised, try `py contacts.py`.

---

## 🧠 How it works

- Contacts are a **list of dictionaries**, one dictionary per person: `{"name": ..., "phone": ..., "email": ...}`
- Saving and loading use Python's built-in `json` module
- If `contacts.json` does not exist yet (the first run), a `try / except FileNotFoundError` block starts with an empty list instead of crashing
- Each action (add, search, edit, delete) is its own **function**, so the code stays tidy and easy to change
- Edit works **in place**: it changes the existing contact instead of removing and re-adding it

---

## 🗂️ Project structure

```text
contact-book/
├── contacts.py      # the whole app
├── contacts.json    # created automatically on first save
└── README.md
```

---

## 📚 What I learned building this

- Lists and dictionaries, and how real apps store records
- Writing and reading files with `json`
- Handling errors with `try / except` so the program does not crash
- Breaking a program into small, reusable functions
- Changing data in place instead of rebuilding it

---

## 🔭 Ideas for next time

- [ ] Stop duplicate names from being added
- [ ] Sort contacts alphabetically
- [ ] Validate phone numbers and emails
- [ ] Rebuild it as a web app with a database

---

👤 **Godwin** · Lagos, Nigeria
🔗 [GitHub](https://github.com/Eyconic-stack) · [LinkedIn](https://linkedin.com/in/godwin-godfrey-289428355?utm_source=share_via&utm_content=profile&utm_medium=member_ios)
