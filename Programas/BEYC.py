
import tkinter as tk

class InterfazBEYC:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado BEYC")
        self.root.geometry("400x400")
        self.root.config(bg="lightyellow")

        tk.Label(root, text="Mensaje:", bg="lightyellow").pack(pady=5)
        self.entrada = tk.Entry(root, width=50)
        self.entrada.pack(pady=5)

        tk.Label(root, text="Clave:", bg="lightyellow").pack(pady=5)
        self.clave_entry = tk.Entry(root, width=50)
        self.clave_entry.pack(pady=5)

        tk.Label(root, text="Resultado:", bg="lightyellow").pack(pady=5)
        self.salida = tk.Entry(root, width=50)
        self.salida.pack(pady=5)

        tk.Button(root, text="Cifrar", command=self.cifrar).pack(pady=10)
        tk.Button(root, text="Descifrar", command=self.descifrar).pack(pady=10)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

    def cifrar(self):
        mensaje = self.entrada.get()
        clave = self.clave_entry.get()
        resultado = ""
        for i in range(len(mensaje)):
            char = chr(ord(mensaje[i]) ^ ord(clave[i % len(clave)]))
            resultado += char
        self.salida.delete(0, tk.END)
        self.salida.insert(0, resultado)

    def descifrar(self):
        self.cifrar()  # BEYC usa XOR, el descifrado es igual que el cifrado


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazBEYC(ventana)
    ventana.mainloop()
