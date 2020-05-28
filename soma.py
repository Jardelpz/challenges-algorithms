tamanho = int(input('Digite o tamanho do array '))
#print(tamanho)
i = 0
lista = []
soma=0


for i in range(tamanho):
    print(f'a {i} a {tamanho}')
    value = int(input('Qual o número? '))
    soma+=value
    lista.append(value)
else:
    print(f'Array: {lista}. Totalizando {soma}')

