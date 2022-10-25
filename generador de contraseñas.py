import random

cantidad = int(input("Cantidad de caracteres de la contraseña: "))

minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "@#$%&/?!"

uso_para = minusculas + mayusculas + numeros + simbolos
ancho_contraseña = cantidad

contraseña = "".join(random.sample(uso_para,ancho_contraseña))
print("Tu contraseña generada es: ", contraseña)