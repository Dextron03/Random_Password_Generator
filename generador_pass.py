import random
import sys

# Mensaje de presentación y descripción del programa.
print("""
  +=============================================================================+
  | Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.|
  | Podrás configurar generar contraseñas con los siguientes parámetros:        |
  | - Longitud: Entre 8 y 16.                                                   |
  | - Con o sin letras mayúsculas.                                              |
  | - Con o sin números.                                                        |
  | - Con o sin símbolos.                                                       |
  | (Pudiendo combinar todos estos parámetros entre ellos)                      |
  +=============================================================================+
""")

def main():
    print(f"Tu nueva contraseña contiene {len(password)} caracteres.")
    print(f"Esta es tu nueva contraseña: 🔐 {password} 🔐")

def long_pass() -> int:
    """Permite al usuario determinar la longitud de la contraseña que quiere generar (entero)."""
    usuario_longitud = int(input("Ingrese la longitud de su contraseña (entre 8 y 16): "))
    return usuario_longitud

def validation_long_pass():
    """Valida la longitud de la contraseña que el usuario quiere generar."""
    while condicion < 1:
        valor_verificacion_long = long_pass()
        cont_log = valor_verificacion_long
        if cont_log >= 8 and cont_log <= 16:
            print(proceso)
            break
        elif cont_log < 8 or cont_log > 16:
            print(f"Por favor, ingrese un número entero mayor a 8 y menor que 16.")
    return cont_log

def enter_mayus(lista_letras):
    """Agrega letras mayúsculas o minúsculas a la contraseña, según la elección del usuario."""
    if usuario_mayus is True:
        password.append(random.choice(lista_letras))
    else:
        password.append(random.choice(lista_letras_minusculas))
    return password

def enter_number(lista_numeros):
    """Agrega números a la contraseña si el usuario lo desea."""
    if usuario_numeros is True:
        password.append(random.choice(lista_numeros))
    return password

def enter_simbolos(lista_simbolos):
    """Agrega símbolos a la contraseña si el usuario lo desea."""
    if usuario_simbolos is True:
        password.append(random.choice(lista_simbolos))
    return password

# Listas con posibles opciones para la generación de contraseñas.
lista_letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista_letras_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']
lista_numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

condicion = 0
password: list = []
proceso = "✅ Siga con el proceso ✅\n"
error = "⚠️ Error: Ingrese valores válidos. ⚠️"

try:
    # Validación de que el usuario ingrese correctamente la longitud deseada.
    validacion_confirmada = validation_long_pass()
except ValueError:
    print("⚠️ Error al ejecutar el programa. ⚠️\nEl programa no podrá continuar.")
    sys.exit()

print("""
      +==============================+
      | Para continuar ingrese [y/n] |
      +==============================+
      """)

while condicion == 0:
    usuario_mayus = input(f"Desea que su contraseña contenga letras mayúsculas? [y/n]: ").lower()
    if usuario_mayus == "y":
        usuario_mayus = True
        print(proceso)
        break
    elif usuario_mayus == "n":
        usuario_mayus = False
        print(proceso)
        break
    else:
        print(error)

while condicion == 0:
    usuario_numeros = input(f"Desea que su contraseña contenga números? [y/n]: ").lower()
    if usuario_numeros == "y":
        usuario_numeros = True
        print(proceso)
        break
    elif usuario_numeros == "n":
        usuario_numeros = False
        print(proceso)
        break
    else:
        print(error)

while condicion == 0:
    usuario_simbolos = input(f"Desea que su contraseña contenga símbolos? [y/n]: ").lower()
    if usuario_simbolos == "y":
        usuario_simbolos = True
        print(proceso)
        break
    elif usuario_simbolos == "n":
        usuario_simbolos = False
        print(proceso)
        break
    else:
        print(error)

# Generar la contraseña aleatoria con los parámetros configurados por el usuario.
for _ in range(validacion_confirmada):
    if len(password) < validacion_confirmada:
        enter_mayus(lista_letras_mayusculas)
    if len(password) < validacion_confirmada:
        enter_number(lista_numeros)
    if len(password) < validacion_confirmada:
        enter_simbolos(lista_simbolos)

# Convertir la lista de contraseñas en una sola cadena y mostrar la contraseña generada.
password = "".join(password)

main()