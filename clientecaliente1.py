import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port=8086
s.connect(("127.0.0.1",port))
while True:
    mensaje=input("Por favor, introduzca un numero entre 0 y 99: ")
    s.send(mensaje.encode())
    print("Esperando respuesta")
    reply=s.recv(1024).decode()
    print("Recibido:",reply)
    if mensaje=="exit":
        s.close()
        break
    if reply=="enhorabuena":
        s.close()
        break
