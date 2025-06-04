from Hospital.Services.Service import *

class Billing(Service):
    def __init__(self, name="Billing"):
        self.name = name
        self.fees = {"Emergency": 40000, "Pharmaceutical": 25000, "Rehabilitative": 50000}

    def status(self, patient):
        if patient.billing_status:
            return f"The bill of patient {patient.name} has already been settled."
        else:
            return f"The bill of patient {patient.name} has yet to be settled."

    def get_price(self, patient, treatment):
        if patient.health_insurance:
            return self.fees[treatment] * 0.8
        else:
            return self.fees[treatment]

    def calculate_total(self, patient):
        total = 0
        for treatment in patient.medical_history: # to check how medical_history is implemented
            total += int(self.get_price(patient, treatment))
        return f"The patient {patient.name} owes {total} in total."

    def process_payment(self, patient):
        if patient.billing_status:
            return "The payment has already been made."
        else:
            patient.billing_status = True
            return "The payment has been processed."