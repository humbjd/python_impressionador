# -*- coding: utf-8 -*-
"""Módulo if - Aula 05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13k6FVPGiyEKVxTolg5U0lg_ORFDE4q2i

# Casos com várias condições/comparações

### Estrutura:

Quando temos várias comparações, ao invés de criar if dentro de if podemos usar os operadores "and" e "or" para tratar essas condições.

Funciona assim:

if condicao_1 and condicao_2:
    vai ser executado se as 2 condições forem verdadeiras ao mesmo tempo

outro caso:

if condicao_1 or condicao_2:
    vai ser executado se pelo menos uma das condições forem verdadeiras

### Exemplo

Vamos voltar ao exemplo de cálculo de meta de vendas dos funcionários. Muitas empresas atribuem bonificação do salário dos funcionários de acordo com o resultado do funcionário e também com o resultado da empresa como um todo.

Nesse caso, a regra funciona da seguinte forma:
- Se o funcionário vendeu mais do que a meta de vendas e a loja bateu a meta de vendas da loja, o funcionário ganha 3% do que ele vendeu em forma de bônus.
- Caso o funcionário tenha batido a meta de vendas individual dele, mas a loja não tenha batido a meta de vendas da loja como um todo, o funcionário não ganha bônus.
"""



"""### Outro exemplo

Agora vamos levar essa análise mais a fundo.

Nessa empresa, existe um outro caso também que garante que o funcionário ganhe um bônus, independente das vendas que ele fez naquele mês.

Todo mês os diretores da empresa fazem uma avaliação qualitativa de todos os funcionários. Nessa avaliação os diretores dão uma nota de 0 a 10 para cada funcionário. Se a nota do funcionário for 9 ou 10, ele também ganha o bônus de 3% do valor de vendas. (os bônus não são cumulativos)
"""


meta_fun = 5000
meta_not = 9
meta_loj = 15000

vend_fun = int(input('Digite a venda total do funcionário: '))
vend_loj = int(input('Digite a venda total da loja: '))
nota_fun = int(input('Qual a nota do funcionário: '))

if vend_fun >= meta_fun and vend_loj >= meta_loj:
        bonus = 0.03 * vend_fun
        print('Funcionário recebe bonus de {} %'.format(bonus))

elif vend_fun != meta_fun and vend_loj != meta_loj and nota_fun >= meta_not:
       bonus = 0.03 * vend_fun
       print('Através da nota {} esse funcionário irá receber R$ {} de bonus'.format(nota_fun, bonus))

else:
    print('Funcionário não recebe bonus')


