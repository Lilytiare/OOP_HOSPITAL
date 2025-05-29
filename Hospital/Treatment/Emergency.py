from Hospital.Treatment.Treatment import *

class Emergency(Treatment):
    def __init__(self, name="Emergency"):
        Treatment.__init__(self, name)
        self.te_p = 0

    def give_treatment(self, patient):
        return "Emergency"

    def __str__(self):
        return "Emergency"
# f"{patient.name} got an emergency treatment !",