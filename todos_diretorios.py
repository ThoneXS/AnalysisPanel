import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def obter_listas_diretorios(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    links = soup.find_all('a') 

    parsed_url = urlparse(url)
    base_url = f'{parsed_url.scheme}://{parsed_url.netloc}'  

    listas_diretorios = []
    for link in links:
        href = link.get('href') 
        if href is not None and not href.startswith('#'): 
            diretorio = base_url + href
            listas_diretorios.append(diretorio)

    return listas_diretorios
