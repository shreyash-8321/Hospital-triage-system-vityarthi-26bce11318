from file_handler import load_patients
from patient_ops import add_patient, show_patients, update_patient, delete_patient
from triage import show_triage
from prescribe import give_medicine

def about_dev():
    print("\n=================================================")
    print("         ABOUT DEVELOPER & PROJECT INFO          ")
    print("=================================================")
    print(" Developer Name : Shreyash Pandey")
    print(" Reg Number     : 26BCE11318")
    print(" Course         : Btech CSE core")
    print(" Semester       : Semester 1")
    print(" Project Title  : Smart Hospital Triage System")
    print("=================================================")

def main():
    patients = load_patients()

    while True:
        print("\n=================================================")
        print("             HOSPITAL TRIAGE SYSTEM              ")
        print("=================================================")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. View Emergency Triage Queue")
        print("4. Auto-Prescribe Medicine by Symptoms")
        print("5. Update Patient Details")
        print("6. Discharge / Delete Patient Record")
        print("7. About Developer ")
        print("8. Exit Program")
        print("=================================================")

        choice = input("Enter option (1-8): ")

        #checks choice
        if choice == '1':
            add_patient(patients)
        elif choice == "2":
            show_patients(patients)
        elif choice == '3':
            show_triage(patients)
        elif choice == '4':
            give_medicine(patients)
        elif choice == "5":
            update_patient(patients)
        elif choice == '6':
            delete_patient(patients)
        elif choice == '7':
            about_dev()
        elif choice == "8":
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

main()