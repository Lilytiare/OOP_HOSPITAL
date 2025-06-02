from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog
import pandas as pd
import json

from Hospital.Services.Registering import *
from Hospital.Person.Patient.Patient import Patient
from Hospital.Person.Staff.Doctor import Doctor
from Hospital.Person.Staff.Nurse import *
from Hospital.Department.EmergencyDepartment import EmergencyDepartment
from Hospital.Department.GeneralPractice import GeneralPractice
from Hospital.Treatment.Emergency import Emergency
from Hospital.Treatment.Pharmaceutical import Pharmaceutical
from Hospital.Treatment.Rehabilitative import Rehabilitative

global department_name
global staff
global global_role
global global_id
global department
global drs_patients


BACKGROUND_IMAGE_PATH = 'images/img.png'
ICON_IMAGE_PATH = 'images/img_1.png'
PATIENT_REGISTRATION_IMAGE = 'images/img_2.png'
VIEW_INFO_IMAGE = 'images/img_3.png'
PATIENTS_FILENAME = ''

def parse_patients():
    patients_data = pd.read_csv(PATIENTS_FILENAME)
    list_of_department_patients = []
    for index, row in patients_data.iterrows():
        row_dict = row.to_dict()
        if row_dict["registering_status"]:
            list_of_department_patients.append(Patient(row_dict["age"], row_dict["id"],row_dict["name"], row_dict["contact_info"], row_dict["urgency_level"], row_dict["health_insurance"]))
    return list_of_department_patients
def parse_staff():
    with open('C:/Users/umarb/PycharmProjects/OOP_HOSPITAL/Hospital/Compilation/Data Base/staff.json') as file:
        staff_data = json.load(file)
        list_of_roles = []
        for key, value in staff_data.items():
            if value["department"] == department_name:
                value["id"] = key
                list_of_roles.append(value)
        list_of_nurses = [Nurse(value["age"], value["id"], value["name"], value["contact_info"],value["shift"], department_name) for value in list_of_roles if value["role"] == "nurse"]
        list_of_doctors = [Doctor(value["age"], value["id"], value["name"], value["contact_info"],value["shift"], department_name, value["specialization"],value["list_of_patients"], value["max_patients"]) for value in list_of_roles if value["role"] == "doctor"]
    return list_of_doctors,list_of_nurses,list_of_doctors + list_of_nurses

# remove_staff() -> admin
# add_staff() -> admin

# appoint doctor -> Nurse --------------Done
# edit filenames

# Now edit the 2 registration methods to be more versatile, so that it could be reused !
# ----^-----Done
# TODO-1:Now construct the Admin's and Doctor's pages ! - >Done<
# TODO-2: Change department -> possibly nurse
# TODO-3: Use department class's assign_department for switching patients between the departments
# TODO-4: Add the department input if the user is admin - >Done<
# TODO -> Doctor, 2 Departments' methods to swap patients, Billing, Patients' status methods
# --------^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^----------

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
        patient = Patient(age_input.get(),id_input.get(),name_input.get(),contact_info.get(),urgency_level = urgency_level.get(),health_insurance=bool(selected_option.get()))
        register = Registration()
        register.patient_register(patient, f'C:/Users/umarb/PycharmProjects/OOP_HOSPITAL/Hospital/Compilation/Data Base/{department_name}.csv')
        root.destroy()
    Button(root, text="Register", command=collect_data, width=15).place(x=370, y=210)
    root.mainloop()
