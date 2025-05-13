from abc import ABC, abstractmethod
from patient.py import *

# patient.registering_status: "discharged" (False) / "admitted" (True)
# patient.billing_status: "unpaid" (False) / "paid" (True)

# Service class - abstract class

class Service(ABC):
    @abstractmethod
    def status(self, patient):
        pass

# Registering class - inherits from Service

class Registering(Service):
    def __init__(self, doctor, patient, illness):
        self.doctor = doctor
        self.patient = patient
        self.illness = illness

    @property
    def final_result(self):
        return {
            "doctor": self.doctor,
            "patient": self.patient,
            "illness": self.illness
        }

    def discharge(self, patient):
        if patient.registering_status:
            patient.registering_status = False
        else:
            return "The patient has already been discharged." # maybe create an error for this? 

    def status(self, patient):
        if patient.registering_status:
            return f"The patient {patient.name} is currently admitted in our hospital."
        else:
            return f"The patient {patient.name} has been discharged from our hospital."

# Billing class - inherits from Service

class Billing(Service):
    def __init__(self, receipt):
        self.receipt = receipt # what is it tho? is it useful? doesn't look like it
        self.fees = {"Rehabilative": 0, "Pharmaceutical": 0, "Emergency": 0}

    def status(self, patient):
        if patient.billing_status:
            return f"The bill of patient {patient.name} has already been settled."
        else:
            return f"The bill of patient {patient.name} has yet to be settled."

    def get_price(self, patient, treatment):
        # treatment: "Rehabilative", "Pharmaceutical" or "Emergency" (string)
        if patient.health_insurance:
            return self.fees[treatment] * 0.4
        else:
            return self.fees[treatment]

    def calculate_total(self, patient):
        total = 0
        for treatment in patient.medical_history: # to check how medical_history is implemented
            total += self.get_price(patient, treatment)
        return f"The patient {patient.name} owes {total} in total."

    def process_payment(self, patient):
        if patient.billing_status:
            return "The payment has already been made." # maybe create an error for this?
        else:
            patient.billing_status = True
            return "The payment has been processed."

