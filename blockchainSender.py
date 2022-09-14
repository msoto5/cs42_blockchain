import requests as rq
from hashlib import sha256


PORT = 8080
SERVER = 'http://localhost:8080'

def enviar_transaccion():
    print("Introduzca el nombre del emisor:")
    emisor = input()
    print()
    print("Introduzca el nombre del receptor:")
    receptor = input()
    print()
    print("Introduzca la cantidad:")
    cantidad = input()
   
    headers = {"Sender":emisor,"Receiver": receptor,"Amount":cantidad}
    r = rq.post(SERVER+'/transactions/new',headers=headers)

    if r.status_code == 200:
        print("La transacción se ha registrado con éxito")
    else:
        print("error al registrar la transacción")
    return

def get_mine():
    print(SERVER+'/mine')
    r = rq.get(SERVER+'/mine')
    if r.status_code == 200:
        print("El bloque se ha minado con éxito")
    else:
        print("Error al minar y crear un nuevo bloque")
    return

def get_chain():
    r = rq.get(SERVER+"/chain")
    if r.status_code == 200:
        print("La cadena de bloques es:")
        print(r.text)
    else:
        print("Error al intentar obtener la cadena de bloques")


opcion = "0"
while(opcion != "4"):
    print()
    print("Escoge una opción:")
    print("\t1.- Envía una nueva transacción para añadir al próximo bloque.")
    print("\t2.- Ejecuta la prueba de trabajo y crea un nuevo bloque")
    print("\t3.- Devuelve la información sobre la cadena de bloques")
    print("\t4.- Salir")


    opcion = input()

    if opcion[0] == "1":
        enviar_transaccion()
    elif opcion[0] == "2":
        get_mine()
    elif opcion[0] == "3":
        get_chain()
    elif opcion[0] != "4":
        print("Wrong option. Try again: ")

print("Saliendo...")
