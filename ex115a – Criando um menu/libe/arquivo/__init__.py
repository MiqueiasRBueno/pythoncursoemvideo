from io import TextIOWrapper
from typing import Any, IO

from libe.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('Pessoas Cadastrada')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<33} {dado[1]:>3} anos')
    finally:
        a.close()
        
        

def cadastrar_usuario(nome, name, idade):
    """Cadastra um novo usuário em um arquivo."""
    try:
        a = open(nome, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f"{name};{idade}\n")  # Escreve os dados no arquivo
            print(f"Usuário {name} cadastrado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao cadastrar: {e}")
       
