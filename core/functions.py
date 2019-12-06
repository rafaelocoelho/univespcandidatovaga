import requests

from requests.exceptions import HTTPError
from unidecode import unidecode
from bs4 import BeautifulSoup

def extrair_dados_pagina(endereco, json = False):
    
    error = []
    resultado = {
        'status': False,
        'mensagem': 'Não foi possível acessar a página especificada.',
        'dados': ''
    }

    try:
        response = requests.get(endereco)
    except HTTPError as http_error:
        error.append(http_error)
    except Exception as exception:
        error.append(exception)
    
    if(len(error)):
        resultado.update({
            'status': False,
            'mensagem': ' \n'.join(error),
            'dados': ''
        }) 

    elif response.status_code==200:
        resultado.update({
            'status': True,
            'mensagem': 'Dados extraídos com sucesso!',
            'dados': response.json() if json else response.content
        })

    return resultado

def retornar_eixos_de_estudo(opcoes = []):

    resultado = []
    eixos_de_estudo = {
        1: 'EIXO DE COMPUTAÇÃO',
        2: 'EIXO DE LICENCIATURA'
    }

    for (indice, eixo) in eixos_de_estudo.items():
        # print(str(indice), opcoes)
        if str(indice) in opcoes:
            resultado.append(eixo)

    return resultado


def formatar_dados_polos_univesp(dados, polos = []):
    
    soup = BeautifulSoup(dados, 'html.parser')
    
    linhas = soup.find_all('tr')

    linhas = linhas[1:len(linhas)-2]

    resultado = {}
    
    for linha in linhas:
        linha = linha.find_all('td')

        polo = linha[0].get_text().upper()
        polo = unidecode(polo)
        
        vagas = {
            'LICENCIATURA': int(linha[2].get_text()),
            'COMPUTACAO': int(linha[3].get_text())
        }

        if len(polos) > 0:
            if polo in map(lambda x:x.upper(), polos):
                resultado.__setitem__(polo, {
                    'EIXO DE COMPUTAÇÃO': {
                        'VAGAS': vagas.get('COMPUTACAO'),
                        'INSCRITOS': []
                    },
                    'EIXO DE LICENCIATURA': {
                        'VAGAS': vagas.get('LICENCIATURA'),
                        'INSCRITOS': []
                    }
                })
        else:
            resultado.__setitem__(polo, {
                'EIXO DE COMPUTAÇÃO': {
                    'VAGAS': vagas.get('COMPUTACAO'),
                    'INSCRITOS': []
                },
                'EIXO DE LICENCIATURA': {
                    'VAGAS': vagas.get('LICENCIATURA'),
                    'INSCRITOS': []
                }
            })
        

    return resultado


def formatar_dados_inscritos_univesp(registros, eixo_de_estudo = [], polos = {}):

    for registro in registros.get('RECORDS'):
       
        polo = unidecode(registro.get('Polo_1').upper())        

        if len(eixo_de_estudo) > 0:
            if registro.get('Eixo') in eixo_de_estudo and polo in polos:
                polos.get(polo).get(registro.get('Eixo').upper()).get('INSCRITOS').append(registro.get('Inscricao')) 
                
        elif polo in polos:
            polos.get(polo).get(registro.get('Eixo').upper()).get('INSCRITOS').append(registro.get('Inscricao')) 

    return polos


def retornar_relacao_candidato_vaga(polos, eixos_de_estudo = []):

    resultado = []

    for (polo, registros) in polos.items():
        for (eixo, dados) in registros.items():
            
            if len(eixos_de_estudo) > 0:
                if eixo in eixos_de_estudo:

                    inscritos = len(dados.get('INSCRITOS'))
                    vagas = dados.get('VAGAS')
                    media = round(inscritos/vagas,2)

                    resultado.append(retorna_mensagem(polo, inscritos, eixo, vagas, media))

            else:
                
                inscritos = len(dados.get('INSCRITOS'))
                vagas = dados.get('VAGAS')
                media = round(inscritos/vagas,2)

                resultado.append(retorna_mensagem(polo, inscritos, eixo, vagas, media))


    return ''.join(resultado)


def retorna_mensagem(polo, inscritos, eixo, vagas, media):

    return f"O polo de {polo} recebeu {inscritos} inscrições para o {eixo} para {vagas} vagas. Isso representa uma corrência média de {media} candidato por vaga.\n"