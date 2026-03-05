from _pydatetime import datetime
from datetime import datetime


menu ="""
    1 - Realizar Deposito;
    2 - Operação de Saque;
    3 - Imprimir Extrato Bancário;
    4 - Sair.
    Digite a opção desejada:
    
=> """

saldo = 0
extrato_bancario = ""
total_depositos = 0
total_saques = 0
numero_saques = 0
valor_limite = 500 # Limite por saque.
LIMITE_SAQUES = 10 # Limite de saques por dia. # Transações

print("\nBem vindo ao autoatendimento BankDIO!")

while True:
    print("Menu - Selecione a opção desejado.")
    opcoes_menu = input(menu)
    if opcoes_menu == "1":
        valor = float(input("Informe o valor a ser depositado: R$ "))
        if valor > 0:
                saldo += valor
                total_depositos += valor
                data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                extrato_bancario += (f'Depósito: R$ {valor:.2f} - {data_hora}\n') # Concateno a string e coloco no extrato.
                print(f'Deposito realizado com sucesso: R$ {valor:.2f} - {data_hora}\n')
        else:
                print("Valor inválido, tente novamente mais tarde!")
    elif opcoes_menu == "2":
        valor = float(input("Valor do saque: R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > valor_limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Saldo é insuficiente para está operação.")
        elif excedeu_limite:
            print(f"O limite por saque é de R${valor_limite:.2f}. Caso necessite de valores maiores entre em contato com seu gerente.")
        elif excedeu_saques:
            print("Número máximo de saques foi excedido. Tente novamente amanhã.")
        elif valor > 0:
            saldo -= valor
            total_saques += valor
            numero_saques += 1
            data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            extrato_bancario += (f'Saque: {valor:.2f} - {data_hora}\n')
        else:
            print('Opção inválida, tente novamente.')
    elif opcoes_menu == "3":
        valor_atual = total_depositos - total_saques
        print('\n--------------- EXTRATO ---------------')
        print('Não foram realizadas movimentações.' if not extrato_bancario else extrato_bancario)
        print(f'Total de depósitos: R$ {total_depositos:.2f}')
        print(f'Total de saques: R$ {total_saques:.2f}')
        print(f'\nSaldo atual: R$ {valor_atual:.2f}')
        print('--------------- EXTRATO ---------------\n')
    elif opcoes_menu == "4":
        print("Obrigado por utilizar nossos serviços, até logo!")
        break
    else:
        print("Opção inválida, por favor selecione as opções disponíveis!")