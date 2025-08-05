
# Sistema Bancário - Estrutura Básica
# Desenvolvido para entrega 1: Estrutura e Funcionalidades Básicas

usuarios = {
    'admin': {'senha': 'admin123', 'tipo': 'admin'},
}

contas = {}

def menu_cliente(conta):
    while True:
        print(f"\n--- Menu Cliente: {conta} ---")
        print("1. Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Extrato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Saldo:", contas[conta]['saldo'])
        elif opcao == '2':
            valor = float(input("Valor para depositar: "))
            contas[conta]['saldo'] += valor
            contas[conta]['extrato'].append(f"Depósito: +{valor:.2f}")
        elif opcao == '3':
            valor = float(input("Valor para sacar: "))
            if contas[conta]['saldo'] >= valor:
                contas[conta]['saldo'] -= valor
                contas[conta]['extrato'].append(f"Saque: -{valor:.2f}")
            else:
                print("Saldo insuficiente.")
        elif opcao == '4':
            print("Extrato:")
            for item in contas[conta]['extrato']:
                print("-", item)
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Cadastrar nova conta")
        print("2. Bloquear conta")
        print("3. Desbloquear conta")
        print("4. Excluir conta")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            conta = input("Digite o número da nova conta: ")
            if conta in contas:
                print("Conta já existe.")
            else:
                senha = input("Digite a senha da nova conta: ")
                contas[conta] = {'senha': senha, 'saldo': 0.0, 'extrato': [], 'bloqueada': False}
                print("Conta criada com sucesso.")
        elif opcao == '2':
            conta = input("Conta a bloquear: ")
            if conta in contas:
                contas[conta]['bloqueada'] = True
                print("Conta bloqueada.")
            else:
                print("Conta não encontrada.")
        elif opcao == '3':
            conta = input("Conta a desbloquear: ")
            if conta in contas:
                contas[conta]['bloqueada'] = False
                print("Conta desbloqueada.")
            else:
                print("Conta não encontrada.")
        elif opcao == '4':
            conta = input("Conta a excluir: ")
            if conta in contas:
                if contas[conta]['saldo'] == 0:
                    del contas[conta]
                    print("Conta excluída.")
                else:
                    print("A conta possui saldo. Não pode ser excluída.")
            else:
                print("Conta não encontrada.")
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

def menu_principal():
    while True:
        print("\n--- MENU INICIAL ---")
        print("1. Cliente")
        print("2. Admin")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            conta = input("Número da conta: ")
            senha = input("Senha: ")
            if conta in contas and contas[conta]['senha'] == senha:
                if contas[conta].get('bloqueada', False):
                    print("Conta bloqueada. Procure o administrador.")
                else:
                    menu_cliente(conta)
            else:
                print("Conta ou senha incorretos.")
        elif opcao == '2':
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            if usuario in usuarios and usuarios[usuario]['senha'] == senha:
                menu_admin()
            else:
                print("Usuário ou senha incorretos.")
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

# Iniciar sistema
menu_principal()
