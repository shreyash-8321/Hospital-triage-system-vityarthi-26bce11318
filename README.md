# Smart Hospital Triage and Queue Management System

This is a simple Python CLI project made to manage hospital patients based on their priority. It also has a basic feature for checking symptoms and getting medicine suggestions.

## What This Project Does

The main idea of this project is to make sure patients with more serious conditions are handled first instead of just following first-come, first-served.

Each patient gets a priority number:

* 1 = Critical - needs help immediately
* 2 = Urgent - needs help soon
* 3 = Normal - can wait

There is also a symptom lookup option where you can enter symptoms and get basic medicine suggestions from a JSON file.

## Features

* Sorts patients according to their priority
* Add, view, update, and discharge patients
* Check symptoms and get medicine suggestions
* Shows patient details in a simple table
* Saves patient data in JSON files

## Technologies Used

* Python 3
* JSON
* `json` and `os` modules
* VS Code / PyCharm

## Files in This Project

* `hospital_system.py` - Main Python file with the menu and program logic
* `medicine_data.json` - Contains symptom and medicine information
* `patient_records.json` - Stores the patient records
* `statement.md` - Contains the problem statement and project scope
* `README.md` - Project information and instructions

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code or PyCharm.
3. Open the terminal.
4. Run:

```bash
python hospital_system.py
```

5. Select the options from the menu.

## How to Test It

1. Add a patient with ID `P101` and priority `1`.
2. Check the queue and see if `P101` is at the top.
3. Try the symptom lookup with something like `fever`.
4. Check the patient table and make sure the details are correct.
5. Discharge `P101` and check if the patient is removed from the records.

## Student Details

* Name: Shreyash Pandey
* Registration Number: 26BCE11318
