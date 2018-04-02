#Nome: Guilherme Lenon da Silva;

'''=====Teste by Trustcode====='''

#Desafio 1

import random
num = list(range(1,301))
print(random.choice(num))

#Desafio 2
from random import sample
lista1 = sample(range(0, 5000000), 500)
lista2 = sample(range(0, 5000000), 50000)
listainter = list(set(lista1).intersection(lista2))
print(listainter)

'''
lista2 = [randint(0, 5000000) for x in range(50000)]
lista1 = [randint(0, 5000000) for x in range(500)]
lista3 = list(set(lista1).intersection(lista2))
print(lista3)
'''

#Desafio 3
nun = int(input("Digite um número: "))
indice = list(range(2, nun))
total = 0
for c in range(2, int((nun**0.5)+1)):
  if c in indice:
    for i in range(c**2, nun, c):
      if i in indice:
        indice.remove(i)
for j in range(1,nun +1):
    if nun % j == 0:
        total += 1
if total == 2:
    nun1 = [nun]
    print(indice + nun1)
else:
    print(indice)

# Desafio 4

word = (input('Digite uma palavra: '))
cont = 0
cont2 = 0
lista = [ord(c) for c in (word)]
soma = sum(lista)
for x in lista:
    if x <96:
        cont += 1
    else:
        cont2 += 1
ajuste1 = cont*38
ajuste2 = cont2*96
ajuste3 = (ajuste1 + ajuste2)
nun = (soma - ajuste3)
print(nun)
cont3 = 0
for j in range(1,nun +1):
    if nun % j == 0:
        cont3 += 1
if cont3 == 2:
    print('É uma palavra prima!')
else:
    print('Não é uma palavra prima!')




