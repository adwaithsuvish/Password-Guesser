# 🔐 Common Password Generator

> A Python tool that generates likely password candidates from personal information — built to understand how weak, personal-info-based passwords get cracked.

---

## 📖 About

This program generates commonly used passwords by permuting personal information provided by the user (like name, dates, etc.). It writes the generated candidates to a text file, which can then be used to **check the strength of your own passwords** — if your real password shows up in the generated list, it's too easy to guess.

Built using **Python loops** and **file handling** — no external libraries required.

> ⚠️ **This program does not store any personal information.** All input is used locally to generate the file and nothing is saved, logged, or transmitted.

---

## ✨ Features

- 🔁 Generates password candidates via permutation of user-supplied info
- 📄 Outputs results to a plain text file for easy review
- 🧪 Can be used to sanity-check how "guessable" a password is
- 🐍 Pure Python — no dependencies to install

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/adwaithsuvish/Password-Guesser.git
cd Password-Guesser

# Run it
python main.py
```

You'll be prompted for personal details, and the tool will generate a text file with the resulting password candidates.

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🧩 Status

This project is **a work in progress**. Planned improvements:

- [ ] Add more permutation patterns / passcode variations
- [ ] Add command-line arguments instead of interactive prompts
- [ ] Add a strength-scoring feature to compare generated output against a real password

---

## 📌 Why I Built This

This started as a way to understand how tools like `cupp` (Common User Passwords Profiler) work — real attackers use exactly this kind of technique to build custom wordlists from a target's personal information. Building a small version myself helped me understand *why* using personal info in passwords is risky, not just that it is.

---

## 📄 License

No license specified yet.
