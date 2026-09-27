from file_handler import load_meds, save_patients


def give_medicine(patients):
    p_id = input("Enter Patient ID: ")

    if p_id not in patients:
        print("Patient ID not found!")
        return

    med_db = load_meds()

    # Check what symptoms the patient already has in their record
    symptom_list = patients[p_id]["symptoms"]

    # If they already have symptoms, give the option to keep them
    if len(symptom_list) > 0:
        print("Patient already has these symptoms recorded:")
        for s in symptom_list:
            print(" - " + s)

        change_choice = input("Press Enter to keep these, or type 'new' to enter different symptoms: ")

        if change_choice == "new":
            symptom_list = []  # clear the list so the program asks for new ones

    # If the list is empty (either they had none, or they typed 'new')
    if len(symptom_list) == 0:
        print("--- Available Symptoms in Database ---")
        for key in med_db:
            print(key)

        user_input = input("Enter patient symptoms separated by commas: ")

        raw_list = user_input.split(",")
        for s in raw_list:
            clean_s = s.strip().lower()
            if clean_s != "":
                symptom_list.append(clean_s)

    suggested_meds = []

    # Generate the prescription based on the final symptom list
    for symptom in symptom_list:
        if symptom in med_db:
            msg = symptom + ": " + med_db[symptom]
            suggested_meds.append(msg)
        else:
            suggested_meds.append(symptom + ": Consult doctor")

    # Update the dictionary and save
    patients[p_id]["symptoms"] = symptom_list
    patients[p_id]['medicines'] = suggested_meds

    save_patients(patients)

    print("\n--- PRESCRIPTION FOR " + patients[p_id]['name'] + " ---")
    for m in suggested_meds:
        print(" - " + m)