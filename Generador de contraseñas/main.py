import random

def password_generator(digitos,cant_numeros):
        # Digitos permitidos
        letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
             "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z"]
        letras_y_especiales=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
             "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z", "!", "\\", "#", "$", "%", "&", "'", "(", ")", "*",
             "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
             "[", "]", "^", "_", "`", "{", "|", "}", "~", " "]
        numeros = ["0", "1", "2", "3", "4", "5", "6", "7",
             "8", "9"]
        password=[None]*digitos

        if cant_numeros<=digitos:
            for _ in range(cant_numeros):
                pasa =False
                while not pasa:
                    indice = random.randrange(0, digitos)
                    if password[indice] is None:
                        password[indice] = random.choice(numeros)
                        pasa = True

        else:
            return "La cantidad de numeros que escribio es mayor a la cantidad de digitos que escribio"

        if cant_numeros<digitos:
            caracteres_especiales = input("¿Desea incluir caracteres especiales en la contraseña? Si/No ")


            if caracteres_especiales=="Si" or caracteres_especiales=="SI" or caracteres_especiales=="si":
                for i in range(digitos):
                    if password[i] is  None:
                        password[i]=random.choice(letras_y_especiales)

            elif caracteres_especiales=="No" or caracteres_especiales=="NO" or caracteres_especiales=="no":
                for i in range(digitos):
                    if password[i] is None:
                        password[i] = random.choice(letras)
            else:
                return "No digito si o no en ningun formato valido"

        final = "".join(password)
        return "Su contraseña es"+final


while True:

        digitos= input("Digite la cantidad de digitos que quiere en su contraseña: ")
        if digitos.isdigit():
                cant_numeros=input("Digite la cantidad de numeros que desea: ")

                contra = password_generator(int(digitos),int(cant_numeros))
                print(contra)
        else:
                break
