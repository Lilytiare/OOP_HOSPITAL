from Hospital.Treatment.Treatment import *

class Pharmaceutical(Treatment):
    def __init__(self, name="General"):
        Treatment.__init__(self, name)
        self.tg_p = 0

    def give_treatment(self, patient):
        return "General"

    def __str__(self):
        return "General"

# f"{patient.name} got a pharmaceutical treatment !",