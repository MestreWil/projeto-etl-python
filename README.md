# Projeto de ETL - Explorando IA Generativa em um Pipeline de ETL com Python

Este repositório contém o código e os recursos para um projeto de ETL (Extração, Transformação e Carregamento) chamado "Explorando IA Generativa em um Pipeline de ETL com Python", desenvolvido como parte do Bootcamp Santander Ciência de Dados com Python.

## Objetivo do Projeto

O objetivo deste projeto é criar um pipeline de ETL que envia mensagens personalizadas para 3 usuários cadastrados em uma API Restful. O processo é dividido em três etapas principais:

1. **Extração (E)**: Utilizamos uma API Restful fornecida pelo Bootcamp para cadastrar 3 usuários. Em seguida, criamos um arquivo CSV contendo os números de registro de cada usuário.

2. **Transformação (T)**: Utilizamos a biblioteca Pandas em um arquivo Python para ler o arquivo CSV, validar se os usuários existem na API e armazenar os dados desses usuários em uma estrutura de dados chamada "usuarios".

3. **Geração de Mensagens Personalizadas (T)**: Utilizamos a API do ChatGPT 3.5 para gerar mensagens personalizadas de 200 caracteres sobre dicas de investimento, incorporando os dados de cada usuário nas mensagens.

4. **Carregamento (L)**: Enviamos as mensagens personalizadas de volta para a API Restful.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
/
├── src/
│   ├── desafioETL.py            # Script Python que realiza as operações de ETL
│
├── data/
│   ├── registroIDs.csv      # Arquivo CSV com os números de registro dos usuários
│
├── README.md             # Este arquivo README
```

## Observações

Este projeto é uma demonstração simplificada de um pipeline de ETL com foco na utilização da IA generativa do ChatGPT 3.5 para criar mensagens personalizadas. Certifique-se de adaptar o projeto às suas necessidades específicas e configurar as APIs conforme necessário.

## Autor

Este projeto foi desenvolvido por William Tavares de Moura.

[Bootcamp Santander Ciência de Dados com Python](https://www.santander.com.br/institucional/servicos-para-voce/educacao/bootcamps/bootcamp-santander-ciencia-de-dados-com-python)
