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
action = defaultdict(int)
activision = []
activisionjp = []
ubi = []
ubijp = []
ea = []
eajp = []
thq = []
thqjp = []
nbg = []
nbgjp = []
capcom = []
capcomjp = []
kde = []
kdejp = []
nint = []
nintjp = []
sony = []
sonyjp = []
sega = []
segajp = []
shooter = defaultdict(int)
platform = defaultdict(int)
with open('video_games.csv') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',')
    for row in csv_content:
        if row[4] == 'Activision':
           activision.append(float(row[9]))
           activisionjp.append(float(row[7]))
        if row[4] == 'Ubisoft':
           ubi.append(float(row[9]))
           ubijp.append(float(row[7]))
        if row[4] == 'Electronic Arts':
           ea.append(float(row[9]))
           eajp.append(float(row[7]))
        if row[4] == 'THQ':
           thq.append(float(row[9]))
           thqjp.append(float(row[7]))   
        if row[4] == 'Namco Bandai Games':
           nbg.append(float(row[9]))
           nbgjp.append(float(row[7]))
        if row[4] == 'Capcom':
           capcom.append(float(row[9]))
           capcomjp.append(float(row[7]))
        if row[4] == 'Konami Digital Entertainment':
           kde.append(float(row[9]))
           kdejp.append(float(row[7]))
        if row[4] == 'Nintendo':
           nint.append(float(row[9]))
           nintjp.append(float(row[7]))
        if row[4] == 'Sony Computer Entertainment':
           sony.append(float(row[9]))
           sonyjp.append(float(row[7]))
        if row[4] == 'Sega':
           sega.append(float(row[9]))
           segajp.append(float(row[7]))
        if row[3] == 'Action':
            action[row[4]] += 1
        if row[3] == 'Platform':
            platform[row[4]]+=1
        if row[3] == 'Shooter':
            shooter[row[4]] += 1
        

sorted_action = dict(sorted(action.items(), key=lambda kv: kv[1],reverse = True))
sorted_platform = dict(sorted(platform.items(), key=lambda kv: kv[1],reverse = True))
sorted_shooter = dict(sorted(shooter.items(), key = lambda kv: kv[1],reverse = True))
#Procurar as três marcas que mais publicaram nestes três generos:
action_e_shooter_e_platform = Counter(sorted_action) + Counter(sorted_shooter) + Counter(sorted_platform)
top_3_publi= action_e_shooter_e_platform.most_common(10)
print(top_3_publi) # A
    
#Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
dict_total = {}

empresas = ['Activision','Ubisoft','Electronic Arts','THQ','Namco Bandai Games','Capcom','Konami Digital Entertainment','Nintendo','Sony Computer Entertainment','Sega']
lista_total = [sum(activision), sum(ubi),sum(ea),sum(thq),sum(nbg),sum(capcom),sum(kde),sum(nint),sum(sony),sum(sega)]

dict_total = Counter(dict(zip(empresas,lista_total)))

print(dict_total.most_common(3)) # B

#Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.
dict_totaljp = {}

empresas = ['Activision','Ubisoft','Electronic Arts','THQ','Namco Bandai Games','Capcom','Konami Digital Entertainment','Nintendo','Sony Computer Entertainment','Sega']
lista_totaljp = [sum(activisionjp), sum(ubijp),sum(eajp),sum(thqjp),sum(nbgjp),sum(capcomjp),sum(kdejp),sum(nintjp),sum(sonyjp),sum(segajp)]

dict_totaljp = Counter(dict(zip(empresas,lista_totaljp)))
print(dict_totaljp.most_common(3)) # C e D

