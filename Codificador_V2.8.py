import os
import sys
import time
# * URL del lanzador de la herramienta 
# TODO Colocar la URL del Manual de la herramienta cuando la cree
MANUAL_URL = "https://youtu.be/z34bWo7csl0" 

# * Base de caracteres válidos para codificación
base = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;!?()[]{}\"'*+-/")

# * Palabra clave para autenticación (encriptada con Atbash)
KeyWord = "oozev"

# * Lista de usuarios encriptados con desplazamiento de -19 letras
Usuarios = ["Opetmgbat", "Xfefet", "Itubeh", "Qjutxk", "EnbL", "Ehhf", "Ftkvxe", "Cbgtcgmf"]

USER = ""          # ? Nombre de usuario actual
LOCAL_USE = None   # ? ID del usuario autenticado

# * Cifra un texto usando el cifrado Atbash (letra ↔ opuesta)
def KeyPut(Key):
    Key = Key.lower()
    resultado = ""
    for letra in Key:
        if letra.isalpha():
            letra_opuesta = chr(ord('a') + (25 - (ord(letra) - ord('a'))))
            resultado += letra_opuesta
        else:
            resultado += letra
    return resultado

# * Espera un número de segundos (pausa)
def wait(segundos=1):
    time.sleep(segundos)

# * Entrada validada para números enteros
def INPUT_AV(mensaje="<< "):
    texto = input(mensaje)
    if texto.isnumeric():
        return int(texto)
    else:
        print("\033[31m#ERROR\033[0m")  # ! Error: entrada no válida
        return INPUT_AV(mensaje)

# * Codifica texto en un vector numérico
def CAV(texto):
    vector = []
    if LOCAL_USE is not None:
        vector.append(LOCAL_USE)  # * Primer valor: ID del usuario actual
    else:
        vector.append(-1)  # ! Usuario no autenticado

    for i, c in enumerate(texto):
        if c in base:
            valor = base.index(c)
            codificado = (valor + i) * LOCAL_USE
            vector.append(codificado)
        else:
            vector.append(-1)  # ! Caracter inválido
    return vector

# * Muestra vector codificado como texto plano
def OUT_CAV(vector):
    salida = []
    for val in vector:
        salida.append(str(val))
    print(">> CÓDIGO:", " ".join(salida))

# * Recibe un código por consola y lo convierte en lista de números
def INPUT_AT():
    entrada = input(">> Ingresar CODE: ")
    elementos = entrada.split()
    vector = []
    for elem in elementos:
        if elem.isnumeric() or (elem.startswith("-") and elem[1:].isnumeric()):
            vector.append(int(elem))
        else:
            vector.append(-1)  # ! Elemento inválido
    return vector

# * Decodifica un vector numérico a texto
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

# * Muestra lista de comandos disponibles
def Help():
    print("\033[36m>> Lista de Comandos\033[32m")
    print("HELP => Mostrar ayuda")
    print("TEXT => Convertir texto en código")
    print("CODE => Convertir código en texto")
    print("EXIT => Salir del programa")
    print("INFO => Mostrar información del programa")
    print("MANUAL => Abrir el Manual de la herramienta")
    print("\033[30m-Entra el comando\033[36m MANUAL\033[30m y revisa el tutorial-")

# * Abre el lanzador de la herramienta
def Launch(MANUAL_URL):
    if MANUAL_URL:
        print("\033[36m>> Abriendo lanzador...\033[32m")
        wait(1)
        os.system(f"start {MANUAL_URL}")  
        print("\033[36m>> Lanzador abierto\033[32m")
        print()
    else:
        print("\033[31m#ERROR\033[0m")  # ! Error: URL no definida

# * Procesa los comandos ingresados por el usuario
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
            input("\033[30m>> Presiona ENTER para continuar...\033[32m")
            print()
        case "CODE":
            vector = INPUT_AT()
            texto = CAT(vector)
            print(">>  Ingresar CODE:", texto)
            input("\033[30m>> Presiona ENTER para continuar...\033[32m")
            print()
        case "INFO":
            PROGRAM_INFO()
            print("LOCAL ID #", LOCAL_USE)
            print()
        case "MANUAL":
            Launch(MANUAL_URL)
        case _:
            print("\033[31m#ERROR\033[0m")  # ! Comando no reconocido

# * Muestra información del archivo ejecutado
def PROGRAM_INFO():
    ruta = os.path.abspath(sys.argv[0])
    nombre = os.path.basename(ruta)
    tamaño = os.path.getsize(ruta)
    print("\033[36m>> INFORMACIÓN DEL USUARIO:\033[32m")
    print(f"\033[36m>> {USER.upper()} (ID #{LOCAL_USE})\033[32m")
    print("\033[36m>> INFORMACIÓN DEL PROGRAMA:\033[32m")
    print(" - Nombre:", nombre)
    print(" - Ruta:  ", ruta)
    print(" - Tamaño:", f"{tamaño} bytes ({tamaño / 1024:.2f} KB)")

# * Autenticación: compara el nombre ingresado con la lista cifrada de usuarios
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
            return i  # * Usuario encontrado
    return None  # ! Usuario no encontrado

# TODO Inicio del programa ---------------------------------------------------------------------->
print("\033[36m>> HERRAMIENTA DE ENCRIPTADO")
wait(1)

# * Ingreso de usuario
print("\033[32m>> Ingresa tu nombre de usuario:")
USER = input("<< ").strip()
LOCAL_USE = LOG_IN(USER, Usuarios)

if LOCAL_USE is not None:
    wait(1)
    # * Ingreso de contraseña
    print("\033[32m>> Ingresa tu contraseña:")
    TRY = input("<<").strip()
    TRY = KeyPut(TRY)  # * Se encripta con Atbash para comparar con KeyWord
    if TRY == KeyWord:
        print(">> Bienvenido\033[30m  -Escribe HELP para ver comandos-  \033[0m")
        print(f"\033[36m>> {USER.upper()} (ID #{LOCAL_USE})\033[32m")
        print()
        while True:
            # * Interfaz del menú principal
            print("\033[32m", end="")
            entrada = input("<< ").strip().upper()
            OPTION(entrada)
else:
    print("\033[31m#ERROR: Usuario no válido\033[0m")  
    exit()
