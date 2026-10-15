# Patient class
class Patient:
    def __init__(self, name, patient_id, age, gender, diagnosis):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n======= Patient Information =======")
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")


# Vaccination class
class Vaccination:
    def __init__(self, center_name):
        self.center_name = center_name
        
        self.records = [] 
         # each record = [patient, vaccine_name, dose_number, date_vaccinated]

    def add_patient(self, patient):
        self.records.append([patient, None, None, None])
        print(f"Patient '{patient.name}' added successfully at {self.center_name}")

    def find_patient(self, patient_id):
        for record in self.records:
            if record[0].patient_id == patient_id:
                return record
        return None

    def vaccinate(self, patient_id, vaccine_name, dose_number, date_vaccinated):
        record = self.find_patient(patient_id)
        if record is None:
            print(f"No patient found with ID {patient_id}")
            return

        record1 = vaccine_name
        record2 = dose_number
        record3 = date_vaccinated
        print(f"{record[0].name} vaccinated with {vaccine_name} (Dose {dose_number}) on {date_vaccinated}")

    # UPDATE method (not a class) — keeps tracking people
    def update(self, patient_id, name=None, age=None, gender=None,
               diagnosis=None, vaccine_name=None, dose_number=None,
               date_vaccinated=None):
        record = self.find_patient(patient_id)
        if record is None:
            print(f"No patient found with ID {patient_id}")
            return

        patient = record[0]

        if name is not None:
            patient.name = name
        if age is not None:
            patient.age = age
        if gender is not None:
            patient.gender = gender
        if diagnosis is not None:
            patient.diagnosis = diagnosis
        if vaccine_name is not None:
            record[1] = vaccine_name
        if dose_number is not None:
            record[2] = dose_number
        if date_vaccinated is not None:
            record[3] = date_vaccinated

        print(f"Record for patient ID {patient_id} updated successfully.")

    def display_patients(self):
        print("\n======= All Patients =======")
        print(f"======= {self.center_name} =======")

        if len(self.records) == 0:
            print("No patient records found.")
        else:
            for record in self.records:
                patient = record[0]
                patient.display_info()
                if record[1] is None:
                    print("Vaccination: Not vaccinated yet")
                else:
                    print(f"Vaccine: {record[1]}")
                    print(f"Dose Number: {record[2]}")
                    print(f"Date Vaccinated: {record[3]}")


# Patient records
patient1 = Patient("Saidu", 101, 23, "male", "poverty")
patient2 = Patient("Abu Turay", 102, 30, "male", "malaria")
patient3 = Patient("Jane", 103, 20, "female", "headache")

# Vaccination center object
center1 = Vaccination("Mohamed Vaccination Center")

# Add all patients
center1.add_patient(patient1)
center1.add_patient(patient2)
center1.add_patient(patient3)

# Vaccinate patients
center1.vaccinate(101, "COVID-19", 1, "2024-01-15")


center1.vaccinate(102, "Malaria", 2, "2024-02-20")
center1.vaccinate(103, "COVID-19", 2, "2024-03-10")

# Show before update
center1.display_patients()

# UPDATE tracking info (not a class — just a method call)
center1.update(102, age=31, diagnosis="typhoid", dose_number=3, date_vaccinated="2024-05-01")

# Show after update
center1.display_patients()
