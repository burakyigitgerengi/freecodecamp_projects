import re
import json
import os

DB_FILE = "medical_records.json"

# ========================
# DATABASE
# ========================


def load_records():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: Corrupted database, starting fresh")
        return []


def save_records(records):
    with open(DB_FILE, "w") as f:
        json.dump(records, f, indent=4)
    print(f"Saved {len(records)} record(s)")


# ========================
# INPUT WITH VALIDATION
# ========================


def get_patient_input():
    """Get patient information from user with validation."""

    print("\n" + "-" * 50)
    print("ADD NEW PATIENT RECORD")
    print("-" * 50)

    # Patient ID
    while True:
        patient_id = input("\nEnter patient ID (e.g., P1234): ").strip()
        if re.fullmatch(r"p\d+", patient_id, re.IGNORECASE):
            patient_id = patient_id.upper()
            break
        print("Invalid format. Must be P followed by numbers.")

    # Age
    while True:
        age_str = input("Enter age (must be 18 or older): ").strip()
        if not age_str.isdigit():
            print("Age must be a number.")
            continue
        age = int(age_str)
        if age < 18:
            print("Age must be 18 or older.")
            continue
        break

    # Gender
    while True:
        gender = input("Enter gender (Male/Female/Other): ").strip()
        if gender.lower() in ("male", "female", "other"):
            gender = gender.capitalize()
            break
        print('Please enter "Male", "Female", or "Other".')

    # Diagnosis (optional)
    while True:
        diagnosis = input("Enter diagnosis (or press Enter to skip): ").strip()
        if diagnosis == "":
            diagnosis = None
            break
        if re.fullmatch(r"[A-Za-z ]+", diagnosis):
            diagnosis = diagnosis.title()
            break
        print("Diagnosis must contain only letters and spaces.")

    # Medications (optional, comma-separated)
    while True:
        medications = input(
            "Enter medications, comma-separated (or press Enter to skip): "
        ).strip()
        if medications == "":
            meds_list = []
            break
        meds = [m.strip() for m in medications.split(",") if m.strip()]
        if all(re.fullmatch(r"[A-Za-z ]+", m) for m in meds):
            meds_list = meds
            break
        print("Medications must contain only letters and spaces.")

    # Last visit ID
    while True:
        last_visit_id = input("Enter last visit ID (e.g., V5678): ").strip()
        if re.fullmatch(r"v\d+", last_visit_id, re.IGNORECASE):
            last_visit_id = last_visit_id.upper()
            break
        print("Invalid format. Must be V followed by numbers.")

    return {
        "patient_id": patient_id,
        "age": age,
        "gender": gender,
        "diagnosis": diagnosis,
        "medications": meds_list,
        "last_visit_id": last_visit_id,
    }


# ========================
# VIEW & SEARCH
# ========================


def view_all_records(records):

    if not records:
        print("\nNo records found")
        return

    print(f"\n{'-'*50}")
    print(f"ALL RECORDS ({len(records)} total)")
    print("-" * 50)

    for i, r in enumerate(records, 1):
        print(f"\n--- Record {i} ---")
        print(f"Patient ID:    {r['patient_id']}")
        print(f"Age:           {r['age']}")
        print(f"Gender:        {r['gender']}")
        print(f"Diagnosis:     {r['diagnosis'] or 'None'}")
        print(f"Medications:   {', '.join(r['medications']) or 'None'}")
        print(f"Last Visit ID: {r['last_visit_id']}")


def search_patient(records):

    if not records:
        print("\nNo records to search")
        return

    patient_id = input("\nEnter patient ID to search: ").strip().upper()
    found = [r for r in records if r["patient_id"] == patient_id]

    if found:
        r = found[0]
        print(f"\n{'-'*50}")
        print(f"FOUND PATIENT: {patient_id}")
        print("-" * 50)
        print(f"\nPatient ID:    {r['patient_id']}")
        print(f"Age:           {r['age']}")
        print(f"Gender:        {r['gender']}")
        print(f"Diagnosis:     {r['diagnosis'] or 'None'}")
        print(f"Medications:   {', '.join(r['medications']) or 'None'}")
        print(f"Last Visit ID: {r['last_visit_id']}")
    else:
        print(f"No patient found with ID: {patient_id}")


# ========================
# MAIN
# ========================


def main():
    records = load_records()

    while True:

        print("\n" + "-" * 50)
        print("MEDICAL RECORDS MANAGEMENT SYSTEM")
        print("-" * 50)
        print(f"Loaded {len(records)} record(s)")

        print(f"\n{'-'*50}")
        print("1. Add new patient record")
        print("2. View all records")
        print("3. Search for a patient")
        print("4. Exit")
        print("-" * 50)

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            new_record = get_patient_input()
            records.append(new_record)
            save_records(records)
            print(f"Patient {new_record['patient_id']} added!")

        elif choice == "2":
            view_all_records(records)

        elif choice == "3":
            search_patient(records)

        elif choice == "4":
            save_records(records)
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
