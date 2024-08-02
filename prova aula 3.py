#Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave.
#  Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. 
# Por fim, exiba o valor total da compra.

contador=0
lista={}

def adicionar_produtos(nome,preco):
    produto={'nome':nome,
             'preço':preco}
    lista.append(produto)

for i in range(5):
    nome=input(f'digite o nome do produto {i+1}: ')
    preco=float(input(f'digite o preço do produto {i+1}: '))
    contador+=preco
    adicionar_produtos(nome,preco)
print(lista)

print(f'vc comprou: {lista} e a soma de tudo deu: {contador}')