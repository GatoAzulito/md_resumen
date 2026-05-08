import tkinter as tk


def incrementar():
    global contador
    contador += 1
    etiqueta_contador.config(text=f"Clics: {contador}")


def reiniciar():
    global contador
    contador = 0
    etiqueta_contador.config(text="Clics: 0")


contador = 0

ventana = tk.Tk()
ventana.title("Contador de clics")
ventana.geometry("300x180")
ventana.resizable(False, False)

etiqueta_titulo = tk.Label(ventana, text="Contador de clics", font=("Segoe UI", 14, "bold"))
etiqueta_titulo.pack(pady=(15, 8))

etiqueta_contador = tk.Label(ventana, text="Clics: 0", font=("Segoe UI", 12))
etiqueta_contador.pack(pady=6)

boton_sumar = tk.Button(ventana, text="Haz clic", width=16, command=incrementar)
boton_sumar.pack(pady=6)

boton_reiniciar = tk.Button(ventana, text="Reiniciar", width=16, command=reiniciar)
boton_reiniciar.pack(pady=4)

ventana.mainloop()