def staff_registration():
    root = Toplevel()
    root.title("Hospital Management System")

    root.geometry("600x370")
    bg_image = PhotoImage(file=VIEW_INFO_IMAGE)
    Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)

    Label(root, text="Full Name: ").place(x=350, y=30)
    name_input = Entry(root, width=17)
    name_input.place(x=420, y=30)
    name_input.focus()

    Label(root, text="Age: ").place(x=350, y=60)
    age_input = Entry(root, width=17)
    age_input.place(x=390, y=60)

    Label(root, text="ID: ").place(x=350, y=90)
    id_input = Entry(root, width=17)
    id_input.place(x=380, y=90)

    Label(root, text="Role: ").place(x=350, y=120)
    role = Entry(root, width=17)
    role.place(x=400, y=120)

    Label(root, text="Contact Info: ").place(x=350, y=150)
    contact_info = Entry(root, width=17)
    contact_info.place(x=435, y=150)

    Label(root, text="Shift: ").place(x=350, y=180)
    shift = Entry(root, width=17)
    shift.place(x=400, y=180)

    Label(root, text="Password: ").place(x=350, y=210)
    password = Entry(root, width=17)
    password.place(x=430, y=210)
    def collect_data():
        if role.get() == "doctor":
            reg_staff = Doctor(age_input.get(),id_input.get(),name_input.get(),contact_info.get(),shift.get(),department_name, department_name,[],10)
        elif role.get() == "nurse":
            reg_staff = Nurse(age_input.get(),id_input.get(),name_input.get(),contact_info.get(),shift.get(),department_name)
        else:
            raise KeyError("Wrong role inserted")
        register = Registration()
        msg = register.staff_register(reg_staff,password.get())
        messagebox.showinfo(title=f"Registering Status", message=msg)
        root.destroy()
    Button(root, text="Register", command=collect_data, width=15).place(x=370, y=250)
    root.mainloop()
def dismiss_staff():
    staff_id = simpledialog.askstring("Staff ID", "Please enter the staff ID you want to dismiss:")
    with open(STAFF_FILENAME, "r") as file:
        data = json.load(file)
    if staff_id in data.keys():
        del data[staff_id]
        with open(STAFF_FILENAME, "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo(title="Status",message=f"Staff ID {staff_id} deleted successfully.")
    else:
        messagebox.showinfo(title="Status",message=f"Staff ID {staff_id} not found.")
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
    parse_patients()

    global staff
    for item in parse_staff()[2]:
        if item.id == global_id:
            staff = item
    department.doctors = parse_staff()[0]
    department.nurses = parse_staff()[1]

    root = Tk()
    root.title("Hospital Management System")
    root.geometry("740x416")
    icon = PhotoImage(file=ICON_IMAGE_PATH)
    root.iconphoto(False, icon)

    bg_image = PhotoImage(file=BACKGROUND_IMAGE_PATH)
    Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)

    Label(root, text=department.perform_task(), font=("Helvetica", 17, "bold"), fg="#DA6C6C").place(relx=0.5, y=20, anchor='n')


    Button(root, text="Patients List", command=patients_list, width=15).place(x=270, y=110)
    Button(root, text="Staff List", command=staff_list, width=15).place(x=470, y=110)
    if global_role == "nurse":
        Button(root, text="Patient registration", command=patient_registration, width=15).place(x=470, y=80)
        Button(root, text="Assign Patient to Doctor", command=doctor_assignation, width=20).place(x=270, y=140)
    if global_role != "admin":
        Button(root, text="View Info", command=view_info, width=15).place(x=270, y=80)
    if global_role == "admin":
        Button(root, text="Register Staff", command=staff_registration, width=20).place(x=470, y=80)
        Button(root, text="Dismiss Staff", command=dismiss_staff, width=20).place(x=270, y=80)
    if global_role == "doctor":
        global drs_patients
        drs_patients = staff.get_current_patients()
        Button(root,text=f"Dr.{staff.name}'s Patients List",
            command=lambda: (
                messagebox.showinfo(title="Hospital Management System",message=drs_patients)
            ),width=20).place(x=470, y=80)
        Button(root, text="Call time of Death", command=call_death_time, width=20).place(x=470, y=140)
        Button(root, text="Discharge Patient", command=discharge_patient, width=20).place(x=470, y=170)
        Button(root, text="Treat Patient", command=treat_patient, width=20).place(x=470, y=200)

    root.mainloop()
def patients_list():
    root = Toplevel()
    root.title("Hospital Management System")
    original_bg = Image.open(VIEW_INFO_IMAGE)
    root.geometry("380x222")
    resized_bg = ImageTk.PhotoImage(original_bg.resize((380, 222)))
    department.list_of_patients = parse_patients()
    messagebox.showinfo(title="List of Patients", message=department.view_patients())
def staff_list():
    department._staff = parse_staff()[2]
    messagebox.showinfo(title="List of Staff", message=department.view_staff())
def view_info():
    messagebox.showinfo(title=f"{global_role.capitalize()}", message=staff.view_info())
