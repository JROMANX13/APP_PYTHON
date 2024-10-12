import os
import subprocess
import customtkinter as ctk

def open_menu():
    menu_window = ctk.CTk()  # Crea una nueva ventana
    menu_window.geometry('500x400')
    menu_window.title('Menú')
    
    # Función para cerrar la ventana actual y abrir otro archivo
    def open_file(file_name):
        menu_window.destroy()  # Cierra la ventana actual
        python_interpreter = os.path.join(os.environ['VIRTUAL_ENV'], 'Scripts', 'python.exe')
        subprocess.run([python_interpreter, file_name])  # Abre el archivo especificado

    # Etiqueta de bienvenida
    ctk.CTkLabel(menu_window, text="Bienvenido al Menú", font=('yu gothic ui', 25, "bold")).pack(pady=20)
 
    # Botón de Calculadora
    calculator_button = ctk.CTkButton(menu_window, text="Calculadora", command=lambda: open_file('calculadora.py'))
    calculator_button.pack(pady=10)

    # Botón de Formulario
    form_button = ctk.CTkButton(menu_window, text="Formulario", command=lambda: open_file('form.py'))
    form_button.pack(pady=10)

    # Botón de Serie Fibonacci
    fibonacci_button = ctk.CTkButton(menu_window, text="Serie Fibonacci", command=lambda: open_file('fibonacci.py'))
    fibonacci_button.pack(pady=10)

    menu_window.mainloop()

if __name__ == '__main__':
    open_menu()
