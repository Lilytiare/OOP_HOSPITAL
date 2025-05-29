from Hospital.Person.Staff.Staff import *
from datetime import datetime

class Doctor(Staff):
    def __init__(self, age, id, name, contact_info, shift, department, specialization: str, list_of_patients: list, max_patients):
        super().__init__(age, id, name, contact_info, shift, department)
        self.specialization = specialization
        self.role = "doctor"
        self.list_of_patients = list_of_patients
        self.max_patients = max_patients
        self.d_p = 0

    def view_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Contact Information: {self.contact_info}\n Shift: {self.shift}\n Specialization: {self.specialization}\n Max Patients: {self.max_patients}"

    def treatment(self, patient, treatmentEU, treatmentGD):
        if self.department == patient.department:
            if patient.urgency_level >= 3:
                treatment = treatmentEU.give_treatment(patient)
                patient.medical_history.append(treatment)
            else:
                treatment = treatmentGD.give_treatment(patient)
                patient.medical_history.append(treatment)
            return f"{treatment} treatment has been administered for {patient.name}."
        else:
            return f"Dr.{self.name} cannot give treatment: not in the same Department."

    def discharge(self, patient):
        if self.department == patient.department:
            self.list_of_patients.remove(patient)
            patient.registering_status = False
            return f"{patient.name} has been discharged."
        else:
            return f"Dr.{self.name} cannot discharge {patient.name}: not in the same Department."

    def call_time_of_death(self, patient):
        time_of_death = datetime.now()
        patient.billing_status = False
        patient.registering_status = False
        patient.medical_history.append(f"Dead. {time_of_death}.")
        return f"Time of death {time_of_death}"

    def get_current_patients(self):
        output = f"Dr.{self.name}'s patients: "
        for p in self.list_of_patients:
            output += p.name + ", "

        output = output[:-2]
        return output