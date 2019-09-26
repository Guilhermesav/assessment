#Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
#Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
#Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela.
#O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.
import requests
import re
from bs4 import BeautifulSoup
from collections import defaultdict

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text

soup = BeautifulSoup(html,"html.parser")


for i in soup.html.body.find_all('div'):
    text = re.sub(' +', ' ', i.text)
    text = re.sub('\n', '', text)
   