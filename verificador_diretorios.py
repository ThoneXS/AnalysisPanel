import requests

def analisar_subdiretorios(site):
    url = f"http://{site}"  
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Site {site} encontrado!")

        subdiretorios = ['admin','wp-content','smtp', 'wp-admin','robots.txt', 'login', 'wp-login']
        for subdiretorio in subdiretorios:
            sub_url = f"{url}/{subdiretorio}"
            sub_response = requests.get(sub_url)
            if sub_response.status_code == 200:
                print(f"diretório {subdiretorio} encontrado: {sub_url}")
            else:
                print(f"Subdiretório {subdiretorio} não encontrado.")
    else:
        print(f"Site {site} não encontrado!")


