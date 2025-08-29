from tkinter import *

def contador_palabras():
    '''Cuenta las palabras en el campo de texto y actualiza el resultado'''
    texto = campo_texto.get("1.0", "end-1c")
    palabras = len(texto.split())
    caracteres = len(texto)
    caracteres_sin_espacio = len("".join(texto.split()))

    resultado.config(text=f"Palabras: {palabras}\nCaracteres: {caracteres}\nCaracteres sin espacios: {caracteres_sin_espacio}")
    
    
    ventana.after(500, contador_palabras)

ventana = Tk()
ventana.title("Contador de palabras dinámico")

campo_texto = Text(ventana, width=40, height=10)
campo_texto.pack(pady=10)

resultado = Label(ventana, text="")
resultado.pack()


contador_palabras()

ventana.mainloop()
