#Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
#https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
#E:
#Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique:
#No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
#Curling
#Patinação no gelo (skating)
#Esqui (skiing)
#Hóquei sobre o gelo (ice hockey)
#Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino.
#Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.
import requests
import urllib3
import csv
import re
from bs4 import BeautifulSoup
from collections import defaultdict,OrderedDict,Counter
locais = ["Salt Lake City","Turin"]
anos = ["2002","2006"]
genero = ["masculino","feminino"]
sweM02= defaultdict(int)
sweM06= defaultdict(int)
sweF02= defaultdict(int)
sweF06= defaultdict(int)
denM02 = defaultdict(int)
denM06 = defaultdict(int)
denF02 = defaultdict(int)
denF06 = defaultdict(int)
norM02 = defaultdict(int)
norM06 = defaultdict(int)
norF02 = defaultdict(int)
norF06 = defaultdict(int)
with open('Winter_Olympics_Medals.csv') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
        print(row)
        if row[0] == '2002':
            if row[4] == 'SWE':
                if row[2] == 'Skiing':
                    sweM02[row[2]] = 0
                    sweF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF[row[2]] += 1
                if row[2] == 'Curling':
                    sweM02[row[2]] = 0
                    sweF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF02[row[2]] += 1
                if row[2] == 'Skating':
                    sweM02[row[2]] = 0
                    sweF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF02[row[2]] += 1
                if row[2] == 'Ice Hockey':
                    sweM02[row[2]] = 0
                    sweF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF02[row[2]] += 1
                            
            if row[4] == 'NOR':
                if row[2] == 'Skiing':
                    norM02[row[2]] = 0
                    norF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF02[row[2]] += 1
                if row[2] == 'Curling':
                    norM02[row[2]] = 0
                    norF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF02[row[2]] += 1
                if row[2] == 'Skating':
                    norM02[row[2]] = 0
                    norF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF02[row[2]] += 1
                if row[2] == 'Ice Hockey':
                    norM02[row[2]] = 0
                    norF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM0202[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF02[row[2]] += 1
                            
            if row[4] == 'DEN':
                if row[2] == 'Skiing':
                    denM02[row[2]] = 0
                    denF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF02[row[2]] += 1
                if row[2] == 'Curling':
                    denM02[row[2]] = 0
                    denF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF02[row[2]] += 1
                if row[2] == 'Skating':
                    denM02[row[2]] = 0
                    denF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF02[row[2]] += 1
                if row[2] == 'Ice Hockey':
                    denM02[row[2]] = 0
                    denF02[row[2]] = 0
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM02[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF02[row[2]] += 1
        if row[0] == '2006':
            if row[4] == 'SWE':
                if row[2] == 'Skiing':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF06[row[2]] += 1
                if row[2] == 'Curling':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF06[row[2]] += 1
                if row[2] == 'Skating':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF06[row[2]] += 1
                if row[2] == 'Ice Hockey':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            sweM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            sweF06[row[2]] += 1
                            
            if row[4] == 'NOR':
                if row[2] == 'Skiing':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF06[row[2]] += 1
                if row[2] == 'Curling':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF06[row[2]] += 1
                if row[2] == 'Skating':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF06[row[2]] += 1
                if row[2] == 'Ice Hockey':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            norM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            norF06[row[2]] += 1
                            
                        
            if row[4] == 'DEN':
                if row[2] == 'Skiing':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF06[row[2]] += 1
                if row[2] == 'Curling':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF06[row[2]] += 1
                if row[2] == 'Skating':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF06[row[2]] += 1
                if row[2] == 'Ice Hockey':
                    if row[6] == 'M':
                        if row[7] == 'Gold':
                            denM06[row[2]] += 1
                    if row[6] == 'W':
                        if row[7] == 'Gold':
                            denF06[row[2]] += 1
        
"""suecia = dict.values(Counter(sweM02) + Counter(sweF02) + Counter(sweM06) + Counter(sweF06))
dinamarca = dict.values(Counter(denM02) + Counter(denF02) + Counter(denM06) + Counter(denF06))
noruega = dict.values(Counter(norM02) + Counter(norF02) + Counter(norM06) + Counter(norF06))
maior_medalhista = {}
maior_medalhista['Suecia'] = sum(suecia)
maior_medalhista['Dinamarca'] = sum(dinamarca)
maior_medalhista['Noruega'] = sum(noruega)

print("O maior medalhista é a", max(maior_medalhista.keys()),"com",max(maior_medalhista.values()),"medalhas.")


print("Nas Olimpiadas de inverno de 2002, em Salt Lake City, a seleção olimpica sueca medalhou ouro nos seguintes esportes:")
print("Modalidades masculinas:", dict(sweM02))
print("Modalidades femininas:", dict(sweF02))
print("Nas Olimpiadas de inverno de 2002, em Salt Lake City, a seleção olimpica dinamarquesa medalhou ouro nos seguintes esportes:")
print("Modalidades masculinas:", dict(denM02))
print("Modalidades femininas:", dict(denF02))
print("Nas Olimpiadas de inverno de 2002, em Salt Lake City, a seleção olimpica norueguesa medalhou ouro nos seguintes esportes")
print("Modalidades masculinas:", dict(norM02))
print("Modalidades femininas:", dict(norF02))
print("Nas Olimpiadas de inverno de 2006, em Turin, a seleção olimpica sueca medalhou ouro nos seguintes esportes")
print("Modalidades masculinas:", dict(sweM06))
print("Modalidades femininas:", dict(sweF06))
print("Nas Olimpiadas de inverno de 2006, em Turin, a seleção olimpica dinamarquesa medalhou ouro nos seguintes esportes")
print("Modalidades masculinas:", dict(denM06))
print("Modalidades femininas:", dict(denF06))
print("Nas Olimpiadas de inverno de 2006, em Turin, a seleção olimpica norueguesa medalhou ouro nos seguintes esportes")
print("Modalidades masculinas:", dict(norM06))
print("Modalidades femininas:", dict(norF06))"""
