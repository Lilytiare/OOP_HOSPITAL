from Hospital.Department.Department import *

class GeneralPractice(Department):
    def __init__(self, name="General Practice", capacity=20):
        super().__init__(name)
        self.capacity = capacity

    def perform_task(self):
        return "General Practice is conducting standard health checks."

    def handle_treatment(self, patient, treatment):
        return treatment.give_treatment(patient)

    def assign_department(self, patient):
        if len(self.list_of_patients) < self.capacity:
            self.list_of_patients.append(patient)
            patient.department = "General"
        else:
            return "General Practice is at full capacity!"

    def add_staff(self, staff):
        self._staff.append(staff)
        try:
            spec = staff.specialization
            self.doctors.append(staff)
            staff.department = "general"
        except:
            self.nurses.append(staff)
            staff.department = "general"
        return f"{staff.name} added to {self._name} department."