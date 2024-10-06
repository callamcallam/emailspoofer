# 📧 Email Spoofing Script

A simple Python script to **send spoofed emails** using the Brevo SMTP relay server. This is an educational tool designed to demonstrate how email spoofing works. **Use it responsibly!**

---

## ⚠️ Disclaimer
**This script is for educational purposes only.** It is illegal to spoof emails without proper authorization. Always make sure you are using this code within the bounds of the law.

---

## 🔧 Features
- Send emails from a **spoofed email address**.
- Customize **subject** and **message** content.
- Uses **Brevo SMTP** relay with authentication.
- Simple **command-line interface** for ease of use.

---

## 🚀 How It Works
This script uses the **`sendemail`** tool to interact with an SMTP server and send emails with a spoofed sender address. The process is automated via a Python script.

---

## 📜 Prerequisites

Before running the script, ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [sendemail](https://linux.die.net/man/1/sendemail) - A command-line email tool.
  
Install `sendemail` on Linux using the following command:
```bash
sudo apt-get install sendemail
