#Formas de alinhamento

#Delimitar um número de espaços

nome = input('Digite seu nome: ')
print('Olá {:10}!'.format(nome))

#Alinhar na direita

print('Olá {:>10}!'.format(nome))

#Alinhar na esquerda

print('Olá {:<10}!'.format(nome))

#Alinhar ao centro

print('Olá {:^10}!'.format(nome))

#Escrever nos espaços

print('Olá {:=^10}!'.format(nome))
print('Olá {:/>10}!'.format(nome))
print('Olá {:*>10}!'.format(nome))


#Fazendo a soma de dois números em uma linha
print('A soma vale {}'.format(int(input('Digite um número: ')) + int(input('Digite outro número: '))))

#Colocar dois prints na mesma linha > end=''
print('Ola', end=' ')
print('Mundo')

#Para quebrar as linhas > \n
print('Ola \n Mundo')
