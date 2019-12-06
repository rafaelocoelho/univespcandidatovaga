from core import functions as fn

print('PESQUISAR A RELAÇÃO DE CANDIDATO/VAGA DA UNIVESP PARA O VESTIBULAR PRIMEIRO SEMESTRE DE 2020.\n')
print('PARA PROSSEGUIR, INFORME O(S) POLO(S) QUE DESEJA CONSULTAR SEPARADO(S) POR VIRGULA OU DEIXE EM BRANCO PARA PESQUISAR TODOS: \n EX. RIBEIRÃO PRETO, SERTÃOZINHO, ETC\n')
print('EM SEGUIDA, INFORME O EIXO DE ESTUDO OU DEIXE EM BRANCO PARA PESQUISAR TODOS: \n\n 1 - COMPUTAÇÃO \n 2 - LICENCIATURA\n\n')

polos_de_interesse = input('INFOME O(S) POLO(S): \n')
eixos_de_estudo = input('INFORME O(S) EIXO(S) DE ESTUDO: \n')

polos_de_interesse = [] if not polos_de_interesse else str(polos_de_interesse).split(',')
eixos_de_estudo = [] if not eixos_de_estudo else fn.retornar_eixos_de_estudo(str(eixos_de_estudo).split(','))

print('Recuperando polos...')
lista_vagas = fn.extrair_dados_pagina('https://univesp.br/noticias/univesp-abre-inscricoes-para-o-vestibular-na-proxima-terca-feira-15-slash-10')

print('Recuperando inscritos...')
lista_inscritos = fn.extrair_dados_pagina('http://vestibular.univesp.br/3nGhChKn3_Homologados/db/UNIVESP-homologados.json?_=1575494061661', True)

if (True, True) == (lista_vagas.get('status'), lista_inscritos.get('status')):

    if lista_inscritos:
        print('\nFormatando dados dos polos extraídos da UNIVESP')
        polos = fn.formatar_dados_polos_univesp(lista_vagas.get('dados'), polos_de_interesse)
        
    if lista_inscritos:
        print('Formatando dados dos inscritos extraídos da UNIVESP')
        polos = fn.formatar_dados_inscritos_univesp(lista_inscritos.get('dados'),eixos_de_estudo, polos)

    if polos:
        print('Processando a concorrência entre candidatos inscritos no vestibular UNIVESP 2020\n')
        resultado = fn.retornar_relacao_candidato_vaga(polos, eixos_de_estudo)

        print(resultado)

else:
    print('Não foi possível acessar os dados')
    