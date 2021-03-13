'''Atividade 3 - Elaborar uma aplicação console em Python que receba o código correspondente ao cargo de um
funcionário e seu salário atual. Após realizar o cálculo de reajuste, a aplicação deverá mostrar o cargo, o
valor do aumento e seu novo salário. Caso seja digitado um código diferente dos possíveis, enviar
mensagem de “Código Inválido”.
'''

codigo = int(input('Informe um código: \nOpções:\n10 - Ajudante\n20 - Pedreiro\n30 - Mestre de Obras\n40 - Arquiteto\n50 - Engenheiro\nDigite a sua opção: '))
salario = float(input('Digite o seu salário atual: '))

if codigo == 10:
    ajudante = salario + (salario * 0.40)
    print('\nO seu cargo é Ajudante.\nO valor do aumento é de 40%\nO seu salario atual é de {:.2f}'.format(
        ajudante))

elif codigo == 20:
    pedreiro = salario + (salario * 0.35)
    print('\nO seu cargo é Pedreiro.\nO valor do aumento é de 35%\nO salario atual é de {:.2f}'.format(
        pedreiro))

elif codigo == 30:
    mestre = salario + (salario * 0.30)
    print('\nO seu cargo é Mestre de Obras.\nO valor do aumento é de 30%\nO seu salario atual é de {:.2f}'.format(
        mestre))

elif codigo == 40:
    arquiteto = salario + (salario * 0.25)
    print('\nO seu cargo é Arquiteto.\nO valor do aumento é de 25%\nO seu salario atual é de {:.2f}'.format(
        arquiteto))

elif codigo == 50:
    print('\nO seu cargo é Engenheiro.\nNão tem aumento!')

else:
    print('Código Invalido!')
