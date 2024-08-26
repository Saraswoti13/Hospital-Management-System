from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import tkinter as tk
from tkinter import ttk

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        

        username_label = ttk.Label(self, text="Username:")
        username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self, show="*")  
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        login_button = ttk.Button(self, text="Login", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "123":
            self.destroy() 
            MainApp()  
        else:
            tk.messagebox.showerror("Error", "Invalid username or password.")

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Management System")
    
        menu_options = [
            "1. Register/View/Update/Delete doctor",
            "2. View Patients/Discharge Patients",
            "3. View discharged patient",
            "4. Assign doctor to a patient",
            "5. Update admin details",
            "6. View all the patients from the from the same family",
            "7. Patient Records",
            "8. Get Management Report",
            "9. Relocate patients from one doctor to another",
            "10. Quit"
        ]
        for idx, option in enumerate(menu_options):
            button = ttk.Button(self, text=option, command=lambda opt=option: self.handle_menu(opt))
            button.grid(row=idx, column=0, padx=10, pady=5)

    def handle_menu(self, option):
        if option == "Register/View/Update/Delete doctor":
            self.doctor_operations()
       
    def doctor_operations(self):

        self.destroy()
        self.title('Doctors Management')
        
        doctor_management_options = [
            "Register Doctor",
            "View Doctors",
            "Update Doctor Detail",
            "Delete Doctor",
            "Go to Home"
        ]
        doctor_management_button_actions = [
            self.register_doctor_action,
            self.view_doctor_action,
            self.update_doctor_action,
            self.delete_doctor_action,
            self.home_window,
        ]

        self.text_label = tk.Label(self.window, text="-----Doctor Management-----")
        self.text_label.grid(row=0, column=0)

if __name__ == "__main__":
    LoginWindow().mainloop()