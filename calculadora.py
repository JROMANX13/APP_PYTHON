import customtkinter as ctk
import subprocess
import os

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("400x600")
        self.master.configure(bg="black")

        self.result_var = ctk.StringVar()

        # Botón Atrás
        self.back_button = ctk.CTkButton(master, text="Atrás", command=self.go_back, width=80, height=30)
        self.back_button.pack(pady=10)

        # Pantalla de resultados
        self.result_entry = ctk.CTkEntry(master, textvariable=self.result_var, width=300, height=50, font=("Arial", 24), bg_color="black", text_color="white")
        self.result_entry.pack(pady=20)

        # Contenedor para los botones
        self.button_frame = ctk.CTkFrame(master)
        self.button_frame.pack(expand=True, fill='both')

        # Crear botones
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1), ('8', 1), ('9', 1), ('/', 1),
            ('4', 2), ('5', 2), ('6', 2), ('*', 2),
            ('1', 3), ('2', 3), ('3', 3), ('-', 3),
            ('0', 4), ('C', 4), ('=', 4), ('+', 4),
        ]

        for (text, row) in buttons:
            button = ctk.CTkButton(self.button_frame, text=text, command=lambda t=text: self.on_button_click(t), width=5, height=2)  
            button.grid(row=row, column=buttons.index((text, row)) % 4, padx=10, pady=10, sticky="nsew")

        
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):  
            self.button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")  # Borrar entrada
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)  # Evaluar la expresión
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")  
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)  

    def go_back(self):
        self.master.destroy()  # Cierra la ventana actual
        subprocess.run([os.path.join(os.environ['VIRTUAL_ENV'], 'Scripts', 'python.exe'), 'menu.py'])  # Abre el menú

if __name__ == "__main__":
    app = ctk.CTk()
    CalculatorApp(app)
    app.mainloop()
