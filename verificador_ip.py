import re
import requests

def obter_informacoes_ip(ip):
    if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
        # Faz a solicitação para a API
        url = f'https://api.ipgeolocation.io/ipgeo?apiKey=1ca0ade8296a4fbd9aa5d5614143442c&ip={ip}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(f'Informações do IP {ip}:')
            print(f'País: {data["country_name"]}')
            print(f'Cidade: {data["city"]}')
            print(f'Código do País: {data["country_code2"]}')
            print(f'Latitude: {data["latitude"]}')
            print(f'Longitude: {data["longitude"]}')     

        else:
            print(f'Não foi possível obter informações do IP {ip}.')
    else:
        print('Formato de IP inválido.')