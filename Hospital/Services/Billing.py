from Hospital.Services.Service import *

class Billing(Service):
    def __init__(self, name="Billing"):
        self.name = name # what is it tho? is it useful? doesn't look like it
        self.fees = {"General": 0.5, "Emergency": 1}
        self.b_p = 0

    def status(self, patient):
        if patient.billing_status:
            return f"The bill of patient {patient.name} has already been settled."
        else:
            return f"The bill of patient {patient.name} has yet to be settled."

    def get_price(self, patient, treatment):
        # treatment: "General" or "Emergency" (string)
        if patient.health_insurance:
            try:
                return self.fees[treatment.name] * 0.4
            except:
                return self.fees[treatment] * 0.4
        else:
            try:
                return self.fees[treatment.name]
            except:
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