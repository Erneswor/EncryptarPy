
import tkinter as tk
from tkinter import messagebox
import numpy as np

class CifradoHillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado Hill - Encriptador")
        self.root.geometry("400x400")

        # Mensaje de entrada
        tk.Label(root, text="Mensaje:").pack()
        self.entrada_mensaje = tk.Entry(root, width=40)
        self.entrada_mensaje.pack()

        # Botones
        tk.Button(root, text="Encriptar", command=self.encriptar).pack(pady=10)
        tk.Button(root, text="Desencriptar", command=self.desencriptar).pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

        # Resultados
        self.etiqueta_llave = tk.Label(root, text="Llave (matriz):")
        self.etiqueta_llave.pack()
        self.etiqueta_cifrado = tk.Label(root, text="Mensaje encriptado:")
        self.etiqueta_cifrado.pack()
        self.etiqueta_desencriptado = tk.Label(root, text="Mensaje desencriptado:")
        self.etiqueta_desencriptado.pack()

        # Definir una llave válida para matriz 2x2 (debe ser invertible módulo 26)
        self.llave = np.array([[3, 3], [2, 5]])
        self.mensaje_cifrado = ""

    def texto_a_numeros(self, texto):
        return [ord(c) - ord('A') for c in texto.upper().replace(" ", "")]

    def numeros_a_texto(self, numeros):
        return ''.join([chr((n % 26) + ord('A')) for n in numeros])

    def encriptar(self):
        mensaje = self.entrada_mensaje.get().replace(" ", "").upper()

        if len(mensaje) % 2 != 0:
            mensaje += 'X'  # Rellenar si es impar

        texto_num = self.texto_a_numeros(mensaje)
        resultado = []

        for i in range(0, len(texto_num), 2):
            bloque = np.array([[texto_num[i]], [texto_num[i+1]]])
            cifrado = np.dot(self.llave, bloque) % 26
            resultado.extend(cifrado.flatten())

        self.mensaje_cifrado = self.numeros_a_texto(resultado)
        self.etiqueta_llave.config(text=f"Llave: {self.llave.tolist()}")
        self.etiqueta_cifrado.config(text=f"Mensaje encriptado: {self.mensaje_cifrado}")
        self.etiqueta_desencriptado.config(text="")

    def modinv(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise Exception('No hay inverso modular')

    def desencriptar(self):
        if not self.mensaje_cifrado:
            messagebox.showwarning("Advertencia", "Primero encripta un mensaje.")
            return

        det = int(np.round(np.linalg.det(self.llave))) % 26
        det_inv = self.modinv(det, 26)

        # Matriz adjunta (inversa multiplicada por determinante)
        adj = np.array([[self.llave[1][1], -self.llave[0][1]],
                        [-self.llave[1][0], self.llave[0][0]]]) % 26

        inversa = (det_inv * adj) % 26
        texto_num = self.texto_a_numeros(self.mensaje_cifrado)
        resultado = []

        for i in range(0, len(texto_num), 2):
            bloque = np.array([[texto_num[i]], [texto_num[i+1]]])
            descifrado = np.dot(inversa, bloque) % 26
            resultado.extend(descifrado.flatten())

        mensaje_original = self.numeros_a_texto(resultado)
        self.etiqueta_desencriptado.config(text=f"Mensaje desencriptado: {mensaje_original}")

# Ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = CifradoHillApp(ventana)
    ventana.mainloop()
