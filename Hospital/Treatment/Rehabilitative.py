from Hospital.Treatment.Treatment import *

class Rehabilitative(Treatment):
    def __init__(self, name="General"):
        Treatment.__init__(self, name)

    def give_treatment(self):
        return "Rehabilitative"

    def __str__(self):
        return "Rehabilitative"
