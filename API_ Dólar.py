from urllib import response
import requests as req 

url =  'https://economia.awesomeapi.com.br/all/USD-BRL'

response = req.get(url)

if response.status_code == 200:
    dolar_value = response.json()['USD']['high']
    data_atualizacao = response.json()['USD']['create_date']
    print(f'O valor do dólar é R$ {dolar_value}')
    print(f'Data de atualização {data_atualizacao}')
else:
    print('Erro ao buscar o valor do dólar!')




