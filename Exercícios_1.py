'''Atividade 1 - Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente? 
'''

a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print(a)
print(b)

# Resposta: B) a será 2 e b será 1
