# 🔐 Password Manager

A simple yet powerful **Password Manager** built with Python and Tkinter.  
It lets you generate strong passwords, save them securely in a local JSON file, and quickly search for them later - all through an easy-to-use GUI.

---

## 🚀 Features

- 🎲 **Password Generator** - creates secure random passwords with letters, numbers, and symbols  
- 💾 **Save Credentials** - store website, email, and password combinations in a `data.json` file  
- 🔍 **Search Functionality** - find saved credentials instantly by website name  
- 📋 **One-click Copy** - automatically copies the generated password to your clipboard  
- ⚠️ **Smart Handling** - prevents overwriting data unless you confirm  

---

## 🧠 Technologies Used

- **Python 3**
- **Tkinter** for the GUI
- **JSON** for local data storage
- **Pyperclip** for clipboard copy

## 💡 How It Works

1. Enter a **website**, **email**, and **password**, or click _Generate Password_ to create one.  
2. Click **Add Password** to save your credentials in `data.json`.  
3. Use the **Search** button to retrieve existing entries.

## 🧰 Installation & Usage

1. Clone the repository:
   git clone https://github.com/<your-username>/password-manager.git
   cd password-manager
2. Install dependencies:
  pip install pyperclip
3. Run the app:
  python main.py
5. Passwords are stored locally — no internet connection required!
## 🛠️ Future Improvements
- 🔐 Encrypt stored passwords
- 🧭 Add export/import options
- ☁️ Optional cloud sync
- 🤖 Integrate simple AI-based password strength checker
