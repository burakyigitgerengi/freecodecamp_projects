def create_character(name, strength, intelligence, charisma):
    # Validate character name
    if not isinstance(name, str):
        return "The character name should be a string."

    if len(name) == 0:
        return "The character should have a name."

    if len(name) > 10:
        return "The character name is too long."

    if " " in name:
        return "The character name should not contain spaces."

    # Validate stats are integers
    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return "All stats should be integers."

    # Validate stat ranges
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        return "All stats should be no less than 1."

    if any(stat > 4 for stat in [strength, intelligence, charisma]):
        return "All stats should be no more than 4."

    # Validate sum of stats
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points."

    # Create character sheet
    def format_stat(value):
        return "●" * value + "○" * (10 - value)

    result = f"{name}\n"
    result += f"STR {format_stat(strength)}\n"
    result += f"INT {format_stat(intelligence)}\n"
    result += f"CHA {format_stat(charisma)}"

    return result


# Test cases
print(create_character("ren", 4, 2, 1))
print(create_character("", 4, 2, 1))
print(create_character("verylongname", 4, 2, 1))
print(create_character("has space", 4, 2, 1))
print(create_character("test", 4, 2, 2))
