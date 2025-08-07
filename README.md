Password Brute Force Simulation
This Python script simulates a brute-force password guessing attack. It randomly generates guesses to match a user-provided password using lowercase letters and digits.

⚠️ Educational Use Only! This project is intended for learning and demonstration purposes only. Do not use it for unauthorized access or unethical purposes.

📁 Files
bruteforce.py – The main script that attempts to guess the input password by randomly generating combinations.

▶️ How to Run
Make sure you have Python installed (Python 3.x).

Clone this repo or download the script file.

Open a terminal or command prompt.

Run the script:

bash
Copy
Edit
Enter a simple password (e.g. abc or 123) when prompted.

💡 Features
Random password generation from lowercase letters and digits.

Console output for each attempt.

Clears the screen after each attempt for cleaner viewing.

Simulates a brute-force attack with a small time delay.

⚙️ Customization
You can adjust the following:

keys list: Add uppercase letters, symbols, etc.

time.sleep(): Increase or decrease the delay between attempts.

Remove os.system("clear") if running in environments where screen clearing is not needed.

❗ Disclaimer
This script is a basic simulation. It does not use efficient or realistic password-cracking methods (like dictionaries or hash reversal), and is very slow for long passwords.

Use it only in ethical scenarios, such as cybersecurity training environments or for learning how brute-force logic works.

