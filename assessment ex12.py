#Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
#Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
#Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela.
#O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.
import requests
import re
from bs4 import BeautifulSoup
from collections import defaultdict
from tabulate import tabulate

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text

soup = BeautifulSoup(html,"html.parser")


tabela = soup.find('div',{'class':'tabela'})
#print(tabela)

DFdict = defaultdict(int)
MTdict = defaultdict(int)
GOdict = defaultdict(int)
MSdict = defaultdict(int)
info_estados = []
estados = tabela.findAll('div',{'class':'linha'})
titulo = tabela.findAll('div',{'class':'titulo'})
titulos = []
for i in titulo:
    text = re.sub(' +', ' ', i.text)
    text = re.sub('\n', '', text)
    titulos.append(i.text)
    #print(i.text)
for i in estados:
    text = re.sub(' +', ' ', i.text)
    text = re.sub('\n', '', text)
    info_estados.append(i.text)
   #print(i.text)
    
celula = tabela.findAll('div',{'class':'celula'})
for i in celula:
    text = re.sub(' +', ' ', i.text)
    text = re.sub('\n', '', text)
    #print(i.text)
    
separacaodf = info_estados[0].replace('\n',' ')
separacaogo = info_estados[1].replace('\n',' ')
separacaomt = info_estados[2].replace('\n',' ')
separacaoms = info_estados[3].replace('\n',' ')
info_mt = separacaomt.split()
info_go = separacaogo.split()
info_df = separacaodf.split()
info_ms = separacaoms.split()
cabecalho = titulos[0].split()
DFdict[cabecalho[3]] = info_df[4]
DFdict[cabecalho[4]] = info_df[5]
GOdict[cabecalho[3]] = info_go[3]
GOdict[cabecalho[4]] = info_go[4]
MTdict[cabecalho[3]] = info_mt[4]
MTdict[cabecalho[4]] = info_mt[5]
MSdict[cabecalho[3]] = info_ms[7]
MSdict[cabecalho[4]] = info_ms[8]
print("Insira a sigla de um estado:")
sigla = input()
if sigla.lower() == 'df':
    print("O nome do estado é",info_df[1],info_df[2])
    print("Sua capital é",info_df[3])
    print("Sua população é",DFdict["População"],"e sua área", DFdict["Área"])
if sigla.lower() == 'go':
    print("O nome do estado é",info_go[1])
    print("Sua capital é",info_go[2])
    print("Sua população é",GOdict["População"],"e sua área", GOdict["Área"])
if sigla.lower() == 'mt':
    print("O nome do estado é",info_mt[1],info_mt[2])
    print("Sua capital é",info_mt[3])
    print("Sua população é",MTdict["População"],"e sua área", MTdict["Área"])
if sigla.lower() == 'ms':
    print("O nome do estado é",info_ms[1],info_mt[2],info_ms[3],info_ms[4])
    print("Sua capital é",info_ms[5],info_ms[6])
    print("Sua população é",MSdict["População"],"e sua área", MSdict["Área"])
else:
    print("Os dados deste estado não estão registrados")
    


    

