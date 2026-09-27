from src.file_handler import save_patients


def add_patient(patients):
    print("\n--- ADD NEW PATIENT ---")
    p_id = input("Enter Patient ID (e.g. P101): ")
    if p_id in patients:
        print("Error: patient already exists!")
        return

    # asks for name
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))

    # asks for priority lvl
    print("Select Priority Level:")
    print("1. Critical")
    print("2. Urgent")
    print("3. Normal")
    prio_choice = input("Enter choice (1-3): ")

    if prio_choice == '1':
        prio_name = "Critical"
        prio_rank = 1
    elif prio_choice == "2":
        prio_name = 'Urgent'
        prio_rank = 2
    else:
        prio_name = "Normal"
        prio_rank = 3

    # creates id
    patients[p_id] = {
        "name": name,
        "age": age,
        "priority_name": prio_name,
        "priority_rank": prio_rank,
        "symptoms": [],
        "medicines": []
    }

    save_patients(patients)
    print("Patient added successfully!")


def show_patients(patients):
    if len(patients) == 0:
        print("No patient records found.")
        return

    print("\n================ PATIENT RECORDS ================")
    for p_id, info in patients.items():
        print(f"ID: {p_id} | Name: {info['name']} | Age: {info['age']} | Priority: {info['priority_name']}")

        if len(info["symptoms"]) > 0:
            print(f"   Symptoms: {', '.join(info['symptoms'])}")
        if len(info["medicines"]) > 0:
            print(f"   Medicines: {', '.join(info['medicines'])}")
        print("-------------------------------------------------")


def update_patient(patients):
    p_id = input("Enter Patient ID to update: ")
    if p_id not in patients:
        print("Patient ID not found!")
        return

    print(f"Updating record for {patients[p_id]['name']}:")
    new_name = input("Enter new name (press Enter to skip): ")

    if new_name != "":
        patients[p_id]["name"] = new_name
        save_patients(patients)
        print("record updated!")


def delete_patient(patients):
    p_id = input("Enter Patient ID to discharge/delete: ")

    if p_id in patients:
        patient_name = patients[p_id]['name']
        del patients[p_id]
        save_patients(patients)
        print(f"Patient {patient_name} discharged.")
    else:
        print("Patient ID not found!")