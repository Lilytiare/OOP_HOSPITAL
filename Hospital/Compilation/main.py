from Hospital.Person.Patient.Patient import Patient
from Hospital.Person.Staff.Doctor import Doctor
from Hospital.Person.Staff.Nurse import Nurse
from Hospital.Department.EmergencyDepartment import EmergencyDepartment
from Hospital.Department.GeneralPractice import GeneralPractice
from Hospital.Treatment.Pharmaceutical import Pharmaceutical
from Hospital.Treatment.Emergency import Emergency
from Hospital.Services.Billing import Billing
from Hospital.Services.Registering import Registration


def c_o(o):
    if o != None:
        print(o)


def assign_patient_to_department(nurse, patient):
    nurse.give_urgency_lvl(patient)
    if patient.urgency_level >= 3:
        Emergency.assign_department(patient)
    else:
        General.assign_department(patient)


def assign_doctor(General, Emergency, nurse, patient):
    if patient.department == "General":
        output = nurse.assign_doctor(patient, General)
    else:
        output = nurse.assign_doctor(patient, Emergency)

    return output


if __name__ == "__main__":
    GP = GeneralPractice()
    ED = EmergencyDepartment()
    treatmentGP = Pharmaceutical()
    treatmentED = Emergency()

    RS = Registration()
    BS = Billing()

    patient1 = Patient(12, 1, "Sett", "1234-5678")
    patient2 = Patient(12, 1, "Ann", "1234-5678")
    patient3 = Patient(12, 1, "Eve", "1234-5678")
    Dr1 = Doctor(44, 1, "Jones", "010-2000-0020", "night", "", "Doctor", [], 3)
    Dr2 = Doctor(44, 1, "Bones", "010-2000-0020", "night", "", "Doctor", [], 3)
    N1 = Nurse(44, 1, "Susy", "010-0111-1111", "night", "General")

    GP.add_staff(Dr1)
    ED.add_staff(Dr2)

    ED.add_staff(N1)
    GP.add_staff(N1)

    assign_patient_to_department(GP, ED, N1, patient1)
    assign_patient_to_department(GP, ED, N1, patient2)
    assign_patient_to_department(GP, ED, N1, patient3)

    o = assign_doctor(GP, ED, N1, patient1)
    c_o(o)
    print()
    print(Dr1.treatment(patient1, treatmentED, treatmentGP))
    o = assign_doctor(GP, ED, N1, patient2)
    c_o(o)
    print()
    print(Dr1.treatment(patient2, treatmentED, treatmentGP))
    o = assign_doctor(GP, ED, N1, patient3)
    c_o(o)
    print()
    print(Dr2.treatment(patient3, treatmentED, treatmentGP))
    print()

    print(patient1.view_appointment())
    print(patient1.view_medical_history())
    print(patient2.view_appointment())
    print(patient2.view_medical_history())
    print(patient3.view_appointment())
    print(patient3.view_medical_history())

    print(Dr1.get_current_patients())
    print(Dr2.get_current_patients())
    print("__________________________________________________")

    o = assign_doctor(GP, ED, N1, patient1)
    c_o(o)
    print()
    print(Dr1.treatment(patient1, treatmentED, treatmentGP))
    o = assign_doctor(GP, ED, N1, patient2)
    c_o(o)
    print()
    print(Dr1.treatment(patient2, treatmentED, treatmentGP))
    o = assign_doctor(GP, ED, N1, patient3)
    c_o(o)
    print()
    print(Dr2.treatment(patient3, treatmentED, treatmentGP))
    print()

    print(patient1.view_appointment())
    print(patient1.view_medical_history())
    print(patient2.view_appointment())
    print(patient2.view_medical_history())
    print(patient3.view_appointment())
    print(patient3.view_medical_history())

    print(Dr1.get_current_patients())
    print(Dr2.get_current_patients())

    print(RS.status(patient1))

    print(Dr1.discharge(patient3))
    print(f"Registering status of {patient1.name}:", patient1.registering_status)
    print(Dr1.discharge(patient1))
    print(f"Registering status of {patient1.name}:", patient1.registering_status)

    print(RS.status(patient1))

    print(BS.get_price(patient1, treatmentED))
    print(patient1.medical_history)
    print(BS.calculate_total(patient1))

    print(BS.status(patient1))
    print(BS.process_payment(patient1))
    print(BS.status(patient1))
    print(BS.process_payment(patient1))