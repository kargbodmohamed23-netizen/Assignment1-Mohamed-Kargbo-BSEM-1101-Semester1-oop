Introduction
The Vaccination Tracker System is a Python application built using Object-Oriented Programming (OOP) principles. It addresses a genuine problem in the health sector: the difficulty of maintaining accurate, accessible, and up-to-date vaccination records in clinics and health centers, particularly in low-resource settings.

The system allows a health worker to register patients, record vaccinations (vaccine name, dose number, and date), update records, and view all stored information through a clean, console-based interface. It is designed to be modular, reusable, privacy-respecting, and freely available in accordance with Digital Public Goods (DPG) standards.

      Problem Statement
Many health centers in Sierra Leone and across the developing world still rely on paper-based systems to track patient vaccinations. This leads to several problems:

Records are easily lost, damaged, or duplicated.

It is difficult to determine which patients have received which doses.

Updating a patient's information requires manually editing paper files.

There is no easy way to retrieve a patient's record by ID.

Data cannot be shared or reused across health centers.

The Vaccination Tracker System solves these problems by providing a lightweight, digital alternative that requires no internet connection, no external libraries, and no expensive hardware.

              Features
Patient Registration – Add new patients with a unique ID, name, age, gender, and diagnosis.

Patient Lookup – Find any patient instantly by their unique ID.

Vaccination Recording – Log the vaccine name, dose number, and date of vaccination for each patient.

Record Updating – Modify patient details (name, age, gender, diagnosis) and vaccination details at any time.

Full Record Display – View all patients and their vaccination status in a single, readable output.

Vaccination Status Check – Clearly shows whether a patient has been vaccinated or not.
 OOP Concepts Applied
 Classes and Objects (Lecture 1)
Two classes were designed, each representing a real-world entity in the health domain.

Class	Purpose	Attributes	Methods
Patient	Represents an individual patient's health record	name, patient_id, age, gender, diagnosis	display_info()
Vaccination	Represents a vaccination center and manages all patient records	center_name, records (list)	add_patient(), find_patient(), vaccinate(), update(), display_patients()
Object creation and interaction:


 Instance Methods (Lecture 3)
Every method in the current implementation is an instance method because it operates on a specific object instance using self.

Patient.display_info() – prints the details of one patient.

Vaccination.add_patient() – adds a patient to a specific center's records.

Vaccination.find_patient() – searches a specific center's records by ID.

Vaccination.vaccinate() – records a vaccination at a specific center.

Vaccination.update() – updates a specific patient's record at a specific center.

Vaccination.display_patients() – displays all records belonging to a specific center.




The Vaccination class stores all patient records in a single list called self.records. Each element of this list is itself a list containing four items:

text
[patient_object, vaccine_name, dose_number, date_vaccinated]
Why a list was chosen:

It preserves insertion order, which is useful for displaying records in the order they were added.

It is simple to iterate over with a for loop.

It supports dynamic growth as new patients are registered.

It allows direct modification of individual records during updates.

Functions that operate on the list:


6. DPG Standards Alignment
DPG Principle	How the Vaccination Tracker Meets It
Open-source	The full source code is published on GitHub under the MIT License. Anyone may view, use, modify, and redistribute it free of charge.
Inclusive and accessible design	The program runs on any computer with Python 3 installed. It uses a simple text-based interface that requires no graphical capability, no internet connection, and no specialised hardware, making it usable in low-resource clinics.
Privacy-respecting	No sensitive personal data is stored. The system deliberately avoids national ID numbers, home addresses, phone numbers, and detailed medical histories. Only the minimum information needed for vaccination tracking is retained: a name, a locally assigned ID, age, gender, a brief diagnosis, and vaccination details.
Modular and reusable	The code is divided into two independent classes with clearly defined responsibilities. The Patient class can be reused in any health application, and the Vaccination class can be extended to support multiple centers, additional vaccines, or new domains such as livestock vaccination.
Transparent and auditable	The logic is straightforward and fully documented, allowing health authorities or developers to inspect and verify how records are handled.
Locally adaptable	Because there are no external dependencies, the system can be deployed offline in rural health posts where internet access is unreliable.
7. 
Project Structure

text
Description of the Project Files
1. main.py – Contains the main Python program, including the Patient and Vaccination classes, their methods, and the console menu used to register patients, record vaccinations, update records, search for patients, and display information.
2. README.md – Provides an overview of the project, its purpose, features, installation instructions, and steps for running the application.
3. LICENSE – Contains the MIT License, allowing others to use, modify, and distribute the source code under its terms.
4. .gitignore – Specifies files and folders that Git should ignore when tracking changes to the project.
Explanation
This structure keeps the project simple and lightweight. The main application code is stored in main.py, while the README and license provide documentation and open-source permissions. The .gitignore file helps prevent unnecessary files, such as Python cache files, from being uploaded to GitHub.
The project can be extended in the future by adding separate files for patient management, vaccination management, database storage, and automated testing as the system grows.




13. Conclusion
The Vaccination Tracker System demonstrates how Object-Oriented Programming can be applied to solve a genuine problem in the health sector. By modelling patients and vaccination centers as classes, storing records in a list, and providing methods for registration, vaccination, updating, and display, the system offers a practical, low-cost digital alternative to paper-based record keeping.

The solution aligns with Digital Public Goods standards by being open-source, accessible, privacy-respecting, and modular. It can be deployed immediately in any health center with a computer and Python installed, and it can be extended in future to support multiple centers, additional vaccine types, or other domains such as livestock health tracking.
