from abc import ABC, abstractmethod

class Department(ABC):
    def __init__(self, name):
        self._name = name
        self._staff = []
        self.doctors = []
        self.nurses = []
        self.list_of_patients = []

    def remove_staff(self, staff):
        if staff in self._staff:
            self._staff.remove(staff)
            print(f"{staff.name} removed from {self._name} department.")
        else:
            print(f"{staff.name} is not in {self._name} department.")

    def view_staff(self):
        if len(self._staff) == 0:
            return f"No staff in {self._name} department."
        members = ""
        for s in self._staff:
            members += s + "\n"
        return f"{self._name} Staff:\n" + members.strip()

    def view_patients(self):
        if len(self.list_of_patients) == 0:
            return f"No Patients in {self._name} department."
        members = ""
        for s in self.list_of_patients:
            members += s.name + "\n"
        return f"{self._name} Patients:\n" + members.strip()

    @abstractmethod
    def perform_task(self):
        pass

    @abstractmethod
    def handle_treatment(self, patient, treatment):
        pass

    @abstractmethod
    def add_staff(self, staff):
        pass