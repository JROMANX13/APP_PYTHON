from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import tkinter.messagebox as messagebox
import os
import subprocess
import customtkinter as ctk


API_KEY = 'AIzaSyDvzg7kzTQ3CcA3ZWZgjPuUhx7MHJIdoOg'


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.setup_window()
        self.create_background()
        self.create_login_frame()

    def setup_window(self):
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

    def create_background(self):
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

    def create_login_frame(self):
        self.lgn_frame = Frame(self.window, bg='#040405',
                               width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # Welcome Label
        Label(self.lgn_frame, text="WELCOME", font=('yu gothic ui',
              25, "bold"), bg="#040405", fg='white').place(x=80, y=30)

        # Side Image
        self.add_image('images\\vector.png', (5, 100))
        self.add_image('images\\hyy.png', (620, 130),
                       label_text="Sign In", label_pos=(650, 240))

        # Username
        self.add_label("Correo", (550, 300))
        self.username_entry = self.add_entry(
            (580, 335), (550, 359), 'images\\username_icon.png')

        # Password
        self.add_label("Password", (550, 380))
        self.password_entry = self.add_entry(
            (580, 416), (550, 440), 'images\\password_icon.png', show="*")

        # Show/Hide Password Button
        self.show_image = ImageTk.PhotoImage(file='images\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='images\\hide.png')
        self.show_button = Button(self.lgn_frame, image=self.show_image,
                                  command=self.toggle_password, relief=FLAT, bg='white', borderwidth=0)
        self.show_button.place(x=860, y=420)

        # Login Button
        self.add_button('LOGIN', (550, 450), self.login_user)

        # Register Button
        self.signup_button_label = Button(
            self.lgn_frame,
            text='REGISTER',
            font=("yu gothic ui", 13, "bold"),
            command=self.register_user,
            bg='#3047ff',
            borderwidth=0,
            fg='white',
            cursor='hand2'
        )
        self.signup_button_label.place(x=550, y=500, width=250, height=35)

        # Forgot Password Button
        Button(self.lgn_frame, text="Forgot Password ?", font=("yu gothic ui", 13, "bold underline"),
               fg="white", relief=FLAT, borderwidth=0, background="#040405").place(x=630, y=555)

    def add_image(self, img_path, position, label_text=None, label_pos=None):
        img = Image.open(img_path)
        photo = ImageTk.PhotoImage(img)
        img_label = Label(self.lgn_frame, image=photo, bg='#040405')
        img_label.image = photo
        img_label.place(x=position[0], y=position[1])
        if label_text and label_pos:
            Label(self.lgn_frame, text=label_text, bg="#040405", fg="white", font=(
                "yu gothic ui", 17, "bold")).place(x=label_pos[0], y=label_pos[1])

    def add_label(self, text, position):
        Label(self.lgn_frame, text=text, bg="#040405", fg="#4f4e4d", font=(
            "yu gothic ui", 13, "bold")).place(x=position[0], y=position[1])

    def add_entry(self, entry_position, line_position, icon_path, show=None):
        entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69", font=(
            "yu gothic ui", 12, "bold"), insertbackground='#6b6a69', show=show)
        entry.place(x=entry_position[0], y=entry_position[1], width=270)
        Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1",
               highlightthickness=0).place(x=line_position[0], y=line_position[1])
        img = Image.open(icon_path)
        photo = ImageTk.PhotoImage(img)
        Label(self.lgn_frame, image=photo, bg='#040405').image = photo
        Label(self.lgn_frame, image=photo, bg='#040405').place(
            x=line_position[0], y=line_position[1]-26)
        return entry

    def add_button(self, text, position, command):
        button_frame = Label(self.lgn_frame, bg='#040405')
        button_frame.place(x=position[0], y=position[1])
        Button(button_frame, text=text, font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
               cursor='hand2', activebackground='#3047ff', fg='white', command=command).pack(padx=20, pady=10)

    def toggle_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
            self.show_button.config(image=self.hide_image)
        else:
            self.password_entry.config(show='*')
            self.show_button.config(image=self.show_image)

    def login_user(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={
            API_KEY}'

        data = {'email': email, 'password': password,
                'returnSecureToken': True}
        response = requests.post(url, data=json.dumps(data), headers={
                                 'Content-Type': 'application/json'})

        if response.status_code == 200:
            user_data = response.json()
            messagebox.showinfo("Login", f"Bienvenido {user_data['email']}")
            self.window.destroy()  # Cierra la ventana actual
            # Obtén la ruta del intérprete del entorno virtual
            python_interpreter = os.path.join(
                os.environ['VIRTUAL_ENV'], 'Scripts', 'python.exe')

            subprocess.run([python_interpreter, 'menu.py'])  # Abre el menú

        else:
            messagebox.showerror("Error", response.json().get(
                'error', {}).get('message', 'Error desconocido'))

    def register_user(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        url = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={
            API_KEY}'

        data = {'email': email, 'password': password,
                'returnSecureToken': True}
        response = requests.post(url, data=json.dumps(data), headers={
                                 'Content-Type': 'application/json'})

        if response.status_code == 200:
            messagebox.showinfo("Registro", "Usuario registrado con éxito")
        else:
            messagebox.showerror("Error", response.json().get(
                'error', {}).get('message', 'Error desconocido'))


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
