def add_setting(settings, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()
    if key in settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )

    # Add the new setting
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    if not key in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key_value_pair):
    # FIX: Handle both string and tuple inputs
    if isinstance(key_value_pair, str):
        key = key_value_pair.lower()
    else:
        key = key_value_pair[0].lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"

    # Simplified the condition
    return "Setting not found!"


def view_settings(settings):
    if settings == dict():
        return "No settings available."

    # FIX: Build a formatted string instead of returning a tuple
    result = "Current User Settings:\n"
    for key, value in settings.items():
        # FIX: Capitalize the first letter of the setting name
        capitalized_key = key.capitalize()
        result += f"{capitalized_key}: {value}\n"

    # FIX: Already ends with newline from the loop
    return result


# Tests
test_settings = {"theme": "light"}

print(add_setting({"theme": "light"}, ("THEME", "dark")))
print(add_setting({"theme": "light"}, ("volume", "high")))
print(update_setting({"theme": "light"}, ("theme", "dark")))
print(update_setting({"theme": "light"}, ("volume", "high")))
print(delete_setting({"theme": "light"}, ("theme", "dark")))

# Test view_settings
print(view_settings({"theme": "dark", "volume": "high"}))
