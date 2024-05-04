menu = f"""
    ========== MENU ==========

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    ==========================

    Insira sua opção aqui: """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f} \n"
            print(f"Depósito de R${valor_deposito} realizado com sucesso!")

        else:
            print("Valor inválido. Tente novamente inserindo um valor válido para o depósito.")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor que deseja sacar: "))
        
        if valor_saque > saldo:
            print("Saldo insuficiente. Tente novamente.")

        elif valor_saque > limite:
            print(f"Valor limite de saque de R${limite} ultrapassado. Tente novamente.")

        elif num_saques >= LIMITE_SAQUES:
            print(f"Limite de {LIMITE_SAQUES} saques diários ultrapassado. Volte amanhã!")

        elif valor_saque > 0:
            num_saques += 1
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f} \n" 
            print(f"Saque de R${valor_saque} realizado com sucesso!")

        else:
            print("Valor inválido. Tente novamente inserindo um valor válido para o saque.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Nenhuma operação foi realizada." if not extrato else extrato)
        print(f"\nSaldo da conta: R${saldo:.2f}")
        print("=============================")

    elif opcao == "0":
        print("Obrigado pela preferência!")
        break

    else:
        print("Opcão inválida. Tente novamente selecionando uma das opções listadas no menu.")