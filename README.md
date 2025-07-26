# 🔐 Password Generator (Python)

A simple and secure Python script to generate strong, random passwords with customizable options including length, uppercase, lowercase, numbers, and special characters.

---

## 📌 Features

* Generate strong random passwords
* Choose password length
* Option to include:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Clean and easy-to-use CLI

---

## 🛠️ Technologies Used

* Python 3.x
* Built-in random and string libraries

---

## 📂 File Structure


📦 password-generator/
├── password_generator.py
└── README.md


---

## 📦 Installation

1. *Clone the repository:*

bash
git clone https://github.com/your-username/password-generator.git
cd password-generator


2. *Run the script:*

bash
python password_generator.py


---

## ▶️ Usage Example

Once you run the script, it will prompt you to enter:


Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

Generated password: G9@kf#TqZ1!d


---

## 🔒 Code Overview

Here's a preview of the logic used:

python
import random
import string

# Character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = string.punctuation

# User input & password generation logic


(Full code is in password_generator.py)

---

## ✅ Requirements

* Python 3.6 or later
* No external libraries required

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
