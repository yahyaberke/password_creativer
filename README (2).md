# 🔐 PasswordCreator

A simple yet customizable command-line password generator built with Python. Users can define the length and character types to generate a strong, random password instantly.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

- Custom password length
- Choose character types:
  - Uppercase & lowercase letters
  - Digits
  - Special characters (`!`, `@`, `#`, etc.)
- Input validation (negative numbers, non-integer input, empty character pool)
- Instantly displays the generated password with its length

---

## 🚀 Getting Started

### Requirements

- Python 3.x

### Run

```bash
git clone https://github.com/yahyaberke/PasswordCreator.git
cd PasswordCreator
python password_creator.py
```

No external dependencies needed.

---

## 🖥️ How It Works

1. User enters the desired password length
2. User selects which character types to include
3. A random password is generated from the selected character pool
4. The password and its length are displayed

### Example Output

```
----------------------------------------
✅ Generated Strong Password:
   aB3!xQm@92Lk
   Length: 12
----------------------------------------
```

---

## 📁 Project Structure

```
PasswordCreator/
│
├── password_creator.py   # Main application file
└── README.md             # Project documentation
```

---

## 🔮 Possible Improvements

- Add option to exclude ambiguous characters (e.g. `0`, `O`, `l`, `1`)
- Generate multiple passwords at once
- Copy password to clipboard automatically
- Build a GUI with Tkinter

---

## 📄 License

This project is licensed under the MIT License.
