import socket
from random import randint

def clientHandler(connection, client_address):
    print ('Connected by',client_address)
    numero=randint(0,99)

    while True :
        data = (connection.recv(1024)).decode()
        if data == "exit":
            reply = "Gracias por todo"
            connection.sendall(reply.encode())
            connection.close()
            print("Conexion con ", client_address," cerrada")
            break

        else:
            try:
                data=int(data)
                if data==numero:
                    print ("Recibido", repr(data))
                    reply="enhorabuena"
                    connection.sendall(reply.encode())
                    connection.close()
                    print("Conexion con ", client_address," cerrada")
                    break

                elif numero-10<data<numero+10:
                    print ("Recibido", repr(data))
                    reply="Caliente,caliente"
                    connection.sendall(reply.encode())

                elif data<numero-10:
                    print ("Recibido", repr(data))
                    reply="Frio, frio, por abajo"
                    connection.sendall(reply.encode())

                elif data>numero+10:
                    print ("Recibido", repr(data))
                    reply="Frio, frio, por encima"
                    connection.sendall(reply.encode())
            except ValueError:
                reply="Introduzca un numero entero valido"
                connection.sendall(reply.encode())


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= socket.gethostname()
port=8086

s.bind(('127.0.0.1',port))

s.listen(10)

print("Server is running")
while True:
    connection, client_address=s.accept()
    clientHandler(connection, client_address)
s.close()
