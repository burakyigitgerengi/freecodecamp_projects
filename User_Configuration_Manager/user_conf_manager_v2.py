import json
import os

DB_FILE = "settings.json"
DEFAULT_SETTINGS = {
    "username": "User",
    "theme": "dark",
    "language": "en",
    "notifications": True,
    "volume": 75,
    "auto_update": True,
}


def load_settings():
    """Load settings from file or create default."""
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE) as f:
                data = json.load(f)
                if data.keys() == DEFAULT_SETTINGS.keys():
                    return data
                print("ERROR: Corrupted settings file, resetting to defaults.")

        with open(DB_FILE, "w") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
        return DEFAULT_SETTINGS.copy()

    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: {e}. Using default settings.")
        return DEFAULT_SETTINGS.copy()


def save_settings(settings):
    """Save settings to file."""
    try:
        with open(DB_FILE, "w") as f:
            json.dump(settings, f, indent=4)
        return True
    except OSError as e:
        print(f"ERROR: Could not save settings: {e}")
        return False


def parse_value(value_str, expected_type):
    """Convert string input to the expected type."""
    if expected_type == bool:
        val = value_str.lower().strip()
        if val in ("true", "1", "yes", "on"):
            return True, True
        elif val in ("false", "0", "no", "off"):
            return False, True
        return None, False

    elif expected_type == int:
        try:
            return int(value_str), True
        except ValueError:
            return None, False

    return value_str, True


def main():
    settings = load_settings()

    print("=" * 40)
    print("User Configuration Manager")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("1. View settings")
        print("2. Update setting")
        print("3. Delete setting")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            print("\nCurrent Settings:")
            print("-" * 30)
            for key, value in settings.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

        elif choice == "2":
            key = input("Setting name: ").strip().lower()

            if key not in DEFAULT_SETTINGS:
                print(
                    f"ERROR: Invalid setting. Valid: {', '.join(DEFAULT_SETTINGS.keys())}"
                )
                continue

            value_str = input(f"New value: ").strip()
            value, valid = parse_value(value_str, type(DEFAULT_SETTINGS[key]))

            if not valid:
                type_name = type(DEFAULT_SETTINGS[key]).__name__
                print(f"ERROR: Invalid {type_name} value.")
                continue

            settings[key] = value
            if save_settings(settings):
                print(f"✓ Setting '{key}' updated to '{value}'")

        elif choice == "3":
            key = input("Setting to delete: ").strip().lower()

            if key not in settings:
                print(f"ERROR: Setting '{key}' does not exist.")
                continue

            del settings[key]
            if save_settings(settings):
                print(f"✓ Setting '{key}' deleted")

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("ERROR: Invalid choice. Enter 1-4.")


if __name__ == "__main__":
    main()
