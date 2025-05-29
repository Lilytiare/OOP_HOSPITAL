from Hospital.Department.Department import *

class EmergencyDepartment(Department):
    def __init__(self, name="Emergency Department", capacity=10):
        super().__init__(name)
        self.capacity = capacity
        self.e_p = 0

    def perform_task(self):
        return "Emergency Department is responding to urgent cases."

    def handle_treatment(self, patient, treatment):
        return treatment.give_treatment(patient)
    def add_staff(self, staff):
        self._staff.append(staff)
        try:
            spec = staff.specialization
            self.doctors.append(staff)
            staff.department = "Emergency"
        except:
            self.nurses.append(staff)
            staff.department = "Emergency"
        print(f"{staff.name} added to {self._name} department.")

    def assign_department(self, patient):
        if len(self.list_of_patients) < self.capacity:
            self.list_of_patients.append(patient)
            patient.department = "Emergency"
        else:
            return "Emergency Department is at full capacity!"