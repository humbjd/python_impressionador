# -*- coding: utf-8 -*-
"""Listas 07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OOCpziQ_tLP8JkLJb7dRvDNuaSG5N9R0

# Print de Listas

2 Opções:
- print "normal"
- método join -> texto.join(lista)
"""

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
print(produtos)

# \n é o botão equivalente ao ENTER no teclado
print('\n'.join(produtos))

print('\n - '.join(produtos))

"""Lembrando do método split de strings:

lista = texto.split(separador)
"""

produtos = 'apple tv, mac, iphone x, iphone 11, IPad, apple watch, mac book, airpods'

lista = produtos.split(', ')

print(lista)