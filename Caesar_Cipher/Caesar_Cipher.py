# Hello, and welcome to my first ever Python project!
# I built a Caesar Cipher as the freecodecamp's first workshop exercise!
# First, I follow the instructions givem by the course, then I build a
# better version my self! Check the other Caesar Cipher file for the
# improved version please. Take care!


def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


encrypted_text = encrypt("freeCodeCamp", 3)
print(encrypted_text)
