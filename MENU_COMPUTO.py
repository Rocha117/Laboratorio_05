import psycopg2
import Comandos
from os import system


class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def __check_usuario(self, username, password):
        if (self.username == username):
            if (self.__password == password):
                return True
            else:
                return False
        else:
            return False

    def inicia_sesion(self, username, password):
        if self.__check_usuario(username, password) == True:
            return True
        else:
            return False


i = 0

# username es el nº de dni del administrador
Administrador = Usuario(75317886, 123)


def menu():
    print("_______________________________________________________________________________\n")
    print("                             LABORATORIO DE COMPUTO                            ")
    print("_______________________________________________________________________________\n")
    print(" 1. Iniciar sesion\n")
    try:
        opcion = int(input(" Opcion: "))
    except:
        print("INGRESE UNA OPCION CORRECTA")
        menu()
    if opcion == 1:
        menu_usuarios()
    else:
        print("Opcion Invalida")


def registrarse():
    usuario = int(input("USERNAME: "))
    print()
    contraseña = int(input("PASSWORD: "))
    print()
    resultado = Administrador.inicia_sesion(usuario, contraseña)
    if resultado == True:
        print("Ingrese sus datos personales\n")
        nombre = str(input("Nombre: "))
        apellido = str(input("Apellido: "))
        input("Huella digital: ")
        huella_hash = Comandos.hashF()
        Comandos.añadir("Huella", huella_hash, nombre, apellido)
        b = Comandos.Buscar(huella_hash)
        print("\nSe ha registrado con exito\n")
        print(f"Nombre: {b[2]}\n")
        print(f"Apellido: {b[3]}\n")
        print(f"Valor Hash de la huella: {b[1]}\n")


def menu_usuarios():
    print("_______________________________________________________________________________\n")
    print("                                INICIO DE SESION                               ")
    print("_______________________________________________________________________________\n")
    print(" 1. Ingresar               2. Registrarse               3. Salir\n")
    opcion = int(input("Opcion: "))

    print()
    Comandos.Crear_tabla("Huella")
    system("cls")

    if opcion == 1:
        huella_sensor = str(input("Identifiquese con su huella digital: "))
        bus = Comandos.Buscar(huella_sensor)
        if bus != None:
            print("\nAcceso permitido\n")
            print(
                f"BIENVENIDO {bus[2]} {bus[3]} AL LABORATORIO DE COMPUTO\n")
        else:
            pass
        if bus == None:
            print("\nAcceso denegado, su huella digital no esta registrada\n")
            print("1. Registrar huella digital           2. Salir\n")
            opcion = int(input("Opcion: "))
            print()
            if opcion == 1:
                registrarse()

            elif opcion == 2:
                print("Cerrando sesion ...")
            else:
                print("Opcion Invalida")

    elif opcion == 2:
        registrarse()

    elif opcion == 3:
        print("Cerrando sesion ...")

    else:
        print("Opcion Invalida")


if __name__ == '__main__':
    menu()
