from Hospital.Person.Person import *

class Patient(Person):
    def __init__(self, age=0, id=0, name=None, contact_info=None, urgency_level=0, health_insurance=False):
        Person.__init__(self, age, id, name, contact_info)
        self.urgency_level = urgency_level
        self.health_insurance = health_insurance
        self.medical_history = []
        self.doctors_appointed = []
        self.department = None
        self.billing_status = False
        self.registering_status = False
        self.p_p = 0

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
            output += i.name + ', '
        output = output[:-2]
        return output