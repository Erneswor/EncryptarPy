import tkinter as tk

class InterfazVernam:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado Vernam")
        self.root.geometry("400x400")
        self.root.config(bg="lightblue")

        tk.Label(root, text="Mensaje:", bg="lightblue").pack(pady=5)
        self.entrada = tk.Entry(root, width=50)
        self.entrada.pack(pady=5)

        tk.Label(root, text="Clave (igual longitud):", bg="lightblue").pack(pady=5)
        self.clave_entry = tk.Entry(root, width=50)
        self.clave_entry.pack(pady=5)

        tk.Label(root, text="Resultado:", bg="lightblue").pack(pady=5)
        self.salida = tk.Entry(root, width=50)
        self.salida.pack(pady=5)

        tk.Button(root, text="Cifrar", command=self.vernam).pack(pady=10)
        tk.Button(root, text="Descifrar", command=self.vernam).pack(pady=10)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

    def vernam(self):
        mensaje = self.entrada.get()
        clave = self.clave_entry.get()

        if len(mensaje) != len(clave):
            self.salida.delete(0, tk.END)
            self.salida.insert(0, "Error: Clave debe tener misma longitud")
            return

        resultado = ""
        for i in range(len(mensaje)):
            letra = chr(ord(mensaje[i]) ^ ord(clave[i]))
            resultado += letra

        self.salida.delete(0, tk.END)
        self.salida.insert(0, resultado)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazVernam(ventana)
    ventana.mainloop()
