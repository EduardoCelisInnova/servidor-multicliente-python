# Servidor Multicliente en Python

Servidor TCP que atiende múltiples clientes simultáneamente usando hilos (threading).

## Características

- Escucha en `127.0.0.1:8888`
- Cada cliente se ejecuta en su propio hilo
- Responde "Mensaje recibido" a cada cliente
- Soporte para múltiples conexiones concurrentes

## Cómo usarlo

### Terminal 1 (Servidor)
```bash
python servidor.py

### Terminal 2
python cliente.py

### Terminal 3
python cliente.py

### Requisitos

    Python 3.x

    Módulos: socket, threading (incluidos en Python estándar)

Autor

Ing. Eduardo Celis
