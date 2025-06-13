import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import os

class MenuInterface:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Menú Principal")
        self.root.geometry("450x650")
        self.root.configure(bg="#f0f0f0")
        
        # Centrar la ventana en la pantalla
        self.center_window()
        
        # Crear el contenido de la interfaz
        self.create_widgets()
        
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal para centrar el contenido
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Título
        title_label = tk.Label(
            main_frame,
            text="MENÚ PRINCIPAL",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 20))

        # Subtítulo
        subtitle_label = tk.Label(
            main_frame,
            text="Cifrados disponibles",
            font=("Arial", 12, "italic"),
            bg="#f0f0f0",
            fg="#555555"
        )
        subtitle_label.pack(pady=(0, 10))

        # Frame para los botones de cifrado
        cipher_frame = tk.Frame(main_frame, bg="#f0f0f0")
        cipher_frame.pack(expand=True)

        button_style = {
            "font": ("Arial", 12),
            "width": 20,
            "height": 2,
            "bg": "#4CAF50",
            "fg": "white",
            "relief": "raised",
            "bd": 2,
            "cursor": "hand2"
        }

        # Botones de cifrado
        btn_hill = tk.Button(cipher_frame, text="Hill", command=self.BTN_Hill, **button_style)
        btn_hill.pack(pady=5)
        btn_vigenere = tk.Button(cipher_frame, text="Vigenère", command=self.Vigenere, **button_style)
        btn_vigenere.pack(pady=5)
        btn_hermetico = tk.Button(cipher_frame, text="Hermetico", command=self.Hermetico, **button_style)
        btn_hermetico.pack(pady=5)
        btn_beyc = tk.Button(cipher_frame, text="BEYC", command=self.BEYC, **button_style)
        btn_beyc.pack(pady=5)
        btn_playfair = tk.Button(cipher_frame, text="Playfair", command=self.Playfair, **button_style)
        btn_playfair.pack(pady=5)
        btn_polybios = tk.Button(cipher_frame, text="Polybios", command=self.Polybios, **button_style)
        btn_polybios.pack(pady=5)
        btn_vernam = tk.Button(cipher_frame, text="Vernam", command=self.Vernam, **button_style)
        btn_vernam.pack(pady=5)

        # Separador visual
        separator = tk.Frame(main_frame, height=2, bg="#cccccc")
        separator.pack(fill="x", pady=15)

        # Frame para botones de ayuda y salida
        bottom_frame = tk.Frame(main_frame, bg="#f0f0f0")
        bottom_frame.pack()

        btn_help = tk.Button(
            bottom_frame,
            text="❓ Ayuda",
            command=self.ayuda,
            **button_style
        )
        btn_help.pack(pady=5)

        exit_button = tk.Button(
            bottom_frame,
            text="🚪 Salir",
            command=self.salir,
            font=("Arial", 12, "bold"),
            width=20,
            height=2,
            bg="#f44336",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        exit_button.pack(pady=5)

        # Información en la parte inferior
        info_label = tk.Label(
            main_frame,
            text="Selecciona una opción del menú",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666666"
        )
        info_label.pack(side="bottom", pady=(15, 0))
        
    def BTN_Hill(self):
     ruta = r"./Programas/Hill.py"
     subprocess.Popen(["python", ruta], shell=True)
        
    def Vigenere(self):
        ruta = r"./Programas/Vigenere.py"
        subprocess.Popen(["python", ruta], shell=True)
        
    def Hermetico(self):
        ruta = r"./Programas/Hermético.py"
        subprocess.Popen(["python", ruta], shell=True)
        
    def BEYC(self):
        ruta= r"./Programas/BEYC.py"
        subprocess.Popen(["python", ruta], shell=True)

    def Playfair(self):
        ruta = r"./Programas/Playfair.py"
        subprocess.Popen(["python", ruta], shell=True)

    def Polybios(self):
        ruta = r"./Programas/Polybios.py"
        subprocess.Popen(["python", ruta], shell=True)

    def Vernam(self):
        ruta = r"./Programas/VERNAM.py"
        subprocess.Popen(["python", ruta], shell=True)

    def ayuda(self):
        """Muestra una ventana de ayuda"""
        messagebox.showinfo(
            "Ayuda",
            "Selecciona un cifrado para abrir su interfaz.\n\n"
            "Usa el botón 'Salir' para cerrar la aplicación."
        )

    def salir(self):
        """Función para salir de la aplicación"""
        respuesta = messagebox.askyesno(
            "Confirmar Salida", 
            "¿Estás seguro de que deseas salir?"
        )
        if respuesta:
            print("Cerrando aplicación...")
            self.root.quit()
            
    def run(self):
        """Ejecutar la aplicación"""
        print("Iniciando interfaz de menú...")
        self.root.mainloop()

    

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = MenuInterface()
    app.run()
