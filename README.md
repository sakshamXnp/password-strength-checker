# 🔐 Password Strength Checker

**Password Strength Checker** is a Python-based security tool designed to analyze and evaluate the strength of user passwords using multiple criteria.  
It calculates entropy to measure randomness, estimates crack time based on brute-force attack speed, and checks for common weaknesses such as short length, lack of character diversity, predictable sequences, and repeated patterns.

The program provides real-time feedback with clear recommendations to help users create stronger and more secure passwords.  
This project combines **practical cybersecurity concepts** with **Python programming**, making it ideal for beginners learning about password security, entropy, and brute-force resistance.

It’s a simple yet educational tool that demonstrates how modern password evaluation works behind the scenes — perfect for students, ethical hackers, and anyone interested in **cybersecurity fundamentals**.

---

## 🧠 Features

✅ Checks password strength (Very Strong / Strong / Medium / Weak)  
✅ Calculates **entropy** to measure randomness  
✅ Estimates **crack time** based on brute-force speed  
✅ Detects:
- Common passwords  
- Sequential patterns (e.g., `1234`, `abcd`, `qwerty`)  
- Repeated characters  
✅ Provides **feedback & suggestions** for creating stronger passwords  

---

## 🧰 Technologies Used

- **Python 3**
- **Regular Expressions (`re`)**
- **Math library**
- **Command-line interface**

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sakshamXnp/password-strength-checker.git
   cd password-strength-checker

2. Run the script:

python password_checker.py


3. Enter a password when prompted and review:

Strength rating

Entropy score (in bits)

Estimated time to crack

Security improvement suggestions

4. 🧮 Example Output
Enter a password to check: MyP@ssw0rd123!

Password Strength: 💪 Strong
🔑 Entropy: 78.95 bits
⏱️ Estimated crack time: 142.52 years

Suggestions:
 - Avoid repeated characters (e.g., aaa, 111).

📊 How It Works

The script evaluates:

Character set variety (lowercase, uppercase, digits, symbols)

Password length

Common or predictable patterns

Entropy formula:

H = log2(pool_size ** password_length)


Crack time:
Based on 1 billion guesses per second (1e9).

🧩 Folder Structure
password-strength-checker/
│
├── password_checker.py     # Main script
├── README.md               # Project documentation
└── LICENSE                 # License file (MIT)

📚 Future Improvements

Add GUI interface using Tkinter or Streamlit

Integrate with password breach API (like HaveIBeenPwned)

Create a web-based version using Flask or Django

Add unit tests for validation

👨‍💻 Author

Saksham Niraula
Computer Science Student @ University of Wisconsin–Green Bay
Specializing in Cybersecurity 🔐
🌍 https://github.com/sakshamXnp
