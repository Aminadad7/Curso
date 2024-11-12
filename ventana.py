import tkinter as tk

# Función que se ejecuta al hacer clic en el botón
def mostrar_texto():
    contenido = text_edit.get("1.0", tk.END)  # Obtiene el texto desde la línea 1, caracter 0, hasta el final
    print(contenido.strip())  # Muestra el texto en la consola (sin espacios en blanco al final)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Ventana")
ventana.geometry("600x400")

# Cuadro de texto
text_edit = tk.Text(ventana, height=10, width=40)
text_edit.pack(pady=10)

# Botón
boton = tk.Button(ventana, text="Saludar", command=mostrar_texto)
boton.pack(pady=10)

# Inicia el bucle principal de la ventana
ventana.mainloop()