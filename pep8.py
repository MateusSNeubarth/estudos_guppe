"""
PEP8 - Python Enhancement Proposal

São estas, propostas de melhorias para a linguagem python

Zen of Python

import this

A ideia da pep8 é que possamos escrever códigos Python de forma Pythonica

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculos, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4


numero_impar: 3

[3] - Utilize 4 espaços para identação!;

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em bracno;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas ;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StrinType,
    ListType,
    SetType,
    Outrotype
)

# Imports devem ser colocados no topo do arquivo logo depois de quaiquer comentários ou doc string e
# antes de constantes ou variáveis globais.

[6] - Espaços em expreções e instruções

# Não faça:

funcao( algo[ 1 ], { outro : 2 } )

# Faça

funcao(algo[1], {outro:2})

# Não Faça

algo (1)

# Faça

algo(1)

# Não Faça

dict ['chave'] = lista [indice]

# Faça

dict['chave'] = lista[indice]

# Não Faça

x =              1
y =              3
variavel_longa = 4

# Faça

x = 1
y = 2
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha

"""
import this
