import os
import sys
import time

base = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;!?()[]{}\"'*+-/")

Usuarios = ["Opetmgbat", "Xfefet", "Itubeh", "Qjutxk", "EnbL", "Ehhf", "Ftkvxe", "Cbgtcgmf"]

USER = ""        
LOCAL_USE = None 

def wait(segundos=1):
    time.sleep(segundos)

def INPUT_AV(mensaje="<< "):
    texto = input(mensaje)
    if texto.isnumeric():
        return int(texto)
    else: 
        print("\033[31m#ERROR\033[0m") 
        return INPUT_AV(mensaje)

def CAV(texto):
    vector = []
    if LOCAL_USE is not None:
        vector.append(LOCAL_USE)
    else:
        vector.append(-1)  

    for i, c in enumerate(texto):
        if c in base:
            valor = base.index(c)
            codificado = (valor + i) * LOCAL_USE  
            vector.append(codificado)
        else:
            vector.append(-1)
    return vector

def OUT_CAV(vector):
    salida = []
    for val in vector:
        salida.append(str(val))
    print(">> CÓDIGO:", " ".join(salida))

def INPUT_AT():
    entrada = input(">> Ingresar CODE: ")
    elementos = entrada.split()
    vector = []
    for elem in elementos:
        if elem.isnumeric() or (elem.startswith("-") and elem[1:].isnumeric()):
            vector.append(int(elem))
        else:
            vector.append(-1)
    return vector

def CAT(vector):
    texto = ""
    if not vector or vector[0] <= 0:
        return "?"
    USERID = vector[0]
    for i, val in enumerate(vector[1:]):
        if val < 0:
            texto += "?"
        else:
            try:
                original = (val // USERID) - i
                if 0 <= original < len(base):
                    texto += base[original]
                else:
                    texto += "?"
            except:
                texto += "?"
    return texto

def Help():
    print("HELP => Pedir ayuda")
    print("TEXT => Texto a código")
    print("CODE => Código a texto")
    print("EXIT => Salir")
    print("INFO => Información del programa")

def OPTION(opcion):
    match opcion.upper():
        case "HELP":
            Help()
            print()
        case "EXIT":
            print("\033[0m") 
            exit()
        case "TEXT":
            texto = input(">> Ingresar TEXTO: ")
            codigo = CAV(texto)
            OUT_CAV(codigo)
            input(">> Presiona ENTER para continuar...")
            print()
        case "CODE":
            vector = INPUT_AT()
            texto = CAT(vector)
            print(">> TEXTO:", texto)
            input(">> Presiona ENTER para continuar...")
            print()
        case "INFO":
            PROGRAM_INFO()
            print("LOCAL ID #", LOCAL_USE)
            print()
        case _:
            print("\033[31m#ERROR\033[0m")

def PROGRAM_INFO():
    ruta = os.path.abspath(sys.argv[0])
    nombre = os.path.basename(ruta)
    tamaño = os.path.getsize(ruta)
    print(">> INFORMACIÓN DEL PROGRAMA")
    print(" - Nombre:", nombre)
    print(" - Ruta:  ", ruta)
    print(" - Tamaño:", f"{tamaño} bytes ({tamaño / 1024:.2f} KB)")

def LOG_IN(nombre, lista):
    nombre = nombre.upper()
    for i, item in enumerate(lista):
        descifrado = ""
        for c in item:
            if c.isupper():
                descifrado += chr((ord(c) - ord('A') - 19) % 26 + ord('A'))
            elif c.islower():
                descifrado += chr((ord(c) - ord('a') - 19) % 26 + ord('a'))
            else:
                descifrado += c
        if descifrado.upper() == nombre:
            return i 
    return None

# --- Inicio del programa ---
print("\033[36m>> ENCRIPTER")
wait(1)
print("\033[32m>> log IN:")
USER = input("<< ").strip()
LOCAL_USE = LOG_IN(USER, Usuarios)

if LOCAL_USE is not None:
    print(">> Welcom")
    print(f"\033[36m>> {USER.upper()} (ID #{LOCAL_USE})\033[32m") 
    while True:
        print("\033[32m", end="") 
        entrada = input("<< ").strip().upper()
        OPTION(entrada)
else:
    print("\033[31m#ERROR\033[0m")  
    exit() 