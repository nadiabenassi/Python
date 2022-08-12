
contraseña1 = input("Escriba su contraseña: ")
contraseña2 = input("Escriba de nuevo su contraseña: ")
contador = 1
while contraseña1 != contraseña2:
    print("Las contraseñas no coinciden. Inténtelo de nuevo.")
    contraseña2 = input("Escriba de nuevo su contraseña: ")
if contraseña1 == contraseña2:
        print("Contraseña confirmada")

