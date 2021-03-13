'''Atividade 2 - Elaborar uma aplicação console em Python que receba um número qualquer,
mostre as opções abaixo, de acordo com o escolhido, efetue o cálculo correspondente e mostre
o resultado. 
'''

n = int(input('Informe um número: \nOpções:\n1 - Raiz Quadrada\n2 - Quadrado\n3 - Cubo\n4 - Soma de todas as operações acima\nDigite sua opção: '))
num = int(input('Digite um valor para a operação: '))

if num <= 0:
    print('Número Negativo!')

elif n == 1:
    r = num ** (1/2)
    print('O resultado da operação é: {:.2f}'.format(r))

elif n == 2:
    q = num * 2
    print('O resultado da operação é: {}'.format(q))

elif n == 3:
    c = num ** 3
    print('O resultado da operação é: {}'.format(c))

elif n == 4:
    r = num ** (1/2)
    q = num * 2
    c = num ** 3
    s = r + q + c
    print('O resultado da soma das operações é: {:.2f}'.format(s))

else:
    print('Opção Invalida!')
