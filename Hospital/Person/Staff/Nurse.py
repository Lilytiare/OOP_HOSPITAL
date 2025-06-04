from Hospital.Person.Staff.Staff import *

class Nurse(Staff):
    def __init__(self, age, id, name, contact_info, shift, department: str):
        super().__init__(age, id, name, contact_info, shift, department)
        self.role = "nurse"

    def view_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Contact Information: {self.contact_info}\n Shift: {self.shift}\n Department: {self.department}"

    def assign_doctor(self, patient, department):
        for d in department.doctors:
            if len(d.list_of_patients) >= d.max_patients:
                return f"Dr. {d.name} is at full capacity!"
            else:
                d.list_of_patients.append(patient.name)
                patient.doctors_appointed.append(d.name)
                patient.registering_status = True
                return d


