

import tkinter as tk
from tkinter import messagebox

def construir_matriz(clave):
    clave = clave.upper().replace("J", "I")
    matriz = []
    usada = set()

    for letra in clave:
        if letra.isalpha() and letra not in usada:
            matriz.append(letra)
            usada.add(letra)

    for letra in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Sin la J
        if letra not in usada:
            matriz.append(letra)
            usada.add(letra)

    return [matriz[i:i+5] for i in range(0, 25, 5)]

def preparar_pares(texto):
    texto = texto.upper().replace("J", "I").replace(" ", "")
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = texto[i+1] if i+1 < len(texto) else "X"
        if a == b:
            b = "X"
            i += 1
        else:
            i += 2
        pares.append((a, b))
    return pares

def buscar_posicion(matriz, letra):
    for fila in range(5):
        for col in range(5):
            if matriz[fila][col] == letra:
                return fila, col
    return None, None

def cifrar_playfair(texto, clave):
    matriz = construir_matriz(clave)
    pares = preparar_pares(texto)
    resultado = ""

    for a, b in pares:
        fila_a, col_a = buscar_posicion(matriz, a)
        fila_b, col_b = buscar_posicion(matriz, b)

        if fila_a == fila_b:
            resultado += matriz[fila_a][(col_a + 1) % 5]
            resultado += matriz[fila_b][(col_b + 1) % 5]
        elif col_a == col_b:
            resultado += matriz[(fila_a + 1) % 5][col_a]
            resultado += matriz[(fila_b + 1) % 5][col_b]
        else:
            resultado += matriz[fila_a][col_b]
            resultado += matriz[fila_b][col_a]

    return resultado

def descifrar_playfair(texto, clave):
    matriz = construir_matriz(clave)
    pares = preparar_pares(texto)
    resultado = ""

    for a, b in pares:
        fila_a, col_a = buscar_posicion(matriz, a)
        fila_b, col_b = buscar_posicion(matriz, b)

        if fila_a == fila_b:
            resultado += matriz[fila_a][(col_a - 1) % 5]
            resultado += matriz[fila_b][(col_b - 1) % 5]
        elif col_a == col_b:
            resultado += matriz[(fila_a - 1) % 5][col_a]
            resultado += matriz[(fila_b - 1) % 5][col_b]
        else:
            resultado += matriz[fila_a][col_b]
            resultado += matriz[fila_b][col_a]

    return resultado

# Interfaz gráfica
class InterfazPlayfair:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado Playfair")
        self.root.geometry("400x420")

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

        cifrado = cifrar_playfair(mensaje, clave)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, cifrado)

    def descifrar(self):
        mensaje = self.entrada_mensaje.get()
        clave = self.entrada_clave.get()

        if not mensaje or not clave:
            messagebox.showerror("Error", "Debe ingresar mensaje y clave.")
            return

        descifrado = descifrar_playfair(mensaje, clave)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, descifrado)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazPlayfair(ventana)
    ventana.mainloop()
