
# Hospital Management System

## Overview

This Hospital Management System is a Python-based application developed with **Object-Oriented Programming (OOP)** principles. It provides a structured way to manage hospital departments, staff, patients, services, and treatments. The project features a GUI-based interface for intuitive interaction, designed to simulate real-world hospital operations.

## Objectives

- Model a hospital's internal systems using OOP
- Implement inheritance, encapsulation, and polymorphism
- Simulate real-time operations like billing, registration, and patient care
- Provide a user-friendly graphical interface for interaction

## Purpose

The purpose of the Project is to address the issues with managing the Hospital, with a real life simulations.

## Class Architecture

### Core Classes and Relationships

| Category     | Classes                                                                 |
|--------------|-------------------------------------------------------------------------|
| Person       | `Person`, `Staff(Person)`, `Patient(Person)`                           |
| Staff Types  | `Doctor(Staff)`, `Nurse(Staff)`                                         |
| Department   | `Department`, `GeneralPractice(Department)`, `EmergencyDepartment(Department)` |
| Treatment    | `Treatment`, `Pharmaceutical(Treatment)`, `Rehabilitative(Treatment)`, `Emergency(Treatment)` |
| Service      | `Service`, `Billing(Service)`, `Register(Service)`                      |

Each class was designed to represent real-world entities within a hospital and maintain clear interactions through OOP design.

##  User Interface

The program runs on a **Graphical User Interface (GUI)** that allows users to:
- Register new patients
- Assign treatments and departments
- View and manage billing and services
- Organize staff by roles and departments

## Project Structure

```bash
OOP_HOSPITAL/
|-- Hospital/
|   |-- Compilation/
|   |   |-- Data Base/                      # DataBase of program  
|   |   |   |-- emergency.csv               # Data of Emergency Department
|   |   |   |-- general.csv                 # Data of General Department
|   |   |   |-- staff.json                  # Data of Staffs
|   |   |   
|   |   |-- images/                         # Prefabs of images
|   |   |   |-- img.png                     # Image for background for login page 
|   |   |   |-- img_1.png                   # Image for Icon of the program
|   |   |   |-- img_2.png                   # Image for background of patient registration page
|   |   |   |-- img_3.png                   # Image for background of staff registration page
|   |   |                
|   |   |-- main_page.py                    # GUI layout and functionality
|   |
|   |-- Department/                     # Department and sub-classes
|   |   |-- Department.py               # Base class - Department
|   |   |-- EmergencyDepartment.py      # Derived class EmergencyDepartment from base class Department
|   |   |-- GeneralPractice.py          # Derived class GeneralPractice from base class Department 
|   |
|   |-- Person/                          # Person and sub-classes
|   |   |-- Patient/                    # Patient class
|   |   |   |-- Patient.py              # Derived class Patient from base class Person
|   |   |
|   |   |-- Staff/                      # Staff class and sub-classes
|   |   |   |-- Doctor.py               # Derived class Doctor from base class Staff
|   |   |   |-- Nurse.py                # Derived class Nurse form base class Staff
|   |   |   |-- Staff.py                # Derived class Staff from base class Person
|   |   |
|   |   |-- Person.py                   # Base class Person
|   |
|   |-- Services/                       # Service and sub-classes
|   |   |-- Billing.py                  # Derived class Billing from base class Service
|   |   |-- Registering.py              # Derived class Registering from base class Service
|   |   |-- Service.py                  # Base class Service
|   |
|   |-- Treatment/                      # Treatment and sub-classes
|   |   |-- Emergency.py                # Derived class Emergency from base class Treatment
|   |   |-- Pharmaceutical.py           # Derived class Pharmaceutical from base class Treatment
|   |   |-- Rehabilitative.py           # Derived class Rehabilitative from base class Treatment
|   |   |-- Treatment.py                # Base class Treatment
|   
|-- main.py                             # Program entry point 
|-- README.md                           # README file
```

## OOP Principles Used

- **Inheritance**: Staff and patients inherit from the `Person` class, while treatments and departments extend base classes.
- **Encapsulation**: Data is managed using private attributes and getter/setter methods.
- **Polymorphism**: Common methods behave differently depending on the object instance.
- **Modularity**: Classes are organized into separate files for clarity and scalability.

## Team Members and Roles

| Name                                         | Responsibility                                                               |
|----------------------------------------------|------------------------------------------------------------------------------|
| Ergasheva Mehribon Kutbiddin Kizi (12244992) | Department, EmergencyDepartment, GeneralPractice classes                     |
| Ni Vitaliy Viktorovich            (12244998) | Person, Patient classes                                                      |
| Kholmurodov Umarbek Elmurod Ugli  (12245023) | Treatment, Pharmaceutical, Rehabilitative, Emergency classes, GUI, Compilation |
| Tumenjargal Tserendemberel        (12245028) | Staff, Nurse, Doctor classes                                                 |
| Suzanne Lise Maud Blanche Tiare   (12250026) | Service, Billing, Registering classes   , Compilation                        |

## Requirements

- Python 3.11 or above  
- GUI library: *tkinter, PIL*  
- Database handling: *pandas, json, ast*

## How to Run

1. Clone the project:
   ```bash
   git clone https://github.com/Lilytiare/OOP_HOSPITAL.git
   cd OOP_HOSPITAL
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Notes

- This project is a simulation and not intended for real hospital use.
- Created as part of an academic assignment to demonstrate OOP proficiency in Python.

## License

This project is for academic purposes. All rights reserved to the authors.
