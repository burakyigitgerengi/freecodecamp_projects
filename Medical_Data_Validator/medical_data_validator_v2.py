import re

medical_records = []


def get_patient_input():
    while True:
        # Patient ID
        while True:
            patient_id = input("Enter patient ID (e.g., P1234): ").strip()
            if re.fullmatch(r"p\d+", patient_id, re.IGNORECASE):
                patient_id = patient_id.upper()
                break
            print("Invalid patient ID format. Please try again.")

        # Age
        while True:
            age_str = input("Enter age (must be 18 or older): ").strip()
            if not age_str.isdigit():
                print("Age must be a number. Please try again.")
                continue
            age = int(age_str)
            if age < 18:
                print("Age must be 18 or older. Please try again.")
                continue
            break

        # Gender
        while True:
            gender = input("Enter gender (Male/Female/Other): ").strip()
            if gender.lower() in ("male", "female", "other"):
                gender = gender.capitalize()
                break
            print('Invalid gender. Please enter "Male", "Female", or "Other".')

        # Diagnosis (optional)
        while True:
            diagnosis = input("Enter diagnosis (or leave blank if none): ").strip()
            if diagnosis == "":
                break
            if re.fullmatch(r"[A-Za-z ]+", diagnosis):
                diagnosis = diagnosis.title()
                break
            print("Diagnosis must contain only letters and spaces. Please try again.")

        # Medications (optional, comma-separated)
        while True:
            medications = input(
                "Enter medications (comma-separated, or leave blank if none): "
            ).strip()
            if medications == "":
                meds_list = []
                break
            meds = [m.strip() for m in medications.split(",") if m.strip()]
            if all(re.fullmatch(r"[A-Za-z ]+", m) for m in meds):
                meds_list = meds
                break
            print("Medications must contain only letters and spaces. Please try again.")

        # Last visit ID
        while True:
            last_visit_id = input("Enter last visit ID (e.g., V5678): ").strip()
            if re.fullmatch(r"v\d+", last_visit_id, re.IGNORECASE):
                last_visit_id = last_visit_id.upper()
                break
            print("Invalid last visit ID format. Please try again.")

        medical_records.append(
            {
                "patient_id": patient_id,
                "age": age,
                "gender": gender,
                "diagnosis": diagnosis,
                "medications": meds_list,
                "last_visit_id": last_visit_id,
            }
        )

        another = input("Add another record? (y/n): ").strip().lower()
        if another not in ("y", "yes"):
            return medical_records

    # example medical record
    # {
    #     "patient_id": "P1001",
    #     "age": 34,
    #     "gender": "Female",
    #     "diagnosis": "Hypertension",
    #     "medications": ["Lisinopril"],
    #     "last_visit_id": "V2301",
    # }


if __name__ == "__main__":
    records = get_patient_input()
    print(records)
