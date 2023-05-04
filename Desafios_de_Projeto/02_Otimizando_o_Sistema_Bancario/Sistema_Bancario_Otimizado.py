import textwrap

def menu():
    menu = """\n
    ==============================   MENU  ============================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    [nu]\tNovo Usuario
    [nc]\tNova Conta
    [lc]\tLista de contas
    ===================================================================
    Comando => """
    return input(textwrap.dedent(menu))
        
def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('\n Deposito realizado com sucesso !')
    
    else:
        print('\nOperação falhou! O valor informado é invalido.')
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('\n Operação falhou! Você não tem saldo suficiente.')

    elif excedeu_limite:
        print('\n Operação falhou! Você não tem limite suficiente.')

    elif excedeu_saques:
        print('\n Operação falhou! NUmero maximo de saques excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso !')

    else:
        print('\n Operação falhou! O valor informado é inválido.')

    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
    print("============================== EXTRATO ==============================")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================================================")

def criar_usuario(usuarios):

    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Ja existe usuario com esse CPF: ')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, N - bairro - cidade/ sigla estado)')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuario registrado com sucesso !')

def filtrar_usuarios(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input('informe o CPF do usuario: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n Usuario não encontrado, fuluxo de criação de conta encerrado: ')
    return None


def listar_contas(contas):
    
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Tiitular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do deposito: '))
    
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Opção invalida, por favor selicione novamente um opção válida.')

main()