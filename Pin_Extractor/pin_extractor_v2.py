def pin_extractor(poems):
    b = []
    b.append(poems)
    # Validation checks
    if not isinstance(poems, list):
        print("Error: You must enter a list.")
        return []

    if len(poems) == 0:
        print("Error: The list is empty. Please provide at least one poem.")
        return []

    # Check if all items in the list are strings
    for i, poem in enumerate(poems):
        if not isinstance(poem, str):
            print(
                f"Error: Poem at index {i} is not a string. You must enter the poems as string values."
            )
            return []
        if poem.strip() == "":
            print(f"Error: Poem at index {i} is empty.")
            return []

    # Main logic
    secret_codes = []
    for poem in poems:
        secret_code = ""
        lines = poem.split("/")
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"
        secret_codes.append(secret_code)

    return secret_codes  # Return the list, not just one code


def get_poems():

    print("=" * 60)
    print("WELCOME TO THE PIN EXTRACTOR")
    print("=" * 60)
    print("\nThis tool extracts secret PIN codes from poems!")
    print("Each line gives one digit based on word lengths.\n")

    poems = []

    # Keep asking until we get a valid number
    while True:
        number_of_poems = input(
            "Please input the number of poems you are willing to import: "
        )
        try:
            number_of_poems = int(number_of_poems)
            if number_of_poems <= 0:
                print("Please enter a positive number.")
                continue
            break  # Valid input, exit the loop
        except ValueError:
            print("You must input a number.")
            # Loop continues, asking again

    for _ in range(number_of_poems):
        print(
            "\nPlease import your poem (use '/' to separate lines): \n(e.g. My Love Deniz/Your are the love of my life/the one and only star/I can look up in the sky/That's how I find my way/Stargazing with tear in my eyes)"
        )
        while True:
            a = input()
            # Allow letters, spaces, slashes, and common punctuation
            allowed_special = " '/-"
            if all(char.isalpha() or char in allowed_special for char in a):
                poems.append(a)
                break  # Exit the inner loop after valid input
            else:
                print(
                    "You must only enter text, spaces, slashes, and basic punctuation."
                )
    return poems


poems_got = get_poems()
print(pin_extractor(poems_got))
