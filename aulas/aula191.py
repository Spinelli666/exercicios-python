# requests para reqisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs

import requests

# http:// -> Está rodando automaticamente na porta 80
# https:// -> Está rodando automaticamente na porta 443

url = 'http://127.0.0.1:5500/aulas/aula190_site/index.html'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
# print(response.json())