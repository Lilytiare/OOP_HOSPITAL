import pandas as pd

class Registration:
    def __init__(self, doctor, patient, illness):
        self.doctor = doctor
        self.patient = patient
        self.illness = illness

    @property
    def final_result(self):
        return {
            "doctor": self.doctor,
            "patient": self.patient,
            "illness": self.illness
        }

    def patient_register(self):
        data = pd.read_csv("sample_file.csv")
        data = pd.concat([data, pd.DataFrame([self.final_result])], ignore_index=True)
        data.to_csv("sample_file.csv")
        if self.doctor in data.doctor.to_list():
            return "The registration was successful !"
        else:
            return "Error with registration !"

sample_registration = Registration("house", "the-patient", "lung-flu")
print(sample_registration.patient_register())
