import customtkinter as ctk
import re
import tkinter.messagebox as messagebox
import os
import subprocess
import menu  # Asegúrate de que este módulo esté accesible

class RegistrationForm:
    def __init__(self, window):
        self.window = window
        self.setup_window()
        self.create_buttons()  # Crear botones "Atrás" y "Enviar"
        self.create_form()

    def setup_window(self):
        self.window.geometry('500x400')
        self.window.resizable(0, 0)
        self.window.title('Formulario')
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.window.configure(bg="black")  # Fondo negro

    def create_buttons(self):
        button_frame = ctk.CTkFrame(self.window, bg_color="black")  # Marco para botones
        button_frame.pack(side='top', fill='x')  # Llenar en la dirección horizontal

        # Botón Atrás
        back_button = ctk.CTkButton(button_frame, text="Atrás", command=self.go_back, width=80, height=30)
        back_button.pack(side='left', padx=10, pady=10)  # Alineado a la izquierda

        # Botón Enviar
        self.submit_button = ctk.CTkButton(button_frame, text="Enviar", command=self.validate_form, width=80, height=30)
        self.submit_button.pack(side='right', padx=10, pady=10)  # Alineado a la derecha

    def go_back(self):
        self.window.destroy()  # Cerrar la ventana actual
        subprocess.run([os.path.join(os.environ['VIRTUAL_ENV'], 'Scripts', 'python.exe'), 'menu.py'])  # Abre el menú

    def create_form(self):
        form_frame = ctk.CTkFrame(self.window, fg_color="black")  # Fondo negro para el marco
        form_frame.pack(pady=20, padx=20, fill='both', expand=True)

        ctk.CTkLabel(form_frame, text="Formulario", font=('yu gothic ui', 25, "bold"), text_color="white").pack(pady=(10, 20))

        # Nombre
        ctk.CTkLabel(form_frame, text="Nombre", font=("yu gothic ui", 12), text_color="white").pack(pady=5)
        self.name_entry = ctk.CTkEntry(form_frame, width=300)
        self.name_entry.pack(pady=5)

        # Email
        ctk.CTkLabel(form_frame, text="Email", font=("yu gothic ui", 12), text_color="white").pack(pady=5)
        self.email_entry = ctk.CTkEntry(form_frame, width=300)
        self.email_entry.pack(pady=5)

        # Teléfono
        ctk.CTkLabel(form_frame, text="Teléfono", font=("yu gothic ui", 12), text_color="white").pack(pady=5)
        self.phone_entry = ctk.CTkEntry(form_frame, width=300, validate='key', 
                                          validatecommand=(self.window.register(self.validate_phone), '%S'))
        self.phone_entry.pack(pady=5)

    def validate_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Por favor, ingrese su nombre.")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Por favor, ingrese una dirección de correo válida.")
            return

        if not phone.isdigit() or len(phone) < 10:
            messagebox.showerror("Error", "Por favor, ingrese un número de teléfono válido.")
            return

        messagebox.showinfo("Éxito", "¡Registro exitoso!")
        self.clear_fields()  # Limpiar campos después de validación exitosa

    def clear_fields(self):
        self.name_entry.delete(0, ctk.END)
        self.email_entry.delete(0, ctk.END)
        self.phone_entry.delete(0, ctk.END)

    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def validate_phone(self, new_value):
        # Permitir solo dígitos
        return new_value.isdigit() or new_value == ""

def page():
    app = ctk.CTk()
    RegistrationForm(app)
    app.mainloop()

if __name__ == '__main__':
    page()
