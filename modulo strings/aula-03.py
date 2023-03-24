# -*- coding: utf-8 -*-
"""Operações com String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8Wj4GgryCVh_1ujmjNCLlJFQDkmdq7C

# Operações com String

str -> transforma número em string<br>
in -> verifica se um texto está contido dentro do outro<br>
operador + -> concatenar string<br>
format e {} -> substitui valores<br>
%s -> substitui textos<br>
%d -> substitui números decimais<br>

Vamos deixar uma cartilha para download
"""

faturamento = 1000
custo = 500
lucro = faturamento - custo




"""Uso do str() e do concatenar com +"""

print('O faturamento da loja foi de: ' + str(faturamento))

"""Uso do Format"""

print('O faturamento foi de: {}'.format(faturamento))

"""Uso do %s e %d"""

print ('O faturamento foi de: %d' % (faturamento))

"""Uso do in (mais exercícios práticos nas próximas aulas)"""

print('@' in 'lira@gmail.com')
print('@' in 'lira.gmail.com')

