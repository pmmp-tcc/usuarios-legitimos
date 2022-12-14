import botometer
import os
import pandas as pd
import random

"""Selecionando o diretório dos meus aquivos de interesse"""

Path = '/content/drive/MyDrive/Colab Notebooks'

os.chdir(Path)

rapidapi_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twitter_app_auth = {
    'consumer_key': 'xxxxxxxxxxxxxxxxxxxx',
    'consumer_secret': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'access_token': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'access_token_secret': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

"""Abrindo arquivo de texto que contém os IDs das contas"""

archive = open('Usuarios_xxx.txt', 'r')

Base = archive.readlines()

Data = list()

for id in Base:
    Data.append(id.strip('\n'))
len(Data)

"""Gerando a pontuação do Botometer para cada conta e guardando em uma lista"""

lista = list()
for screen_name, result in bom.check_accounts_in(Data):
  lista.append([screen_name, result])

lista

"""Criando uma lista para cada conta com informações sobre a pontuação """

dados = list()
for c in range(len(lista)):
  try:
    dados.append([lista[c][0]])
    dados[c].append(lista[c][1]['user']['user_data']['screen_name'])

    for valor in lista[c][1]['raw_scores']['universal'].values():
      dados[c].append(valor)
  
  except KeyError:
    print(f'User: {lista[c][0]}, Index: {c}')

dados2 = list()
for c in range(len(dados)):
  if len(dados[c]) != 1:
    dados2.append(dados[c])

colunas = ['id', 'screen_name', 'astroturf',	'fake_follower',	'financial',	'other',	'overall',	'self_declared',	'spammer']

df = pd.DataFrame(dados2, columns=colunas)

df.head()

from secret import *

"""Criando uma lista para cada conta com informações do perfil"""

ids = Data

json = list()

for i in range(len(ids)):
  try:
    json.append(api.get_user(user_id=ids[i])._json)
  
  except Exception as error:
    print(f'Error: {error.__class__}')

keys = ['id', 'screen_name', 'location','description', 'followers_count', 'friends_count', 'created_at', 'favourites_count', 'statuses_count']

value = list()
for i in range(len(json)):
    value.append([])
    value[i].append(json[i]['id_str'])
    value[i].append(json[i]['screen_name'])
    value[i].append(json[i]['location'])
    value[i].append(json[i]['description'])
    value[i].append(json[i]['followers_count'])
    value[i].append(json[i]['friends_count'])
    value[i].append(json[i]['created_at'])
    value[i].append(json[i]['favourites_count'])
    value[i].append(json[i]['statuses_count'])
        
print(value)

df2 = pd.DataFrame(value, columns = keys)

df2.head()

tweets = list()
aux = ''
for i in range(len(df2)):
  tweets.append([])

  try:
    for tweet in api.user_timeline(user_id=df2.id[i]):
      aux = aux + tweet._json['text'] + '\n'

  except Exception as error:
    print(error.__class__)

  else:
     tweets[i].append(aux)
     aux = ''

df2['time_line'] = tweets

"""Juntandos os dois datas Frames com informações sobre a pontuação e perfil"""

df['id']=df['id'].astype(str)

dados = pd.merge(df2, df, how = 'inner', on = ['id', 'screen_name'])

dados.head()

"""Salvando CSV

"""

dados.to_csv('Usuarios_xxx.csv', index=False)
