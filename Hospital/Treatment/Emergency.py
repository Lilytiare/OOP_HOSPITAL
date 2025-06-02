from Hospital.Treatment.Treatment import *

class Emergency(Treatment):
    def __init__(self, name="Emergency"):
        Treatment.__init__(self, name)

    def give_treatment(self):
        return "Emergency"

    def __str__(self):
        return "Emergency"
# f"{patient.name} got an emergency treatment !",