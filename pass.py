import os
import random
import time

# Get password from user
pas = input("Send The Password: ")

# Valid characters
keys = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

# Initialize guess
pwg = ""

# Brute-force loop
while pwg != pas:
    pwg = ""
    for i in range(len(pas)):
        guess_char = keys[random.randint(0, len(keys) - 1)]
        pwg += guess_char  # Build guess in correct order

    # Output
    print("Trying:", pwg)
    print("Attacking... Please Wait!")
    time.sleep(0.2)  # Delay for realism

    # Clear screen (optional)
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

    # Check if password matched
    if pwg == pas:
        print("Password Found: " + pwg)
        break
    else:
        print("Password Not Found Yet!")

