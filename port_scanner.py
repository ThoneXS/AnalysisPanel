import socket

def verificar_portas_abertas(host, portas):
    for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  

        resultado = sock.connect_ex((host, porta))
        if resultado == 0:
            print(f"A porta {porta} está aberta.")
        else:
            print(f"A porta {porta} está fechada.")

        sock.close()
