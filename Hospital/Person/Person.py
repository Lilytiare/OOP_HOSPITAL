from abc import abstractmethod

def assign_patient_to_department(General, Emergency, nurse, patient):
    nurse.give_urgency_lvl(patient)
    if patient.urgency_level >= 3:
        Emergency.assign_department(patient)
    else:
        General.assign_department(patient)


def assign_doctor(General, Emergency, nurse, patient):
    if patient.department == "General":
        output = nurse.assign_doctor(patient, General)
    else:
        output = nurse.assign_doctor(patient, Emergency)

    return output


class Person:
    def __init__(self, age=0, id=0, name=None, contact_info=None):
        self.age = age
        self.id = id
        self.name = name
        self.contact_info = contact_info

    @abstractmethod
    def view_info(self):
        return None

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID: {self.id}\nContact Info: {self.contact_info}"
