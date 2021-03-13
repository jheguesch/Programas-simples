'''Atividade 4 - O restaurante “Mosca Frita” encomendou uma aplicação em Python console para efetuar a venda de seus produtos (pratos). 
Em uma entrevista com o dono do restaurante, ele explicou que precisa das seguintes funcionalidades: o programa deve exibir o
menu dos dias da semana versus os pratos principais que são servidos, conforme layout abaixo. Ao inserir o dia da semana 
(dom, qua, sex ou sab) deve ser exibido o prato relacionado bem como o seu valor, de acordo com a tabela abaixo. Ainda deve-se 
informar a quantidade de pratos que o cliente deseja comprar e exibir o valor a ser pago ao final. Como alguns clientes pedem 
desconto, é importante que o programa permita escolher se um desconto será concedido ou não. Caso o desconto seja concedido, o 
mesmo deverá ser informado pelo funcionário que estiver operando o programa; neste caso deverá ser exibido o valor do desconto 
e o novo valor a ser pago. Caso nenhum desconto seja concedido, deverá ser informado que não houve desconto. O programa também 
deverá tratar se for inserido algum dia da semana inválido.  
'''
print('*' * 50)
print('*                                                *')
print('             Restaurante Mosca Frita              ')
print('*                                                *')
print('*' * 50)
print('*                                                *')
print('*                                                *')
print('*    Escolha o cardápio que deseja visualizar    *')
print('*                                                *')
print('*  Dia          Prato principal          Opção   *')
print('* Domingo         Macarronada             Dom    *')
print('* Quarta           Feijoada               Qua    *')
print('* Sexta         Peixe Grelhado            Sex    *')
print('* Sábado           Churrasco              Sab    *')
print('*                                                *')
print('*' * 50)

opcao = str(input('Digite a opção desejada: '))
print('Opção escolhida:', opcao)


if opcao == 'Dom':
    print('Prato do dia: Macarronada')
    print('R$12.90')
    qtde = int(input('Quantidade: '))
    qtde = 12.90 * qtde
    print('Valor a ser pago: {:.2f}'.format(qtde))
    opcao_desc = str(input('\nDesconto ? (S/N): '))
    if opcao_desc == 'S':
        desc = int(
            input('Informe a taxa, em porcentagem, de desconto concedida: '))
        valor = ((0.01 * desc) * qtde)
        valor_final = qtde - valor
        print('\nValor do desconto: {:.2f}'.format(valor))
        print('Valor a ser pago: {:.2f}'.format(valor_final))

    elif opcao_desc == 'N':
        print('\nSem desconto')
        print('Valor a ser pago: {:.2f}'.format(qtde))


elif opcao == 'Qua':
    print('Prato do dia: Feijoada')
    print('R$15.50')
    qtde = int(input('Quantidade: '))
    qtde = 15.50 * qtde
    print('Valor a ser pago: {:.2f}'.format(qtde))
    opcao_desc = str(input('\nDesconto ? (S/N): '))
    if opcao_desc == 'S':
        desc = int(
            input('Informe a taxa, em porcentagem, de desconto concedida: '))
        valor = ((0.01 * desc) * qtde)
        valor_final = qtde - valor
        print('\nValor do desconto: {:.2f}'.format(valor))
        print('Valor a ser pago: {:.2f}'.format(valor_final))

    elif opcao_desc == 'N':
        print('\nSem desconto')
        print('Valor a ser pago: {:.2f}'.format(qtde))


elif opcao == 'Sex':
    print('Prato do dia: Peixe Grelhado')
    print('R$11.00')
    qtde = int(input('Quantidade: '))
    qtde = 11.00 * qtde
    print('Valor a ser pago: {:.2f}'.format(qtde))
    opcao_desc = str(input('\nDesconto ? (S/N): '))
    if opcao_desc == 'S':
        desc = int(
            input('Informe a taxa, em porcentagem, de desconto concedida: '))
        valor = ((0.01 * desc) * qtde)
        valor_final = qtde - valor
        print('\nValor do desconto: {:.2f}'.format(valor))
        print('Valor a ser pago: {:.2f}'.format(valor_final))

    elif opcao_desc == 'N':
        print('\nSem desconto')
        print('Valor a ser pago: {:.2f}'.format(qtde))


elif opcao == 'Sab':
    print('Prato do dia: Churrasco')
    print('R$14.30')
    qtde = int(input('Quantidade: '))
    qtde = 14.30 * qtde
    print('Valor a ser pago: {:.2f}'.format(qtde))
    opcao_desc = str(input('\nDesconto ? (S/N): '))
    if opcao_desc == 'S':
        desc = int(
            input('Informe a taxa, em porcentagem, de desconto concedida: '))
        valor = ((0.01 * desc) * qtde)
        valor_final = qtde - valor
        print('\nValor do desconto: {:.2f}'.format(valor))
        print('Valor a ser pago: {:.2f}'.format(valor_final))

    elif opcao_desc == 'N':
        print('\nSem desconto')
        print('Valor a ser pago: {:.2f}'.format(qtde))

else:
    print('\nOpção Invalida!!!')
