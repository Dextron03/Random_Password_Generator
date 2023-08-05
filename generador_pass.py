import random
import sys

print("""
  +=============================================================================+
  |Escribe un programa que sea capaz de generar contraseñas de forma aleatoria. |
  | Podrás configurar generar contraseñas con los siguientes parámetros:        |
  | - Longitud: Entre 8 y 16.                                                   |
  | - Con o sin letras mayúsculas.                                              |
  | - Con o sin números.                                                        |
  | - Con o sin símbolos.                                                       |
  | (Pudiendo combinar todos estos parámetros entre ellos)                      |
  +=============================================================================+
 """)
#=====================================Listas==========================================================================
lista_letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lista_letras_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lista_simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']

lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#=====================================================================================================================
condicion = 0

password : list = [] 

proceso = "✅Siga con el proceso✅\n"


def validation_long_pass():
  """Esta funcion como su nombre indica valida la longitud de la contraseña que usuario queiere generar."""
  while condicion < 1:
    valor_verficacion_log = long_pass()
    cont_log = valor_verficacion_log
    if cont_log >= 8 and cont_log <= 16:
      print(proceso)
      break
    elif cont_log < 8 or cont_log > 16:
      print(f"Porfavor ingrese un valor mayor a 8 y menor que 16")
  return cont_log


def long_pass() -> int:
  """Esta funcion hace que el usuario determine la longitud de la contraseña que quiere generar."""
  usuario_longitud : int = int(input("Ingresa la longitud de tu contraseña (no sea mayor a 16 pero que sea igual o mayor a 8) -->"))
  return usuario_longitud

try:
  validacion_cofirmada = validation_long_pass()
except ValueError:
  print("⚠️ Este programa no acepta letras⚠️, por ahora el programa no podra seguir.")
  sys.exit()

usuario_mayus : str = input(f"Desea que su contraseña contenga letras mayusculas? ").lower()

if usuario_mayus == "si" or usuario_mayus == "yes":
  usuario_mayus = True
else:
  usuario_mayus = False
print(proceso)

usuario_numeros : str = input(f"Desea que su contraseña contenga numeros? ").lower
if usuario_numeros == "si" or usuario_numeros == "yes":
  usuario_numeros = True
else:
  usuario_numeros = False
print(proceso)

usuario_simbolos : str = input(f"Desaaea que su contraseña contenga simbolos? ").lower()
if usuario_simbolos == "si" or usuario_simbolos == "yes":
  usuario_simbolos = True
else:
  usuario_simbolos = False
print(proceso)

def enter_mayus():
    if usuario_mayus is True:
      password.append(random.choice(lista_letras_mayusculas))
    else:
      password.append(random.choice(lista_letras_minusculas))
    return password

def enter_number():
    if usuario_numeros is True:
      password.append(random.choice(lista_numeros))
      return password

def enter_simbolos():
    if usuario_simbolos is True:
     password.append(random.choice(lista_simbolos))
    return password

for x in range(validacion_cofirmada):
  enter_mayus()
  enter_number()
  enter_simbolos()
  
password = "".join(password)
print(f"Tu nueva contraseña contiene {len(password)} caracteres.\nEsta es tu nueva contraseña 🔐--> {password} <--🔐")
