from colorama import Fore, Style
import os
import platform

caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def banner():
    title = """
                                                                                                                      
 @@@@@@@  @@@  @@@@@@@@  @@@@@@@    @@@@@@   @@@@@@@    @@@@@@       @@@@@@@  @@@@@@@@   @@@@@@    @@@@@@   @@@@@@@   
@@@@@@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@@@@@@  
!@@       @@!  @@!       @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@     !@@       @@!       !@@       @@!  @@@  @@!  @@@  
!@!       !@!  !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@     !@!       !@!       !@!       !@!  @!@  !@!  @!@  
!@!       !!@  @!!!:!    @!@!!@!   @!@!@!@!  @!@  !@!  @!@  !@!     !@!       @!!!:!    !!@@!!    @!@!@!@!  @!@!!@!   
!!!       !!!  !!!!!:    !!@!@!    !!!@!!!!  !@!  !!!  !@!  !!!     !!!       !!!!!:     !!@!!!   !!!@!!!!  !!@!@!    
:!!       !!:  !!:       !!: :!!   !!:  !!!  !!:  !!!  !!:  !!!     :!!       !!:            !:!  !!:  !!!  !!: :!!   
:!:       :!:  :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!     :!:       :!:           !:!   :!:  !:!  :!:  !:!  
 ::: :::   ::   ::       ::   :::  ::   :::   :::: ::  ::::: ::      ::: :::   :: ::::  :::: ::   ::   :::  ::   :::  
 :: :: :  :     :         :   : :   :   : :  :: :  :    : :  :       :: :: :  : :: ::   :: : :     :   : :   :   : :
By XenoCode.

Seleccione una opcion.
[1] Cifrar
[2] Decifrar
[3] Exit
 """
    
    print(Fore.BLUE + title)

def limpiar():
    if platform.system() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def cipher(textos, desplazamiento):
    result = ""
    may_caracteres = [c.upper() for c in caracteres] # caracteres en mayusculas

    for texto in textos:
        if texto.isalpha(): # Verificamos si solo es texto
            if texto.isupper(): # Verificamos si el texto es mayuscula
                des = may_caracteres.index(texto)
                new_des = (des + desplazamiento) % 26
                result += may_caracteres[new_des]
            else: # Para texto minusculas
                des = caracteres.index(texto)
                new_des = (des + desplazamiento) % 26
                result += caracteres[new_des]
        else: # Guarda si son caracteres o espacios
            result+=texto

    print(f"[*] Tu texto se a cifrado correctamente: {Fore.GREEN}{result}{Style.RESET_ALL}") # Muestra el resultado

def des_cipher(textos, desplazamiento):
    result = ""
    may_caracteres = [c.upper() for c in caracteres] # caracteres en mayusculas

    for texto in textos:
        if texto.isalpha(): # Verificamos si solo es texto
            if texto.isupper(): # Verificamos si el texto es mayuscula
                des = may_caracteres.index(texto)
                new_des = (des - desplazamiento) % 26
                result += may_caracteres[new_des]
            else: # Para texto minusculas
                des = caracteres.index(texto)
                new_des = (des - desplazamiento) % 26
                result += caracteres[new_des]
        else: # Guarda si son caracteres o espacios
            result+=texto

    print(f"[*] El mensaje fue decifrado correctamente: {Fore.GREEN}{result}{Style.RESET_ALL}") # Muestra el resuultado

if __name__ == "__main__":
    banner()
    try:
        while True:
            limpiar()
            options = int(input())

            if options == 1:
                limpiar()
                print("Que mensaje le gustaria cifrar")
                textos = input("> ")
                print("Cuanto de desplazamiento le gustaria poner.")
                desplazamiento = int(input("> "))

                cipher(textos,desplazamiento)
                input("\nPresiona Enter para salir...")
                exit()

            elif options == 2:
                print("Que mensaje le gustaria decifrar")
                textos = input("> ")
                print("Cuanto de desplazamiento le gustaria poner.")
                desplazamiento = int(input("> "))

                des_cipher(textos,desplazamiento)
                input("\nPresiona Enter para salir...")
                exit()
            elif options == 3:
                exit()
            else:
                print(f"{Fore.RED}[*] Porfavor seleccione una opcion valida.{Style.RESET_ALL}")
                input("\nPresiona Enter para salir...")
                exit()
    except Exception as e:
        print("Error:", e)
        exit()
