"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python string é tudo que estiver entre:
- Aspas simples; Ex: 'Angelina Jolie'
- Aspas duplas; Ex: "Angelina Jolie"
- Aspas simples triplas; Ex: '''Angelina Jolie'''
"""
# - Aspas duplas triplas; Ex: """Angelina Jolie"""

#  Entrada de dados
# print("Qual seu nome?")
# nome = input()  # Input -> entrada
nome = input('Qual seu nome? ')
# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome.title())

# Exemplo de print 'moderno' 3.x
# print('Seja bem vinco(a) {0}' .format(nome))
# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome.title()}')

# print('Quantos anos você completa esse ano? ')
# idade = input()
idade = int(input('Quantos anos você completa esse ano? '))

# Processamento

# Saída
# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos' % (nome.title(), idade))

# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos de idade'.format(nome, idade))
# Exemplo de print 'mais atual' 3.7
print(f'{nome.title()} tem {idade} anos de idade')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro 
"""
print(f'{nome.title()} nasceu em {2022 - idade}')
