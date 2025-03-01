# -*- coding: utf-8 -*-
"""Meu primeiro passo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13FondjSSL3Z3WhSG5chk_NRRPCRcsYVu

Operadores Aritméticos
"""

# Adição
10 + 2

# Subtração
10 - 2

#Divisão
10 / 2

#Multiplicação
10 * 2

#Divisão Inteira
10 // 2

# Resto da divisão
10 % 2

#Potenciação
10 ** 2

"""  Operadores Relacionais"""

# Menor
10 < 2

# Menor ou igual
10 <= 2

# Maior ou igual
10 >= 2

# Igual
10 == 10

# Diferente
10 != 10

"""Operadores Lógicos
  - AND
  - OR
  - NOT

-Tabela da Verdade



      AND
"""

print (10 < 2 and 4 < 6)
print (10 > 2 and 4 > 6)
print (10 < 2 and 4 > 6)
print (10 < 2 and 4 < 6)

"""**Variáveis**



Variáveis estão alocadas nos espaços de memória.
"""

# Nome da variável é ''X'' que armazena o valor de 10 em um espaço de memória.
x = 5
print(x) # Utilizar a referencia no nome atribuído

[12]  x = 5
      print('O valor de x é ', x)

print(' O valor de x é', x, 'e o dobro é', x * 2)

nome = 'Rafael Vargas'
print(nome)

print('EU,', nome, 'tirei', x * 2, 'na prova de phyton')

"""Input
* Armazenar a informação digitada pelo usuário em uma variável.
* o Dado armazenado sempre será um texto
"""

nome = input ("Digite o nome do usuário") #aguarda até o usuário digitar algo
print(nome)

valor = input('Digite o valor do produto:')
print(valor)

valor = input("Digite a nota")
print(nome, 'sua nota foi', valor)

valor_convert = int(valor)
desconto = valor_convert -5
print(desconto)

"""Condicional

"""

# If
if 5 > 10:
  print('Verdade')

# if/else
num1 = 10
num2 = 5
if num1 > num2:
  print('O num1 é o maior número')

else:
  print( 'O num2 é o maior número')

#If / Elif/ Else
num1 = 10
num2 = 10
if num1 > num2:
    print ('O num1 é o maior número')
elif num1 < num2:
    print('O num2 é o maior número')
else:
    print('Os dois são iguais')

"""CONDICIONAL COM NÚMEROS LÓGICOS"""

num1 = 10
num2 = 5
num3 = 2
if (num1 > num2) and (num1 > num3):
  print ('O num1 é o maior número')
else:
  print ('O num1 não é o maior número')

"""Listas, tuplas e dicionários"""

lista = [5, 'Rafael', 8.9]

type(lista)

lista.append('Rafael') #Adicionar um elemento na lista

print(lista)
print(lista[1])

tupla =(5, 'Rafael', 8.9)

type(tupla)

print(tupla)

dicionario = {'nome':'Rafael', 'idade':26, 'nota':8.9}

type(dicionario)

print(dicionario)

print(dicionario['nome'])

"""Estrutura de repetição

**FOR
"""

# FOR RANGE
for contador in range(10):
    print (contador)

# for range + break
for contador in range(1000):
    print(contador)
    if contador == 5:
        break

lista = ['Teste1', 'Teste2']

# For Simples
for val in lista:
  print(val)

#for com Enumerate
for i, val in enumerate(lista):
  print(i, val)

lista2 = [2,3,4]

for val in lista2:
  val += 1
  print(val)

for val in lista2:
  val *= 2
  print(val)

"""While"""

val = 1
while (val <6):
        val *=2
        print(val)

#While com else
val = 4
while val <10:
  val *=2
else:
  print('Valor de val é: ', val)