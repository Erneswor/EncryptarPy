
import tkinter as tk
from tkinter import messagebox
import random
import string

# Función para generar una clave aleatoria del mismo tamaño que el mensaje
def generar_clave(mensaje):
    caracteres = string.ascii_uppercase + string.whitespace
    clave = ''.join(random.choice(caracteres) for _ in mensaje)
    return clave

# Cifrado usando XOR entre caracteres
def cifrar_hermetico(mensaje, clave):
    mensaje = mensaje.upper()
    clave = clave.upper()
    cifrado = ""

    for m, k in zip(mensaje, clave):
        if m not in string.printable or k not in string.printable:
            cifrado += m  # Mantiene caracteres no estándar sin cifrar
        else:
            # Operación XOR con la posición ASCII (limitada a 0-255)
            valor = ord(m) ^ ord(k)
            cifrado += chr(valor)

    return cifrado

# Descifrado usando la misma clave y operación XOR
def descifrar_hermetico(cifrado, clave):
    descifrado = ""

    for c, k in zip(cifrado, clave):
        if k not in string.printable:
            descifrado += c
        else:
            valor = ord(c) ^ ord(k)
            descifrado += chr(valor)

    return descifrado

# Interfaz gráfica
class InterfazHermetico:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado Hermético")
        self.root.geometry("500x500")

        tk.Label(root, text="Mensaje:").pack()
        self.entrada_mensaje = tk.Entry(root, width=60)
        self.entrada_mensaje.pack()

        tk.Button(root, text="Generar Clave", command=self.generar_clave).pack(pady=5)

        tk.Label(root, text="Clave:").pack()
        self.entrada_clave = tk.Entry(root, width=60)
        self.entrada_clave.pack()

        tk.Button(root, text="Cifrar", command=self.cifrar).pack(pady=10)
        tk.Button(root, text="Descifrar", command=self.descifrar).pack()

        tk.Label(root, text="Resultado:").pack()
        self.resultado = tk.Text(root, height=6, width=60)
        self.resultado.pack(pady=10)

        tk.Button(root, text="Salir", command=self.root.quit).pack(pady=10)

    def generar_clave(self):
        mensaje = self.entrada_mensaje.get()
        if not mensaje:
            messagebox.showwarning("Advertencia", "Ingrese primero el mensaje para generar clave.")
            return
        clave = generar_clave(mensaje)
        self.entrada_clave.delete(0, tk.END)
        self.entrada_clave.insert(tk.END, clave)

    def cifrar(self):
        mensaje = self.entrada_mensaje.get()
        clave = self.entrada_clave.get()

        if not mensaje or not clave:
            messagebox.showerror("Error", "Debe ingresar mensaje y clave.")
            return

        if len(clave) != len(mensaje):
            messagebox.showerror("Error", "La clave debe tener la misma longitud que el mensaje.")
            return

        cifrado = cifrar_hermetico(mensaje, clave)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, cifrado)

    def descifrar(self):
        cifrado = self.entrada_mensaje.get()
        clave = self.entrada_clave.get()

        if not cifrado or not clave:
            messagebox.showerror("Error", "Debe ingresar mensaje cifrado y clave.")
            return

        if len(clave) != len(cifrado):
            messagebox.showerror("Error", "La clave debe tener la misma longitud que el mensaje cifrado.")
            return

        descifrado = descifrar_hermetico(cifrado, clave)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, descifrado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazHermetico(ventana)
    ventana.mainloop()
