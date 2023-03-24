# -*- coding: utf-8 -*-
"""String Indice Negativo e Pedaço de Texto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g-0xQfysuzoVE8Q5bDi4dFwNo-E7sNwi

Texto: lira@gmail.com

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
  0   1   2   3   4  5  6  7  8  9 10 11 12 13

Para pegar um texto de trás para frente: texto[índice] -> onde índice é negativo
Para pegar o pedaço de um texto use : (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice]
"""

email = 'lira@gmail.com'
nome = 'João Paulo Lira'

print(email[:2])

"""Exercícios para Fixação:
Basta completar os prints de forma correta
"""

print('Tamanho do e-mail ' + str(len(email)) + ' caracteres')
print('Primeiro Caractere ' + email[0])
print('Último Caractere ' + email[13])
print('Servidor do email ' + email[5:])