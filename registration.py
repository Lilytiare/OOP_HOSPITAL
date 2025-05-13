import pandas as pd

class Registration:
    def __init__(self, doctor, patient, illness):
        self.doctor = doctor
        self.patient = patient
        self.illness = illness
        self.final_result = {
            "doctor": self.doctor,
            "patient": self.patient,
            "illness": self.illness
        }
        self.filename = "sample_file.csv"
    def get_data(self):
        try:
            data = pd.read_csv(self.filename)
        except pd.errors.EmptyDataError:
            data = pd.DataFrame(columns=["doctor", "patient", "illness"])
            data.to_csv(self.filename, index=False)
            data = pd.read_csv(self.filename)

        new_row = pd.DataFrame([self.final_result])
        data = pd.concat([data, new_row], ignore_index=True)

        data.to_csv(self.filename, index=False)
        return data

    def patient_register(self):
        data = self.get_data()
        if self.doctor in data["doctor"].to_list():
            return "The registration was successful!"
        else:
            return "Error with registration!"

