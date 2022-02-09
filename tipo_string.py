"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma String', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma String", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma String''', '''234''', '''a''', '''True''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas -> """uma String""", """234""', """a""", """True""", """42.3"""
"""
nome = 'Mateus'
print(nome)
print(type(nome))

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina \' Jolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

# [ 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14]
# ['M', 'a', 't', 'e', 'u', 's', ' ', 'N', 'e', 'u', 'b', 'a', 'r', 't', 'h']
nome = 'Mateus Neubarth'
print(nome[0:6])  # Slice de string

print(nome[7:15])  # Slice de string

# [ 0         1        ]
# ['Mateus', 'Neubarth'] 
print(nome.split()[0])

print(nome.split()[1])
"""
# - Estiver entre aspas duplas triplas -> """uma String""", """234""', """a""", """True""", """42.3"""
nome = 'Mateus Neubarth'

# [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])  # Inversão da String Pythônico

print(nome.replace('M', 'O'))

print(type(nome))

texto = 'Socorram me subino onibus em marrocos'  # Palíndromo
print(texto)

print(texto[::-1])
