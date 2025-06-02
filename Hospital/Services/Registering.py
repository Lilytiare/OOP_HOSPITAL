
import pandas as pd
import ast
STAFF_FILENAME = '../Compilation/Data Base/staff.json'

from Hospital.Person.Patient.Patient import *
import json
class Registration:
    def save_edit_patient_data(self, patient, filename):
        final_result = {
            "seq_id": 0,
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "contact_info": patient.contact_info,
            "urgency_level": patient.urgency_level,
            "health_insurance": patient.health_insurance,
            "medical_history": [],
            "doctors_appointed": [],
            "registering_status": True,
            "billing_status": True
        }
        try:
            data = pd.read_csv(filename)
        except (pd.errors.EmptyDataError, FileNotFoundError):
            data = pd.DataFrame(columns=["seq_id","id", "name", "age", "contact_info", "urgency_level", "health_insurance", "medical_history", "doctors_appointed", "registering_status", "billing_status"])
            data.to_csv(filename, index=False)
            data = pd.read_csv(filename)
        data_list = data.seq_id.to_list()
        final_result["seq_id"] = len(data_list)
        new_row = pd.DataFrame([final_result])
        data = pd.concat([data, new_row], ignore_index=True)
        data.to_csv(filename, index=False)
        return data, patient.id

    def save_edit_staff_data(self, staff, pwd):
        final_result = {staff.id:{
            "age": staff.age,
            "role": staff.role,
            "name": staff.name,
            "password": pwd,
            "contact_info": staff.contact_info,
            "shift": staff.shift,
            "department": staff.department,
        }}
        if final_result[staff.id]["role"] == "doctor":
            final_result[staff.id]["specialization"] = staff.specialization
            final_result[staff.id]["list_of_patients"]=staff.list_of_patients
            final_result[staff.id]["max_patients"] = staff.max_patients
        try:
            with open(STAFF_FILENAME, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(STAFF_FILENAME, "w") as data_file:
                json.dump(final_result, data_file, indent=4)
        else:
            data.update(final_result)
            with open(STAFF_FILENAME, "w") as data_file:
                json.dump(data, data_file, indent=4)
        return data, staff.id

    def patient_register(self, patient, filename):
        data, patient_id = self.save_edit_patient_data(patient, filename=filename)
        if patient_id in data["id"].to_list():
            return "The registration was successful!"
        else:
            return "Error with registration!"
    def staff_register(self, staff, pwd):
        data,staff_id = self.save_edit_staff_data(staff, pwd)
        if staff_id in list(data.keys()):
            return "The registration was successful!"
        else:
            return "Error with registration!"

def edit_patient_data(file_path, searched_row, searched_column, value,action):
    data = pd.read_csv(file_path)
    cell_val = data.loc[data["id"] == searched_row, searched_column].values[0]
    if action == "append":
        if isinstance(cell_val, str):
            try:
                cell_list = ast.literal_eval(cell_val)
                if not isinstance(cell_list, list):
                    cell_list = [cell_list]
            except Exception:
                cell_list = [cell_val]
        elif isinstance(cell_val, list):
            cell_list = cell_val
        else:
            cell_list = [cell_val]
        cell_list.append(value)
        data.loc[data["id"] == searched_row, searched_column] = str(cell_list)
    elif action == "edit":
        data.loc[data["id"] == searched_row, searched_column] = value
    data.to_csv(file_path, index=False)

def save_staff_data(assign_value,searched_key, searched_value):
    with open(STAFF_FILENAME, "r+") as file:
        staff_data = json.load(file)
        file.seek(0)
        staff_data[searched_key][searched_value] = assign_value
        json.dump(staff_data, file, indent=4)
        file.truncate()