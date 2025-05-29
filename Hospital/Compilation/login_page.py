from tkinter import *
import json
from tkinter import messagebox

from main_page import main_page_compilation
BACKGROUND_IMAGE_PATH = 'images/img.png'
ICON_IMAGE_PATH = 'images/img_1.png'

def search_staff():
    role = role_input.get().lower()
    id = id_input.get()
    password = password_input.get()
    try:
        with open("Data Base/staff.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Not Found")
        return None
    else:
        if id in data:
            if password == data[id]["password"]:
                root.destroy()
                main_page_compilation(role,id)
        else:
            messagebox.showwarning(title=f"Warning", message="Staff not found")

root = Tk()
root.title("Hospital Management System")
root.geometry("740x416")
icon = PhotoImage(file=ICON_IMAGE_PATH)  # Must be .png or .gif
root.iconphoto(False, icon)


bg_image = PhotoImage(file=BACKGROUND_IMAGE_PATH)
Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)


Label(root, text="Name: ").place(x=400, y=200)
name_input = Entry(root, width=32)
name_input.place(x=451, y=200)
name_input.focus()

Label(root, text="ID: ").place(x=400, y=230)
id_input = Entry(root, width=32)
id_input.place(x=451, y=230)

Label(root, text="Password: ").place(x=400, y=260)
password_input = Entry(root, width=29)
password_input.place(x=470, y=260)

Label(root, text="Occupation: ").place(x=400, y=290)
role_input = Entry(root, width=27)
role_input.place(x=485, y=290)




Button(root, text="Login", command=search_staff, width=13).place(x=420, y=350)
root.mainloop()