import os
import sys
import pyperclip
import time
# * URL del lanzador de la herramienta 
MANUAL_URL = "https://encriptador-zd6m.vercel.app/" 

# * Base de caracteres válidos para codificación
base = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;!?()[]{}\"'*+-/")

# * Palabra clave para autenticación (encriptada con Atbash)
KeyWord = "oozev"

# * Lista de usuarios encriptados con desplazamiento de -19 letras
Usuarios = ["Opetmgbat", "Xfefet", "Itubeh", "Qjutxk", "EnbL", "Ehhf", "Ftkvxe", "Cbgtcgmf", "Uxkxgbvx"]

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

# * Evitar interrupciones inesperadas en la entrada del usuario
def safe_input(mensaje):
    try:
        return input(mensaje)
    except KeyboardInterrupt:
        print("\n\033[31m#INTERUPCION POR EL USUARIO\033[0m") # ! Manejo de Ctrl+C y otras interrupciones
        return None
    except Exception as e:
        print(f"\033[31m#ERROR EN ENTRADA: {type(e).__name__}: {e}\033[0m") # ! Error general en la entrada
        return None

# * Espera un número de segundos (pausa)
def wait(segundos=1):
    time.sleep(segundos)

# * Entrada validada para números enteros
def INPUT_AV(mensaje="<< "):
    texto = safe_input(mensaje)
    if texto is None:
        return None
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
    entrada = safe_input(">> Ingresar CODE: ")
    if entrada is None:
        return []
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

# * Copia un texto al portapapeles 
def COPIAR(texto):
    if pyperclip:
        pyperclip.copy(texto)
        print("\033[36m>> Texto copiado al portapapeles\033[32m")
    else:
        print("\033[31m#ERROR: No se pudo copiar (pyperclip no disponible).\033[0m")

# * Muestra lista de comandos disponibles
def Help():
    print("\033[36m>> Lista de Comandos\033[32m")
    print("HELP => Mostrar ayuda")
    print("TEXT => Convertir texto en código")
    print("CODE => Convertir código en texto")
    print("EXIT => Salir del programa")
    print("CLEAR => Limpiar pantalla")
    print("INFO => Mostrar información del programa")
    print("MANUAL => Abrir el Manual de la herramienta")
    print("\033[2m-Entra el comando\033[36m MANUAL\033[2m y revisa el tutorial-")

# * Abre el lanzador de la herramienta
def Launch(MANUAL_URL):
    if MANUAL_URL:
        print("\033[36m>> Abriendo Manual...\033[32m")
        wait(1)
        os.system(f"start {MANUAL_URL}")  
        print("\033[36m>> Manual abierto\033[32m")
        print()
    else:
        print("\033[31m#ERROR\033[0m")  # ! Error: URL no definida

# * Limpia la pantalla de la consola
def Clear():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[36m>> Pantalla limpiada\033[32m")

# * Procesa la opción ingresada por el usuario
def OPTION(opcion):
    match opcion.upper():
        case "HELP":
            Help()
            print()
        case "EXIT":
            print("\033[0m")
            exit()
        case "TEXT":
            texto = safe_input(">> Ingresar TEXTO: ")
            if texto is None:
                return
            codigo = CAV(texto)
            OUT_CAV(codigo)
            if pyperclip:
                COPIAR(" ".join(map(str, codigo)))
            safe_input("\033[2m>> Presiona ENTER para continuar...\033[32m")
            print()
        case "CODE":
            vector = INPUT_AT()
            if not vector:
                return
            texto = CAT(vector)
            print(">>  Ingresar CODE:", texto)
            if pyperclip:
                COPIAR(" ".join(map(str, vector)))
            safe_input("\033[2m>> Presiona ENTER para continuar...\033[32m")
            print()
        case "INFO":
            PROGRAM_INFO()
            print("LOCAL ID #", LOCAL_USE)
            print()
        case "MANUAL":
            Launch(MANUAL_URL)
        case "CLEAR":
            Clear()
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
USER = safe_input("<< ")
if USER is None:
    exit()
USER = USER.strip()
LOCAL_USE = LOG_IN(USER, Usuarios)

if LOCAL_USE is not None:
    wait(1)
    # * Ingreso de contraseña
    print("\033[32m>> Ingresa tu contraseña:")
    TRY = safe_input("<< ")
    if TRY is None:
        exit()
    TRY = KeyPut(TRY)  # * Se encripta con Atbash para comparar con KeyWord
    if TRY == KeyWord:
        print(">> Bienvenido\033[2m -Escribe HELP para ver comandos-  \033[0m")
        print(f"\033[36m>> {USER.upper()} (ID #{LOCAL_USE})\033[32m")
        print()
        while True:
            # * Interfaz del menú principal
            print("\033[32m", end="")
            entrada = safe_input("<< ")
            if entrada is None:
                break
            entrada = entrada.strip().upper()
            OPTION(entrada)
else:
    print("\033[31m#ERROR: Usuario no válido\033[0m")  
    exit()