
import tkinter as tk
from tkinter import messagebox

cuadro_polybios = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
    'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
    'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
    'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
    'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
}

cuadro_inverso = {v: k for k, v in cuadro_polybios.items()}

class InterfazPolybios:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Cifrado Polybios - Seguridad Informatica")
        self.root.geometry("500x550")
        self.root.config(bg="#2c3e50")
        self.root.resizable(False, False)
        
        
        self.root.update_idletasks()
        width = 500
        height = 550
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        title_label = tk.Label(
            main_frame,
            text="🔐 CIFRADO POLYBIOS",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=(0, 10))

        
        subtitle_label = tk.Label(
            main_frame,
            text="Seguridad en Informática",
            font=("Arial", 10, "italic"),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        subtitle_label.pack(pady=(0, 30))

       
        input_frame = tk.Frame(main_frame, bg="#34495e", relief="raised", bd=2)
        input_frame.pack(fill="x", pady=(0, 20))

        tk.Label(
            input_frame,
            text="📝 MENSAJE:",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        ).pack(pady=(10, 5))

        self.entrada = tk.Entry(
            input_frame,
            width=50,
            font=("Consolas", 11),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief="sunken",
            bd=2,
            justify="center"
        )
        self.entrada.pack(pady=(0, 15), padx=20)

        
        output_frame = tk.Frame(main_frame, bg="#34495e", relief="raised", bd=2)
        output_frame.pack(fill="x", pady=(0, 30))

        tk.Label(
            output_frame,
            text="🔢 RESULTADO:",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        ).pack(pady=(10, 5))

        self.salida = tk.Entry(
            output_frame,
            width=50,
            font=("Consolas", 11),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief="sunken",
            bd=2,
            justify="center",
            state="readonly"
        )
        self.salida.pack(pady=(0, 15), padx=20)

        
        button_frame = tk.Frame(main_frame, bg="#2c3e50")
        button_frame.pack(pady=20)

       
        btn_cifrar = tk.Button(
            button_frame,
            text="🔒 CIFRAR",
            command=self.cifrar,
            font=("Arial", 12, "bold"),
            width=12,
            height=2,
            bg="#27ae60",
            fg="white",
            activebackground="#2ecc71",
            activeforeground="white",
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        btn_cifrar.pack(side="left", padx=10)

        
        btn_descifrar = tk.Button(
            button_frame,
            text="🔓 DESCIFRAR",
            command=self.descifrar,
            font=("Arial", 12, "bold"),
            width=12,
            height=2,
            bg="#3498db",
            fg="white",
            activebackground="#5dade2",
            activeforeground="white",
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        btn_descifrar.pack(side="left", padx=10)

       
        btn_limpiar = tk.Button(
            button_frame,
            text="🧹 LIMPIAR",
            command=self.limpiar,
            font=("Arial", 12, "bold"),
            width=12,
            height=2,
            bg="#f39c12",
            fg="white",
            activebackground="#f4d03f",
            activeforeground="white",
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        btn_limpiar.pack(side="left", padx=10)

       
        separator = tk.Frame(main_frame, height=2, bg="#7f8c8d")
        separator.pack(fill="x", pady=20)

       
        secondary_frame = tk.Frame(main_frame, bg="#2c3e50")
        secondary_frame.pack(pady=10)

       
        btn_salir = tk.Button(
            main_frame,
            text="🚪 SALIR",
            command=self.salir,
            font=("Arial", 12, "bold"),
            width=15,
            height=2,
            bg="#e74c3c",
            fg="white",
            activebackground="#ec7063",
            activeforeground="white",
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        btn_salir.pack(pady=20)


    def cifrar(self):
        mensaje = self.entrada.get().replace("j", "i").replace("J", "I")
        if not mensaje.strip():
            messagebox.showwarning("Advertencia", "Por favor, ingresa un mensaje para cifrar")
            return

        cifrado = ""
        for letra in mensaje:
            if letra == " ":
                cifrado += " "
            else:
                letra_mayus = letra.upper()
                if letra_mayus in cuadro_polybios:
                    cifrado += cuadro_polybios[letra_mayus]
                else:
                    cifrado += "??"

        self.salida.config(state="normal")
        self.salida.delete(0, tk.END)
        self.salida.insert(0, cifrado)
        self.salida.config(state="readonly")

    def descifrar(self):
        texto = self.entrada.get()
        if not texto.strip():
            messagebox.showwarning("Advertencia", "Por favor, ingresa un mensaje para descifrar")
            return

        descifrado = ""
        i = 0
        while i < len(texto):
            if texto[i] == " ":
                descifrado += "?"
                i += 1
            else:
                par = texto[i:i+2]
                letra = cuadro_inverso.get(par, '?')
                descifrado += letra
                i += 2

        self.salida.config(state="normal")
        self.salida.delete(0, tk.END)
        self.salida.insert(0, descifrado)
        self.salida.config(state="readonly")

    def limpiar(self):
       
        self.entrada.delete(0, tk.END)
        self.salida.config(state="normal")
        self.salida.delete(0, tk.END)
        self.salida.config(state="readonly")

    def salir(self):
        respuesta = messagebox.askyesno(
            "Confirmar Salida", 
            "¿Estás seguro de que deseas salir?"
        )
        if respuesta:
            self.root.quit()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazPolybios(ventana)
    ventana.mainloop()
