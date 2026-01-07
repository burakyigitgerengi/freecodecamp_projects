# Welcome to the improved version of the Caesar_Cipher exercise in
# the freecodecamp course!

import os

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_text():
    while True:
        text = input("Please input your text: ")
        clear_terminal()
        # Create a version to check: remove spaces
        check_text = text.replace(" ", "")

        # Check if every character in the input is inside our ALPHABET string
        is_valid = all(char in ALPHABET for char in check_text)

        if is_valid and len(check_text) > 0:
            return text
        else:
            print(
                "Invalid input! Please use English letters only (a-z).\n"
                "Characters like 'ü' or '123' are not allowed."
            )


def get_shift():
    while True:
        shift_input = input("Please input the value of shift (1-25): ")
        clear_terminal()
        if shift_input.isdigit():
            shift = int(shift_input)
            if 1 <= shift <= 25:
                return shift
        print("Invalid shift! Please enter a whole number between 1 and 25.")


def caesar(text, shift, mode):

    while True:
        mode = input("Will you encrypt or decrypt? (E/D): ").lower()
        clear_terminal()

        if mode == "d":
            shift = -shift
            break

        elif mode == "e":
            break

        else:
            print('Please only type the letters "D" and "E": ')
    # Inform the user which operation will be performed and the effective shift
    mode_name = "decrypting" if shift < 0 else "encrypting"
    effective_shift = abs(shift)
    print(f"Now {mode_name} with a shift of {effective_shift} positions.")

    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    translation_table = str.maketrans(
        ALPHABET + ALPHABET.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    output = text.translate(translation_table)
    return output


# --- Execution ---
print("Caesar Cipher — a simple shift-based text encryptor/decryptor.")
print(
    "You will be asked for the text, a shift value (1-25), and whether to encrypt or decrypt."
)

user_text = get_text()
print(f"Text received: {user_text}")
user_shift = get_shift()
print(f"Shift value set to: {user_shift}")

output = caesar(user_text, user_shift, mode=True)
print(f"Final result: {output}")
