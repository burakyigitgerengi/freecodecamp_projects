def pin_extractor(poems):
    # Validation checks
    if not isinstance(poems, list):
        print("You must enter a list.")
        return []

    if not poems:
        print("You must enter a valid text.")
        return []

    # Check if all items in the list are strings
    for poem in poems:
        if not isinstance(poem, str):
            print("You must enter the poems as string values.")
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
    poems = []
    number_of_poems = input(
        "Please input the number of poems you are willing to import: "
    )
    number_of_poems = int(number_of_poems)
    for _ in range(number_of_poems):
        print(
            "Please import your poem (use '/' to separate lines): \n(e.g. My Love Deniz/Your are the love of my life/the one and only star/I can look up in the sky/That's how I find my way/Stargazing with tear in my eyes)"
        )
        a = input()
        a = a.replace(" / ", "\n")  # Only replace " / " not every space
        poems.append(a)
    return poems


poems_got = get_poems()
print(pin_extractor(poems_got))
