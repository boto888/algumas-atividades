import requests
import pprint
key_api = "d2817fd89e7d4b008cf153915252404"
url_da_api = "http://api.weatherapi.com/v1/current.json"

parametro = {
    'key': key_api,
    'q': 'teresina',
    'lang': 'pt'
}

resposta = requests.get(url_da_api, params=parametro)
if resposta.status_code == 200:
    print('deu certo')
    dados = resposta.json()
    #pprint.pprint(dados)
    temp = dados['current']['temp_c']
    condicao = dados['current']['condition']['text']
    print(temp)
    print(condicao)
