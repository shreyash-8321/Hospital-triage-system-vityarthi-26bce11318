# Problem Statement & Scope: Smart Hospital Triage System

## 1. Problem Statement

Hospitals can get very busy, causing delays in patient registration and treatment. Usually, patients are handled based on arrival time, which may delay treatment for patients with serious conditions.

This project helps prioritize patients based on the severity of their condition and also provides basic symptom and medicine information.

## 2. Project Scope

The **Smart Hospital Triage System** is an offline, terminal-based system for managing hospital patients.

It can:

* Register patients
* Assign priority based on condition
* Arrange the patient queue by priority
* Look up basic symptom and medicine information
* Store records using JSON files

## 3. Target Users

* **Triage Staff / Receptionists:** Add and manage patient details.
* **Doctors / Medical Staff:** View patients based on priority.
* **Hospital Staff:** Check basic symptom and medicine information.

## 4. Main Features

* **Priority Queue:** Critical (Rank 1), Urgent (Rank 2), Normal (Rank 3)
* **Symptom Lookup:** Matches symptoms with 80+ stored conditions.
* **Patient Management:** Add, view, update, and discharge patients.
* **JSON Storage:** Uses `patient_records.json` and `medicine_data.json` for local storage.
