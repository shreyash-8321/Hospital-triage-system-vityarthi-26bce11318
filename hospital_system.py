import json
import os

pat_file = "patient_records.json"
med_file = "medicine_data.json"

# reads patients info
all_patients = {}
if os.path.exists(pat_file):
    try:
        f = open(pat_file, "r")
        all_patients = json.load(f)
        f.close()
    except:
        all_patients = {}

med_dict = {}
if os.path.exists(med_file):
    with open(med_file, "r") as f_med:
        med_dict = json.load(f_med)


while True:
    print("\n" + "=" * 36)
    print("    Smart Hospital Triage System    ")
    print("=" * 36)
    print("1. Add New Patient\n2. Show All Admitted\n3. View Priority list")
    print("4. Check Symptoms & Prescribe meds")
    print("5. Edit Patient info")
    print("6. Discharge Patient")
    print("7. Project & Student Details")
    print("8. Exit")
    print("-" * 36)

    ch = input("Enter choice (1-8): ").strip()

    if ch == "1":
        print("\n--- Register Patient ---")
        id_val = input("Enter ID: ").strip().upper()
        if id_val in all_patients:
            print("Notice: Patient ID already present!")
            continue

        p_name = input("Enter Name: ")
        raw_age = input("Enter Age: ").strip()
        p_age = int(raw_age) if raw_age.isdigit() else 18
        if not raw_age.isdigit():
            print("Invalid number, putting age as 18")

        print("Set priority: 1=Critical, 2=Urgent, 3=Normal")
        lvl = input("Priority: ").strip()

        urgency, rank_val = "Normal", 3
        if lvl == "1":
            urgency, rank_val = "Critical", 1
        elif lvl == "2":
            urgency, rank_val = "Urgent", 2

        all_patients[id_val] = {
            "name": p_name.strip(),
            "age": p_age,
            "urgency": urgency,
            "rank": rank_val,
            "symptoms": [],
            "prescription": [],
        }

        with open(pat_file, "w") as fp:
            json.dump(all_patients, fp, indent=4)

        print("Patient", p_name, "registered successfully.")

    elif ch == "2":
        if not all_patients:
            print("\nDatabase is currently empty.")
            continue

        print("\n" + "=" * 80)
        print(f"{'ID':<8} | {'Name':<20} | {'Age':<5} | {'Category':<10} | {'Symptoms':<25}")
        print("=" * 80)
        for pid, p in all_patients.items():
            category = p.get("urgency") or p.get("status") or "Normal"
            p_name = p.get("name", "Unknown")
            p_age = p.get("age", 0)
            symptoms = ", ".join(p.get("symptoms", []))
            if not symptoms:
                symptoms = "None recorded"
            print(f"{pid:<8} | {p_name:<20} | {p_age:<5} | {category:<10} | {symptoms:<25}")
        print("-" * 80)

    elif ch == "3":
        if not all_patients:
            print("\nQueue is empty.")
            continue

        queue = []
        for pid, p in all_patients.items():
            rank = p.get("rank") or p.get("priority_level") or 3
            category = p.get("urgency") or p.get("status") or "Normal"
            name = p.get("name", "Unknown")
            queue.append((rank, pid, name, category))
        queue.sort()

        print("\n" + "=" * 55)
        print(f"{'Pos':<5} | {'Category':<10} | {'Token':<8} | {'Patient Name':<20}")
        print("=" * 55)
        for count, item in enumerate(queue, start=1):
            print(f"#{count:<4} | {item[3]:<10} | {item[1]:<8} | {item[2]:<20}")
        print("=" * 55)

    elif ch == "4":
        p_id = input("\nEnter Patient ID: ").strip().upper()
        if p_id not in all_patients:
            print("No record found with that ID.")
            continue

        print("\nRecognized symptoms list:")
        for s in med_dict.keys():
            print(" - " + s)

        user_syms = input("\nType symptoms with commas: ").lower()
        clean_list = []
        med_suggestions = []

        for item in user_syms.split(","):
            curr = item.strip()
            if not curr:
                continue

            clean_list.append(curr)
            note = med_dict.get(curr, "Consult doctor for prescription")
            med_suggestions.append(f"{curr.title()}: {note}")

        all_patients[p_id]["symptoms"] = clean_list
        all_patients[p_id]["prescription"] = med_suggestions

        fp = open(pat_file, "w")
        json.dump(all_patients, fp, indent=4)
        fp.close()

        patient_name = all_patients[p_id].get("name", "Patient")
        print("\nPrescription saved for " + patient_name + ":")
        for line in med_suggestions:
            print(">>", line)

    elif ch == "5":
        edit_id = input("\nEnter ID to edit: ").strip().upper()
        if edit_id not in all_patients:
            print("ID not found.")
            continue

        print("Old Name:", all_patients[edit_id].get("name", ""))
        new_val = input("New Name: ").strip()
        if new_val:
            all_patients[edit_id]["name"] = new_val
            with open(pat_file, "w") as fp:
                json.dump(all_patients, fp, indent=4)
            print("Name updated.")

    elif ch == "6":
        del_id = input("\nEnter ID to discharge: ").strip().upper()
        if del_id not in all_patients:
            print("Invalid patient ID.")
            continue

        discharged_pat = all_patients.pop(del_id)
        fp = open(pat_file, "w")
        json.dump(all_patients, fp, indent=4)
        fp.close()
        print("Discharged:", discharged_pat.get("name", "Record"))

    elif ch == "7":
        print("\n" + "~" * 35)
        print("Name: Shreyash Pandey")
        print("Reg No: 26BCE11318")
        print("Project: Smart Hospital Triage System")
        print("Course: Python Essentials")
        print("~" * 35)

    elif ch == "8":
        print("\nExiting. Thank you!")
        break

    else:
        print("Invalid choice, enter a number from 1 to 8.")