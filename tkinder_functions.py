from tkinter import *
from tkinter import ttk
from menu_functions import *

activ_profil = None

def l_message(sucess):
    loading_message = Toplevel(root)
    message_var = StringVar()
    if sucess == True:
        loading_message.title("Profil erfolgreich geladen")
        loading_message.geometry("400x150+400+400")
        message_var.set(f"Profil {activ_profil.name} wurde erfolgreich geladen.")
    if sucess == False:
        loading_message.title("Profil konnte nicht geladen werden")
        loading_message.geometry("300x150+400+400")
        message_var.set("Profilname oder Passwort ist falsch!")
    message_label = ttk.Label(loading_message, textvariable=message_var, font=("Arial", 12)); message_label.grid(column=0, row=0, pady=20)
    message_button = ttk.Button(loading_message, text="Okay", command= loading_message.destroy); message_button.grid(column=0, row=1, pady=20)
    loading_message.mainloop()
    return

def l_profil(namevar, passwordvar):
    name = namevar.get()
    password = passwordvar.get()
    profil = load_profile(name)
    if profil != None:
        if password == profil.password:
            print("Loading profil was succesfull")
            global activ_profil
            activ_profil = profil
            profilname.set(f"{activ_profil.name}")
            l_message(True)
        else:
            l_message(False)

def open_load_profil():
    open_window = Toplevel(root)
    open_window.title("Lade Profil...")
    open_window.geometry("320x150+350+350")
    profil_name_label = ttk.Label(open_window, text="Profilname:")
    profil_name_label.grid(column=0, row=0, padx= 20, pady=(10,0))
    name_variable = StringVar()
    password_variable = StringVar()
    entry_profil_name = ttk.Entry(open_window, textvariable=name_variable)
    entry_profil_name.grid(column=0, row=1)
    password_label = ttk.Label(open_window, text="Passwort:"); password_label.grid(column=0, row=2)
    entry_password = ttk.Entry(open_window, show="*", textvariable=password_variable); entry_password.grid(column=0, row=3)
    load_button = ttk.Button(open_window, text="Laden", command=lambda:  open_window.destroy() & l_profil(name_variable, password_variable) ); load_button.grid(column=1, row=1, padx= 20, pady=(10,0), rowspan=1)
    cancel_button = ttk.Button(open_window, text="Abbrechen", command= open_window.destroy); cancel_button.grid(column=1, row=3, padx=20, pady=(0,10))
    open_window.mainloop()





root = Tk()
root.title("Rangierplaner")
root.geometry("800x400+300+300")
root.option_add("*tearoff", False)
menubar = Menu(root)
root["menu"] = menubar
menu_profil = Menu(menubar)
menubar.add_cascade(menu=menu_profil, label="Profile")
menu_profil.add_command(label="Lade Profil...", command=open_load_profil)

profilname = StringVar()
profilname.set("Kein Profil geladen")
profilname_label = ttk.Label(root, text="Kein Profil geladen", textvariable=profilname); profilname_label.grid(column=9,row=0, sticky="NE")
root.mainloop() # zum starten des widgets