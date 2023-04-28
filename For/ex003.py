# Exercícios
# Calculando % de uma lista
#Faremos algo parecido com \"filtrar\" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso,
# mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.
# Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta,
# eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta,
# temos 30% dos vendedores que bateram a meta.

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcos', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

#  Vamos resolver de 2 formas:

#     "    1. Criando uma lista auxiliar apenas com os vendedores que bateram a meta
acima_meta = []

for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)

print(acima_meta)
print('{:.1%} dos vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))

#     "    2. Fazendo o cálculo diretamente na lista que já temos

qtde_vend_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        qtde_vend_acima += 1

print('{:.1%} dos vendedores bateram a meta'.format(qtde_vend_acima / len(vendas)))

melhor_vendedor = ''
maior_venda = 0

for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        melhor_vendedor = venda[0]
print('O melhor vendedor foi {} com {} vendas'.format(melhor_vendedor, maior_venda))