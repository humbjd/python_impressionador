# Estrutura while:

### Funcionamento:
#Usamos o while quando queremos repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa.
#A lógica é: enquanto a condição for verdadeira, o while executa o código.
# Assim que ela terminar de ser verdadeira, o código \"sai\" do while.
venda = input('Registre um produto. \n'
                'Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')

vendas = []
# crie aqui seu programa
while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. \n'
                'Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia ')


print('Registro Finalizado. Os produtos cadastrados foram: {}'. format(vendas))


