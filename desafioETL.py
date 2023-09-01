import pandas as pd
import requests
import json
import openai

#Extração de Dados (extrect)

data_frame = pd.read_csv('registroIDs.csv')
id_usuario = data_frame['UserID'].tolist()

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

def pegar_usuario(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

usuarios = [usuario for id in id_usuario if (usuario := pegar_usuario(id)) is not None]

#Transformação de Dados (Transform)

openai.api_key = 'Sua key para a api da openai (your openai key api)'

def gerador_noticiasIA(use):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
      {
        "role": "system", 
        "content": "Você é um especialista em mercado financeiro e investimentos."
       
       },
      {
        "role": "user", 
        "content": f"Crie uma mensagem para {usuario['name']} com dicas de investimento e compra e venda de ações. (máximo de 200 caracteres)"
        }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for usuario in usuarios:
  dicas =  gerador_noticiasIA(usuario)
  print(dicas)
  
#Carrgamento dos Dados (load)

def usuario_atualizado(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json= user)
  return True if response.status_code == 200 else False

for user in usuarios:
  success = usuario_atualizado(user)
  print(f"Usuario {user['name']} atualizado? {success}")