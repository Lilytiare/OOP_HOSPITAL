from Hospital.Person.Staff.Staff import *
from datetime import datetime

class Doctor(Staff):
    def __init__(self, age, id, name, contact_info, shift, department, specialization: str, list_of_patients: list, max_patients):
        super().__init__(age, id, name, contact_info, shift, department)
        self.specialization = specialization
        self.role = "doctor"
        self.list_of_patients = list_of_patients
        self.max_patients = max_patients

    def view_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Contact Information: {self.contact_info}\n Shift: {self.shift}\n Specialization: {self.specialization}\n Max Patients: {self.max_patients}"

    def treat(self, patient, treatment):
        treatment = treatment.give_treatment()
        patient.medical_history.append(treatment)
        return treatment,f"{treatment} treatment has been administered for {patient.name}."

    def discharge(self, patient):
        self.list_of_patients.remove(patient.name)
        patient.registering_status = False
        return self.list_of_patients, f"{patient.name} has been discharged."

    def call_time_of_death(self, patient):
        time_of_death = datetime.now()
        patient.billing_status = False
        patient.registering_status = False
        patient.medical_history.append(f"Dead. {time_of_death}.")
        return f"Time of death {time_of_death}"

    def get_current_patients(self):
        output = f"Dr.{self.name}'s patients: \n\n"
        for p in self.list_of_patients:
            output += p + "\n"
        return output