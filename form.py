import customtkinter as ctk
import re
import tkinter.messagebox as messagebox

class RegistrationForm:
    def __init__(self, window):
        self.window = window
        self.setup_window()
        self.create_form()

    def setup_window(self):
        self.window.geometry('500x400')
        self.window.resizable(0, 0)
        self.window.title('Registration Form')

    def create_form(self):
        ctk.CTkLabel(self.window, text="Register", font=('yu gothic ui', 25, "bold")).pack(pady=20)

        # Name
        ctk.CTkLabel(self.window, text="Name", font=("yu gothic ui", 12)).pack(pady=5)
        self.name_entry = ctk.CTkEntry(self.window, width=300)
        self.name_entry.pack(pady=5)

        # Email
        ctk.CTkLabel(self.window, text="Email", font=("yu gothic ui", 12)).pack(pady=5)
        self.email_entry = ctk.CTkEntry(self.window, width=300)
        self.email_entry.pack(pady=5)

        # Phone
        ctk.CTkLabel(self.window, text="Phone", font=("yu gothic ui", 12)).pack(pady=5)
        self.phone_entry = ctk.CTkEntry(self.window, width=300)
        self.phone_entry.pack(pady=5)

        # Submit Button
        self.submit_button = ctk.CTkButton(self.window, text="Submit", command=self.validate_form)
        self.submit_button.pack(pady=20)

    def validate_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address.")
            return

        if not phone.isdigit() or len(phone) < 10:
            messagebox.showerror("Error", "Please enter a valid phone number.")
            return

        messagebox.showinfo("Success", "Registration successful!")

    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

def page():
    app = ctk.CTk()
    RegistrationForm(app)
    app.mainloop()

if __name__ == '__main__':
    page()
