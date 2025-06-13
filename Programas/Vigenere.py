
import tkinter as tk
from tkinter import messagebox

def cifrar_vigenere(texto, clave):
    texto = texto.upper().replace(" ", "")
    clave = clave.upper()
    resultado = ""
    clave_expandida = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]

    for i in range(len(texto)):
        if texto[i].isalpha():
            letra = chr((ord(texto[i]) + ord(clave_expandida[i]) - 2 * ord('A')) % 26 + ord('A'))
            resultado += letra
        else:
            resultado += texto[i]

    return resultado

def descifrar_vigenere(texto, clave):
    texto = texto.upper().replace(" ", "")
    clave = clave.upper()
    resultado = ""
    clave_expandida = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]

    for i in range(len(texto)):
        if texto[i].isalpha():
            letra = chr((ord(texto[i]) - ord(clave_expandida[i]) + 26) % 26 + ord('A'))
            resultado += letra
        else:
            resultado += texto[i]

    return resultado

# Interfaz gráfica
class InterfazVigenere:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado Vigenère")
        self.root.geometry("400x400")

        # Widgets
        tk.Label(root, text="Mensaje:").pack()
        self.entrada_mensaje = tk.Entry(root, width=50)
        self.entrada_mensaje.pack()

        tk.Label(root, text="Clave:").pack()
        self.entrada_clave = tk.Entry(root, width=50)
        self.entrada_clave.pack()

        tk.Button(root, text="Cifrar", command=self.cifrar).pack(pady=10)
        tk.Button(root, text="Descifrar", command=self.descifrar).pack()

        tk.Label(root, text="Resultado:").pack()
        self.resultado = tk.Text(root, height=5, width=50)
        self.resultado.pack(pady=10)

        tk.Button(root, text="Salir", command=self.root.quit).pack(pady=10)

    def cifrar(self):
        mensaje = self.entrada_mensaje.get()
        clave = self.entrada_clave.get()

        if not mensaje or not clave:
            messagebox.showerror("Error", "Debe ingresar mensaje y clave.")
            return

        cifrado = cifrar_vigenere(mensaje, clave)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, cifrado)

    def descifrar(self):
        mensaje = self.entrada_mensaje.get()
        clave = self.entrada_clave.get()

        if not mensaje or not clave:
            messagebox.showerror("Error", "Debe ingresar mensaje y clave.")
            return

        descifrado = descifrar_vigenere(mensaje, clave)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, descifrado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazVigenere(ventana)
    ventana.mainloop()