def doctor_assignation():
    root = Toplevel()
    root.title("Hospital Management System")
    original_bg = Image.open(VIEW_INFO_IMAGE)
    root.geometry(f"380x{len(parse_patients()) * 30 + 60}")
    resized_bg = ImageTk.PhotoImage(original_bg.resize((380, 222)))
    bg_label = Label(root, image=resized_bg, padx=10,pady=10)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    def handle_assign(p):
        msg = staff.assign_doctor(p, department)
        if isinstance(msg, Doctor):
            doctor = msg
            save_staff_data(doctor.list_of_patients, doctor.id,"list_of_patients")
            edit_patient_data(file_path=PATIENTS_FILENAME, searched_row=p.id, searched_column="doctors_appointed" ,value=doctor.name, action="append")
            messagebox.showinfo(message=f"{p.name.capitalize()} has been assigned to Dr. {doctor.name.capitalize()}")
            root.destroy()
        else:
            messagebox.showwarning("Assignment Failed", msg)
    for x, patient in enumerate(parse_patients(), start=1):
        Button(
            root,
            text=f"{patient.name}: {patient.id}",
            command=lambda p=patient: handle_assign(p),
            width=15
        ).place(relx=0.5, y=x * 30)
    root.mainloop(),
def call_death_time():
    root = Toplevel()
    root.title("Hospital Management System")
    height = len(parse_patients()) * 30 + 60
    root.geometry(f"380x{height}")
    original_bg = Image.open(VIEW_INFO_IMAGE)
    resized_bg = ImageTk.PhotoImage(original_bg.resize((380, height)))
    bg_label = Label(root, image=resized_bg, padx=10, pady=10)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    def handle_time(p):
        messagebox.showinfo(message=staff.call_time_of_death(p))
        edit_patient_data(PATIENTS_FILENAME,p.id,"registering_status",False,"edit")
        edit_patient_data(PATIENTS_FILENAME,p.id,"billing_status",False,"edit")
        root.destroy()
    for x, patient in enumerate(parse_patients(), start=1):
        Button(root,
            text=f"{patient.name}: {patient.id}",
            command=lambda p=patient: handle_time(p),
            width=15
        ).place(relx=0.5, y=x * 30)
    root.mainloop()
def discharge_patient():
    root = Toplevel()
    root.title("Hospital Management System")
    height = len(parse_patients()) * 30 + 60
    root.geometry(f"380x{height}")
    original_bg = Image.open(VIEW_INFO_IMAGE)
    resized_bg = ImageTk.PhotoImage(original_bg.resize((380, height)))
    bg_label = Label(root, image=resized_bg, padx=10, pady=10)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def handle_discharge(p):
        p_list,msg = staff.discharge(p)
        save_staff_data(p_list, staff.id, "list_of_patients")
        edit_patient_data(PATIENTS_FILENAME,p.id,"registering_status",False,"edit")
        messagebox.showinfo(title="Hospital Management System", message=msg)
        root.destroy()
    for x, patient in enumerate(parse_patients(), start=1):
        Button(root,
            text=f"{patient.name}: {patient.id}",
            command=lambda p=patient: handle_discharge(p),
            width=15
        ).place(relx=0.5, y=x * 30)
    root.mainloop()
def treat_patient():
    root = Toplevel()
    root.title("Hospital Management System")
    height = len(parse_patients()) * 30 + 100
    root.geometry(f"380x{height}")
    original_bg = Image.open(VIEW_INFO_IMAGE)
    resized_bg = ImageTk.PhotoImage(original_bg.resize((380, height)))
    bg_label = Label(root, image=resized_bg, padx=10, pady=10)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    if department_name != "emergency":
        treatment_input = Entry(root, width=17)
        treatment_input.place(x=60, y=30)
    def handle_treatment(p):
        if department_name != "emergency":
            input_value = treatment_input.get().lower()
            treatment_type = Rehabilitative if input_value == "rehabilitative" else Pharmaceutical
            treatment = treatment_type()
        else:
            treatment = Emergency()
        tmnt, msg = staff.treat(p,treatment)
        edit_patient_data(PATIENTS_FILENAME,p.id,"medical_history",tmnt,"append")
        messagebox.showinfo(title="Hospital Management System", message=msg)
        root.destroy()

    for x, patient in enumerate(parse_patients(), start=1):
        Button(root,
            text=f"{patient.name}: {patient.id}",
            command=lambda p=patient: handle_treatment(p),
            width=15
        ).place(relx=0.5, y=x * 30)

    root.mainloop()



# main_page_compilation("house", "1234567", "emergency")
# staff_registration()