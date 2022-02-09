"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java:

for(int i = 0 < 10; i++){
    //execução do loop
}

Python

for item in iteravel:
    //execução do loop



Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Mateus Neubarth'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range[1, 10]

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)


Enumerate:

((0, 'M'), (1, 'a'), (2, 't'), (3 'e')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor podemos descartá-lo utilizando um underline (_)

nome = 'Mateus Neubarth'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print('A soma é', soma)

nome = 'Mateus Neubarth'
for letra in nome:
    print(letra, end='')

Tabela de emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode

"""

# Original: U+1F621
# Modificado: U0001F621

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F621' * num)
