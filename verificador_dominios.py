import socket

def listar_dominios(site):
    try:
        ip = socket.gethostbyname(site)
        dominios = socket.gethostbyaddr(ip)
        print(f"Domínios associados ao IP {ip}:")
        for dominio in dominios:
            print(dominio)
    except socket.gaierror:
        print("Não foi possível obter o IP do site.")
