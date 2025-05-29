from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pandas as pd
import json

from numpy.ma.core import inner

from Hospital.Person.Person import assign_doctor
from Hospital.Services.Registering import Registration, STAFF_FILENAME
from Hospital.Person.Patient.Patient import Patient
from Hospital.Person.Staff.Doctor import Doctor
from Hospital.Department.EmergencyDepartment import EmergencyDepartment
from Hospital.Department.GeneralPractice import GeneralPractice

global department_name
global patient
global staff
global global_role
global global_id
global department



BACKGROUND_IMAGE_PATH = 'images/img.png'
ICON_IMAGE_PATH = 'images/img_1.png'
PATIENT_REGISTRATION_IMAGE = 'images/img_2.png'
VIEW_INFO_IMAGE = 'images/img_3.png'

PATIENTS_FILENAME = ''
list_of_department_patients =[]

# remove_staff() -> admin
# add_staff() -> admin
# Change department
# appoint doctor -> Nurse
#edit filenames
# Maybe we should have 3 lists containing 3

def patient_registration():
    root = Toplevel()
    root.title("Hospital Management System")
    root.geometry("535x300")

    original_bg = Image.open(PATIENT_REGISTRATION_IMAGE)
    resized_bg = ImageTk.PhotoImage(original_bg.resize((535, 300)))

    bg_label = Label(root, image=resized_bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(root, text="Full Name: ").place(x=250, y=30)
    name_input = Entry(root, width=17)
    name_input.place(x=330, y=30)
    name_input.focus()

    Label(root, text="Age: ").place(x=250, y=60)
    age_input = Entry(root, width=17)
    age_input.place(x=300, y=60)

    Label(root, text="ID: ").place(x=260, y=90)
    id_input = Entry(root, width=17)
    id_input.place(x=300, y=90)

    Label(root, text="Contact Info: ").place(x=270, y=120)
    contact_info = Entry(root, width=17)
    contact_info.place(x=360, y=120)

    Label(root, text="Urgency Level: ").place(x=330, y=180)
    urgency_level = Entry(root, width=17)
    urgency_level.place(x=420, y=180)

    selected_option = IntVar()
    selected_option.set(0)

    Label(root, text="Health Insurance: ").place(x=300, y=150)
    radio1 = Radiobutton(root, text="Yes",variable=selected_option,value=1)
    radio1.place(x=420, y=150)
    radio2 = Radiobutton(root, text="No",variable=selected_option,value=0)
    radio2.place(x=470, y=150)

    def collect_data():
        global patient
        patient = Patient(age_input.get(),id_input.get(),name_input.get(),contact_info.get(),urgency_level = urgency_level.get(),health_insurance=bool(selected_option.get()))
        register = Registration()
        register.patient_register(patient, f'C:/Users/umarb/PycharmProjects/OOP_HOSPITAL/Hospital/Compilation/Data Base/{department_name}.csv')
        root.destroy()
    Button(root, text="Register", command=collect_data, width=15).place(x=370, y=210)

    root.mainloop()
    return age_input.get(),id_input.get(),name_input.get(),contact_info.get(),urgency_level.get(),bool(selected_option.get())
def view_info():
    # messagebox.showinfo(title=f"{patient.id}", message=f"Patient: {patient.name}, ID: {patient.id}\n Age: {patient.age}, Contact Info: {patient.contact_info} was registered successfully")
    output_text = f"Employee: {staff.name}\nID: {staff.id}\nAge: {staff.age}\nContact Info: {staff.contact_info}\nShift: {staff.shift}\nDepartment: {staff.department}\n"
    if global_role == "doctor":
        output_text += f"Specialization: {staff.specialization}\nList of Patients: {" ".join(staff.list_of_patients)}\nCurrent busyness: {len(staff.list_of_patients)}/{staff.max_patients}"
    messagebox.showinfo(title=f"{global_role.capitalize()}", message=output_text)
def main_page_compilation(input_role, input_id, inner_department_name):
    global global_role
    global_role = input_role

    global global_id
    global_id = input_id

    global department
    department = GeneralPractice(20) if inner_department_name == "general" else EmergencyDepartment(20)

    global department_name
    department_name  = inner_department_name
    global PATIENTS_FILENAME
    PATIENTS_FILENAME = f'C:/Users/umarb/PycharmProjects/OOP_HOSPITAL/Hospital/Compilation/Data Base/{inner_department_name}.csv'
    patients_data = pd.read_csv(PATIENTS_FILENAME)

    root = Tk()
    root.title("Hospital Management System")
    root.geometry("740x416")
    icon = PhotoImage(file=ICON_IMAGE_PATH)
    root.iconphoto(False, icon)

    bg_image = PhotoImage(file=BACKGROUND_IMAGE_PATH)
    Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)

    Label(root, text=department.perform_task(), font=("Helvetica", 17, "bold"), fg="#DA6C6C").place(relx=0.5, y=20, anchor='n')

    if global_role == "nurse":
        Button(root, text="Patient registration", command=patient_registration, width=15).place(x=470, y=80)
        # Button(root, text="Assign Patient to Doctor", command=assign_patient_to_department, width=20).place(x=270, y=140)
    Button(root, text="View Info", command=view_info, width=15).place(x=270, y=80)
    Button(root, text="Patients List", command=patients_list, width=15).place(x=270, y=110)
    Button(root, text="Staff List", command=staff_list, width=15).place(x=470, y=110)

    root.mainloop()
def patients_list():
    department.list_of_patients = list_of_department_patients
    messagebox.showinfo(title="List of Patients", message=department.view_patients())
def staff_list():
    with open('C:/Users/umarb/PycharmProjects/OOP_HOSPITAL/Hospital/Compilation/Data Base/staff.json') as file:
        staff_data = json.load(file)
        list_of_staff = [value["name"] for key, value in staff_data.items() if value["department"] == department_name]
    department._staff = list_of_staff
    messagebox.showinfo(title="List of Staff", message=department.view_staff())

# def assign_patient_to_department():
#     if patient.urgency_level >= 3:
#         department.assign_department(patient.name)
#         data = pd.read_csv(f'C:/Users/umarb/PycharmProjects/OOP_HOSPITAL/Hospital/Compilation/Data Base/{department_name}.csv')
#         new_row = pd.DataFrame([final_result])
#         data = pd.concat([data, new_row], ignore_index=True)
#         data.to_csv(filename, index=False)
#     else:
#         department.assign_department(patient)

# main_page_compilation("nurse", "7654321")
# patient_registration()