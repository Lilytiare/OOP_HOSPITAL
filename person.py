from abc import abstractmethod
from datetime import datetime
import Department


def assign_patient_to_department(General, Emergancy, Nurse, Patient):
    Nurse.give_urgency_lvl(Patient)
    if Patient.urgency_level >= 3:
        Emergancy.assign_department(Patient)
    else:
        General.assign_department(Patient)


class Person:
    def __init__(self, age=0, id=0, name=None, contact_info=None):
        self.age = age
        self.id = id
        self.name = name
        self.contact_info = contact_info

    @abstractmethod
    def view_info(self):
        pass

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID: {self.id}\nContact Info: {self.contact_info}"


class Patient(Person):
    def __init__(self, age=0, id=0, name=None, contact_info=None, urgency_level=0, health_insurance=False, medical_history=[], doctors_appointed=[], department=None, billing_status=False, registering_status=True):
        Person.__init__(self, age, id, name, contact_info)
        self.urgency_level = urgency_level
        self.health_insurance = health_insurance
        self.medical_history = medical_history
        self.doctors_appointed = doctors_appointed
        self.department = department
        self.billing_status = billing_status
        self.registering_status = registering_status

    def view_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nID: {self.id}\nContact Info: {self.contact_info}\nUrgency Level: {self.urgency_level}\nHealth Insurance: {self.health_insurance}\nMedical History: {self.medical_history}\nDoctors Appointed: {self.doctors_appointed}"

    def view_medical_history(self):
        output = f"{self.name}'s medical history: "
        for i in self.medical_history:
            output += i + ', '

        output = output[:-2]
        return output

    def view_appointment(self):
        output = f"{self.name} doctors appointed: "
        for i in self.doctors_appointed:
            output += i + ', '

        output = output[:-2]
        return output


class Staff(Person):
    def __init__(self, age, id, name, contact_info, shift: str):
        super().__init__(age, id, name, contact_info)
        self.shift = shift

    def view_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Contact Information: {self.contact_info}\n Shift: {self.shift}"


class Nurse(Staff):
    def __init__(self, age, id, name, contact_info, shift, department: str):
        super().__init__(age, id, name, contact_info, shift)
        self.department = department

    def view_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Contact Information: {self.contact_info}\n Shift: {self.shift}\n Department: {self.department}"

    def give_urgency_lvl(self, patient):
        patient.urgency_level = int(input("Input patients urgency level (1-5): "))

    def assign_doctor(self, patient, doctor):
        if len(doctor.list_of_patients) >= doctor.max_patients:
            return f"Dr. {doctor.name} is at full capacity!"
        else:
            doctor.list_of_patients.append(patient)
            patient.doctors_appointed.append(doctor.name)


class Doctor(Staff):
    def __init__(self, age, id, name, contact_info, shift, specialization: str, list_of_patients: list, max_patients):
        super().__init__(age, id, name, contact_info, shift)
        self.specialization = specialization
        self.list_of_patients = list_of_patients
        self.max_patients = max_patients

    def view_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Contact Information: {self.contact_info}\n Shift: {self.shift}\n Specialization: {self.specialization}"

    def treatment(self, patient, treatment, treatmentGD, treatmentEU):
        if patient.urgency_lvl >= 3:
            treatment = treatmentEU.call_emergency_treatment()
        else:
            treatment = treatmentGD.call_treatment()
        return f"{treatment} has been administered."

    def discharge(self, patient):
        patient.status = "Discharged"
        return f"{patient.name} has been discharged."

    def call_time_of_death(self):
        time_of_death = datetime.now()
        return f"Time of death {time_of_death}"


if __name__ == "__main__":
    GP = Department.GeneralPractice()
    ED = Department.EmergencyDepartment()
    person = Person()
    print(person)
    patient1 = Patient(12, 1, "Sett", "1234-5678")
    patient2 = Patient(12, 1, "Ann", "1234-5678")
    patient3 = Patient(12, 1, "Eve", "1234-5678")
    print(patient1.view_info())
    patient1.add_medical_history("GeneralPractice")
    print()
    print(f"{patient1.name} appointed {patient1.doctors_appointed[-1]}")
    print()
    print(patient1.view_info())
    print(patient1.view_medical_history())
    print(patient1.view_appointment())
    Dr1 = Doctor(44, 1, "Jones", "010-2000-0020", "night", "Doctor", [], 3)
    Dr2 = Doctor(44, 1, "Bones", "010-2000-0020", "night", "Doctor", [], 3)
    print(Dr1.view_info())
    N1 = Nurse(44, 1, "Susy", "010-0111-1111", "night", "General")
    print(N1.view_info())

    assign_patient_to_department(GP, ED, N1, patient1)
    print(GP.view_patients())
    print(ED.view_patients())
    assign_patient_to_department(GP, ED, N1, patient2)
    print(GP.view_patients())
    print(ED.view_patients())
    assign_patient_to_department(GP, ED, N1, patient3)
    print(GP.view_patients())
    print(ED.view_patients())

    print(patient1.doctors_appointed)

    N1.assign_doctor(patient1, Dr1)
    N1.assign_doctor(patient2, Dr2)
    print(patient1.doctors_appointed)
    print(Dr1.list_of_patients)
    print(patient2.doctors_appointed)
    print(Dr2.list_of_patients)

