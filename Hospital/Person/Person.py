from abc import abstractmethod

class Person:
    def __init__(self, age=0, id=0, name=None, contact_info=None):
        self.age = age
        self.id = id
        self.name = name
        self.contact_info = contact_info

    @abstractmethod
    def view_info(self):
        return None

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID: {self.id}\nContact Info: {self.contact_info}"
