import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import pyperclip

#Crear ventana
ventana=tk.Tk()
ventana.title("Creador de contraseñas")
ventana.config(width=700,height=300)

# Digitos permitidos
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
          "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"]
letras_y_especiales = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                       "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                       "W", "X", "Y", "Z", "!", "\\", "#", "$", "%", "&", "'", "(", ")", "*",
                       "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
                       "[", "]", "^", "_", "`", "{", "|", "}", "~", " "]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7",
           "8", "9"]

#Funciones
def password_generator():
        #Obtener los valores
        digitosa=digitos_entry.get()
        cant_numerosa = cant_numeros_entry.get()
        caracteres_especialesa = caracteres_especiales_entry.get()

        #Pasar si los datos ingresados son numeros
        if digitosa.isdigit() and cant_numerosa.isdigit() :
                #convertir a enteros
                digitos=int(digitosa)
                cant_numeros=int(cant_numerosa)
                caracteres_especiales=str(caracteres_especialesa)

                #Crear la lista para la contraseña
                password = [None] * digitos

                #Comprobar si la cantidad de numeros que se quiere es menor a la cantidad de digitos de la contraseña
                if cant_numeros <= digitos:

                        #Recorrer aleatoriamente las posiciones de la lista y comprobar que esten vacias y asi asignarles un valor
                        for _ in range(cant_numeros):
                                pasa = False
                                while not pasa:
                                        indice = random.randrange(0, digitos)
                                        if password[indice] is None:
                                                password[indice] = random.choice(numeros)
                                                pasa = True

                #Mensaje de error si se insertaron mas numeros que digitos posibles
                else:
                        messagebox.showinfo("Error","La cantidad de numeros que escribio es mayor a la "
                                            "cantidad de digitos que escribio")

                #comprobar  si la cantidad de numeros es estrictamente menor para saber si es contraseña de solo numeros
                if cant_numeros < digitos:

                        #Comprobar el formato de lo que se escribio y asignarle un valor a las posiciones vacias
                        if caracteres_especiales == "Si" or caracteres_especiales == "SI" or caracteres_especiales == "si":
                                for i in range(digitos):
                                        if password[i] is None:
                                                password[i] = random.choice(letras_y_especiales)

                        elif caracteres_especiales == "No" or caracteres_especiales == "NO" or caracteres_especiales == "no":
                                for i in range(digitos):
                                        if password[i] is None:
                                                password[i] = random.choice(letras)
                        else:
                                messagebox.showinfo("Error", "No escribio si o no en un formato valido")
                #Juntar la lista
                final = "".join(password)
                #Mostrar la lista
                finallabel=tk.Label(text=f"La contraseña generada es: {final}")
                finallabel.place(x=20,y=200)
                #Boton para copiar
                copy = ttk.Button(text="Copiar", command=lambda:copy_text(final))
                copy.place(x=20,y=230)

        #Mostrar error si no se digita formato valido
        else:
                messagebox.showinfo("No numero","No digito un numero, intente de nuevo")


#Funcion para copiar el texto
def copy_text(final):
        texto=final
        pyperclip.copy(texto)
        messagebox.showinfo("Copiado","Su contraseña ha sido copiada en el portapapeles")

#Textos y entradas
digitoslabel = ttk.Label(text="Digite la cantidad de digitos que quiere en su contraseña: ")
digitoslabel.place(x=20, y=20)
digitos_entry = ttk.Entry()
digitos_entry.place(x=350,y=20,width=80)

cant_numeroslabel = ttk.Label(text="Digite la cantidad de numeros que desea: ")
cant_numeroslabel.place(x=20, y=60)
cant_numeros_entry = ttk.Entry()
cant_numeros_entry.place(x=250, y=60,width=80)

caracteres_especialeslabel=ttk.Label(text="¿Desea incluir caracteres especiales en la contraseña? Si/No ")
caracteres_especialeslabel.place(x=20,y=100)
caracteres_especiales_entry=ttk.Entry()
caracteres_especiales_entry.place(x=300,y=100,width=80)

#Boton
boton = ttk.Button(text="Crear contraseña", command=password_generator)
boton.place(x=20, y=150)


ventana.mainloop()