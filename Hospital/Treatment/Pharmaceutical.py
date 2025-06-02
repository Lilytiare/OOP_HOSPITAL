from Hospital.Treatment.Treatment import *

class Pharmaceutical(Treatment):
    def __init__(self, name="General"):
        Treatment.__init__(self, name)

    def give_treatment(self):
        return "Pharmaceutical"

    def __str__(self):
        return "Pharmaceutical"

# f"{patient.name} got a pharmaceutical treatment !",