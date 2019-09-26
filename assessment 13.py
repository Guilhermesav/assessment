#Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
#Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
#Conte quantas vezes apareceu a palavra ladies no conteúdo da página
import requests
import re
from bs4 import BeautifulSoup
from collections import defaultdict

url = "http://brasil.pyladies.com/about"

html = requests.get(url).text

soup = BeautifulSoup(html,'html.parser')
palavras = []
cont =[]
dicionario = defaultdict(int)
for i in soup.html.body.find_all('p'):
    text = re.sub(' +', ' ', i.text)
    text = re.sub('\n', '', text)
    if text is not " ":
        for palavras in text.split(" "):
            dicionario[palavras.lower()] += 1
            

       

for palavra in palavras:
    dicionario[palavra] +=1
for item in dicionario.items():
    if item[1] == 1:
        cont.append((item[0],item[1]))
cont.sort(key=lambda x : x[1])
print(cont)
print("A palavra ladies aparece",dicionario["ladies"],"vezes")

        
        