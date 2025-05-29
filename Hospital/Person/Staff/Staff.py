from Hospital.Person.Person import *

class Staff(Person):
    def __init__(self, age, id, name, contact_info, shift: str, department: str):
        super().__init__(age, id, name, contact_info)
        self.shift = shift
        self.department = department

    def view_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Contact Information: {self.contact_info}\n Shift: {self.shift}"