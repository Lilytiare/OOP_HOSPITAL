from Hospital.Treatment.Treatment import *

class Rehabilitative(Treatment):
    def __init__(self, name="General"):
        Treatment.__init__(self, name)
        self.tg_pp = 0

    def give_treatment(self, patient):
        return "General"

    def __str__(self):
        return "General"
    # def give_treatment(self, patient):
    #     return f"{patient.name} got a rehabilitative treatment !"