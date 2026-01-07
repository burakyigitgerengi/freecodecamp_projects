import json
import os

DB_FILE = "settings.json"
DEFAULT_SETTINGS = {"username": "", "theme": "dark", "language": "en"}


def get_user_config():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
        return DEFAULT_SETTINGS

    try:
        with open(DB_FILE, "r") as f:
            settings = json.load(f)
        if settings.keys() == DEFAULT_SETTINGS.keys():
            return settings
        else:
            print("CORRUPTED SETTINGS FILE, CREATING A NEW ONE.")
            with open(DB_FILE, "w") as f:
                json.dump(DEFAULT_SETTINGS, f, indent=4)
            return DEFAULT_SETTINGS

    except (OSError, json.JSONDecodeError):
        print("CORRUPTED SETTINGS FILE, CREATING A NEW ONE.")
        with open(DB_FILE, "w") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
        return DEFAULT_SETTINGS


settings = get_user_config()


def add_update_setting(key, value):
    if key in DEFAULT_SETTINGS:
        settings[key] = value
        with open(DB_FILE, "w") as f:
            json.dump(settings, f, indent=4)
        print(f"Setting '{key}' added/updated with value '{value}' successfully!")
        return True
    else:
        print(f"Invalid setting: {key}")
        return False


def delete_setting(key):
    if not isinstance(key, str):
        print("Invalid key type")
        return

    key = key.lower()

    if key in settings:
        settings.pop(key)
        with open(DB_FILE, "w") as f:
            json.dump(settings, f, indent=4)
        print(f"Setting '{key}' deleted successfully!")
    else:
        print(f"Setting '{key}' does not exist! Cannot delete a non-existing setting.")


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings.items():
        capitalized_key = key.capitalize()
        result += f"{capitalized_key}: {value}\n"
    return result


def main():
    print("User Configuration Manager")
    while True:
        print("\nOptions:")
        print("1. View settings")
        print("2. Add/Update setting")
        print("3. Delete setting")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(view_settings(settings))
        elif choice == "2":
            key = input("Enter setting name: ")
            value = input("Enter value: ")
            add_update_setting(key, value)
        elif choice == "3":
            key = input("Enter setting name to delete: ")
            delete_setting(key)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
