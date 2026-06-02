# Configuracion de cliente para pruebas con la conexion del servidor.

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 8888))
cliente.send(b"Hola servidor")
datos = cliente.recv(1024)
print(f"Mensaje del servidor: {datos.decode()}")

cliente.close()

