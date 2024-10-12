import customtkinter as ctk
import subprocess
import os

class FibonacciApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Serie de Fibonacci")
        self.master.geometry("400x300")
        self.master.configure(bg="black")

        # Botón Atrás
        self.back_button = ctk.CTkButton(master, text="Atrás", command=self.go_back, width=80, height=30)
        self.back_button.pack(pady=10)

        # Entrada para el número de elementos
        self.label = ctk.CTkLabel(master, text="Número de elementos:", fg_color="black", text_color="white")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(master, width=200)
        self.entry.pack(pady=10)

        # Botón para calcular la serie
        self.calculate_button = ctk.CTkButton(master, text="Calcular Fibonacci", command=self.calculate_fibonacci)
        self.calculate_button.pack(pady=20)

        # Área para mostrar la serie
        self.result_var = ctk.StringVar()
        self.result_label = ctk.CTkLabel(master, textvariable=self.result_var, fg_color="black", text_color="white")
        self.result_label.pack(pady=10)

    def calculate_fibonacci(self):
        try:
            n = int(self.entry.get())
            if n < 0:
                raise ValueError("El número debe ser positivo")
            fibonacci_series = self.fibonacci(n)
            self.result_var.set(f"Serie: {', '.join(map(str, fibonacci_series))}")
        except ValueError as e:
            self.result_var.set("Error: " + str(e))

    def fibonacci(self, n):
        series = []
        a, b = 0, 1
        for _ in range(n):
            series.append(a)
            a, b = b, a + b
        return series

    def go_back(self):
        self.master.destroy()  # Cierra la ventana actual
        subprocess.run([os.path.join(os.environ['VIRTUAL_ENV'], 'Scripts', 'python.exe'), 'menu.py'])  # Abre el menú

if __name__ == "__main__":
    app = ctk.CTk()
    FibonacciApp(app)
    app.mainloop()
