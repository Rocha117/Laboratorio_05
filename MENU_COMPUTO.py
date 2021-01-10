
class Usuario:
	def __init__(self, username, password):
		self.username = username
		self.__password = password

	def __check_usuario(self,username,password):
		if (self.username == username):
			if (self.__password == password):
				return True
			else:
				return False
		else:
			return False

	def inicia_sesion(self,username,password):
		if self.__check_usuario(username, password) == True:
			return True
		else:
			return False

huellas_base=[111,222,333]#simula la base de tados
i=0

Administrador = Usuario(75317886,123) #username es el nº de dni


def main():
    while i==0:
        menu()
            
def menu():
    print("_______________________________________________________________________________\n")
    print("                             LABORATORIO DE COMPUTO                            ")
    print("_______________________________________________________________________________\n")
    print(" 1. Iniciar sesion\n")
    try:
        opcion=int(input(" Opcion: "))      
    except:
        print("INGRESE UNA OPCION CORRECTA")
        menu ()        
    if opcion==1:
        menu_usuarios()
    else:
        print("Opcion Invalida")

def registrarse():
    usuario=int(input("USERNAME: "))
    print()
    contraseña = int(input("PASSWORD: "))
    print()
    resultado = Administrador.inicia_sesion(usuario,contraseña)
    if resultado == 1:
        print("Ingrese sus datos personales\n")
        nombre=str(input("Nombres: "))
        apellido=str(input("Apellido: "))
        dni=int(input("DNI: "))
        huella_hash=int(input("Huella digital: "))
        print("Se ha registrado con exito")
            
def menu_usuarios():
    print("_______________________________________________________________________________\n")
    print("                                INICIO DE SESION                               ")
    print("_______________________________________________________________________________\n")
    print(" 1. Ingresar               2. Registrarse               3. Salir\n")
    opcion=int(input("Opcion: "))
    print()
    if opcion ==1:
        huella_sensor=int(input("Identifiquese con su huella digital: "))#
        if huella_sensor in huellas_base: #simular que la huella esta en la base de datos
            print("\nAcceso permitido\n")
            print("BIENVENIDO AL LABORATORIO DE COMPUTO\n")
        else:
            print("\nAcceso denegado, su huella digital no esta registrada\n")
            print("1. Registrar huella digital           2. Salir\n")
            opcion=int(input("Opcion: "))
            print()
            if opcion==1:
                registrarse()
    elif opcion == 2:
        registrarse()

    elif opcion==3:
        print("Cerrando sesion ...")
       
    else:
        print("Opcion Invalida")
           
if __name__ == '__main__':
	main()
