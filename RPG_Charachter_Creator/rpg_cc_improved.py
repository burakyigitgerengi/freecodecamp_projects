import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def format_stat(value):
    return "●" * value + "○" * (10 - value)


def create_character():
    clear_screen()

    # Welcome message
    print("=" * 50)
    print("    WELCOME TO RPG CHARACTER CREATOR")
    print("=" * 50)
    print()

    # Name input loop
    print("CHARACTER NAME RULES:")
    print("  • Must be 1-10 letters long")
    print("  • Only alphabet letters allowed")
    print("  • No spaces or special characters")
    print()

    while True:
        name = input("Please type your character's name: ").strip()

        if len(name) == 0:
            print("❌ Your character name must have a name.\n")
        elif len(name) > 10:
            print("❌ Your character name can't be longer than 10 letters.\n")
        elif not name.isalpha():
            print(
                "❌ Your character name must only contain alphabet letters (no spaces).\n"
            )
        else:
            name = name.capitalize()
            break

    clear_screen()
    print(f"Great! Your character's name is: {name}\n")

    # Stats input loop
    print("STAT ASSIGNMENT RULES:")
    print("  • You have 7 points to distribute")
    print("  • Each stat must be between 1-4")
    print("  • Strength + Intelligence + Charisma = 7")
    print()
    print("Example: Strength=3, Intelligence=2, Charisma=2")
    print()

    while True:
        strength = input("Assign value to STRENGTH (1-4): ")
        intelligence = input("Assign value to INTELLIGENCE (1-4): ")
        charisma = input("Assign value to CHARISMA (1-4): ")

        try:
            strength, intelligence, charisma = map(
                int, [strength, intelligence, charisma]
            )
        except ValueError:
            print("\n❌ [Error] Please enter numbers only. Let's try again.\n")
            continue

        if strength < 1 or intelligence < 1 or charisma < 1:
            print("❌ All stats must be at least 1.\n")
        elif strength > 4 or intelligence > 4 or charisma > 4:
            print("❌ All stats must be no more than 4.\n")
        elif strength + intelligence + charisma != 7:
            total = strength + intelligence + charisma
            print(f"❌ Total is {total}, but must equal 7 points.\n")
        else:
            break

    # Display final character
    clear_screen()
    print("=" * 50)
    print("    CHARACTER CREATED SUCCESSFULLY!")
    print("=" * 50)
    print()
    print(f"Name: {name}")
    print("-" * 50)
    print(f"Strength:     {format_stat(strength)} ({strength}/10)")
    print(f"Intelligence: {format_stat(intelligence)} ({intelligence}/10)")
    print(f"Charisma:     {format_stat(charisma)} ({charisma}/10)")
    print("=" * 50)

    return f"\n✓ {name} is ready for adventure!"


print(create_character())
