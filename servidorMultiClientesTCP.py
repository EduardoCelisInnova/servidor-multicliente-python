# Servidor para conexion de clientes multiples.

print("Servidor de conexion de clientes multiples.")

import socket
import threading

def manejarCliente(cliente, direccion):
    print(f"Cliente {direccion} conectado: ")
    #recibir datos
    datos = cliente.recv(1024)
    print(f"Datos recibidos: {datos}")
    #enviar respuesta
    cliente.send(b"Mensaje recibido")
    #cerrar
    cliente.close()
    pass

    
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 8888))
servidor.listen(5)

print("Servidor escuchando...")

#inicio del ciclo while

while True:
    # crear un hilo que ejecute variable manejar cliente
    cliente, direccion = servidor.accept()
    # Pasarle cliente y direccion
    hilo = threading.Thread(target=manejarCliente, args=(cliente, direccion))
    # Iniciar el hilo
    hilo.start()
