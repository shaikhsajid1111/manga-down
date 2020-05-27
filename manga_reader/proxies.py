import requests
from random import choice
from bs4 import BeautifulSoup
def get_proxy():
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
            chosen_proxy = choice(proxies)
        except IndexError:
            continue

    return {'https':f'https://{chosen_proxy}',
            'http' : f'http://{chosen_proxy}',
            'ftp': f'ftp://{chosen_proxy}'
    }

