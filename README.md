# univespcandidatovaga
Programa para consultar a relação entre candidatos inscritos e vagas disponíveis para o vestibular da UNIVESP no primeiro semestre de 2020.

#### Dependências
Para instalar todas as dependências para o proejto, baixe-o e execute o seguinte comando na em sua raiz: `pip install -r requirements.txt`

#### Requisitos
O projeto foi desenvolvido com Python na versão 3.

#### Como utilizar
Para utilizar o programa é muito simples, após baixá-los e configura-lo confirme descrito acima, acesse o a raiz do projeto utilizando algum terminal linha de comando de sua preferência e digite o comando: `py app.py`

Feito isso, o programa será executado, e nesse momento será solicitado duas informações, o POLO e o EIXO DE ESTUDO que deseja consultar.

Ao lhe ser perguntado sobre o POLO que deseja consultar, com a pergunta  **INFORME O(S) POLO(S)**. Basta informar o nome da cidade que deseja consultar o(s) polo(s), separando-os por vírgula e sem espaço, da seguinte forma: `RIBEIRAO PRETO,SERTAOZINHO,CRAVINHOS`. Ou simplesmente deixe em branco para consultar todos os polos.

Na sequência, lhe será perguntado qual o EIXO DE ESTUDO deseja realizar a consulta, com a pergunta **INFORME O(S) EIXO(S) DE ESTUDO**. Basta informar o eixo de estudo, sendo duas opções possíveis, 1 para EIXO DE COMPUTAÇÃO e 2 para EIXO DE LICENCIATURA. Ou simplesmente deixe em branco para consultar todos os polos.

Feito isso o sistemas irá recuperar os polos e os candidatos incritos do site da UNIVESP. Em seguida os dados serão formatados, processados e na sequência serão retornados os dados da consulta para o(s) polo(s) e eixo(s) solicitado(s) da sguinte forma: 

INFOME O(S) POLO(S):

`RIBEIRAO PRETO`

INFORME O(S) EIXO(S) DE ESTUDO:

`1`

Recuperando polos...

Recuperando inscritos...

Formatando dados dos polos extraídos da UNIVESP

Formatando dados dos inscritos extraídos da UNIVESP

Processando a concorrência entre candidatos inscritos no vestibular UNIVESP 2020


**O polo de RIBEIRAO PRETO recebeu 330 inscrições para o EIXO DE COMPUTAÇÃO para 100 vagas. Isso representa uma corrência média de 3.3 candidato por vaga.**