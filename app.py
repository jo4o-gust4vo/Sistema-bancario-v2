def menu():
    menu = '''
            \n ===================MENU===================

                    [D] - DEPOSITO
                    [S] - SAQUE
                    [E] - EXTRATO
                    [RU] - REGISTRAR USUÁRIO
                    [CC] - CRIAR CONTA
                    [LC] - LISTAR CONTAS
                    [Q] - SAIR
                    
    >>'''

    return input(menu)


def deposito(saldo, extrato, valor_depositado, /):
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f'o Valor depositado: R$ {valor_depositado:.2f} \n'
        print('Deposito realizado com sucesso!')
    else:
        print('operação inválida.')
    return saldo, extrato


def saque(*, saldo, extrato, valor_de_saque, limite_de_saque, numero_de_saque, limite_numero_saque):
    excedeu_saldo = valor_de_saque > saldo
    excedeu_limite = valor_de_saque > limite_de_saque
    excedeu_numero_saque = numero_de_saque > limite_numero_saque
    if excedeu_saldo:
        print('Operação inválida, pois o valor de saque é maior que o valor do saldo.')
    elif excedeu_limite:
        print('valor de saque excedido do limite.')
    elif excedeu_numero_saque:
        print('Quantidade de saque excedido do limite.')
    elif valor_de_saque > 0:
        saldo -= valor_de_saque
        extrato += f'Valor de saque: R$ {valor_de_saque:.2f}\n'
        numero_de_saque += 1
        print('Saque realizado com sucesso!')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print('Não foram realizadas movimentações.') if not extrato else print(extrato)
    print(f'Saldo atual: {saldo} \n')
    print("\n================+++++++++================")


def verifica_usuario(cpf, usuarios):
    for indice, i in enumerate(usuarios):
        if cpf == usuarios[indice]['CPF']:

            return cpf,usuarios[indice]['nome']
        else:

            return None


def criar_usuarios(usuarios):
    cpf = int(input('Digite o CPF a ser cadastrado: '))
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print('O usuário já existe.')
        return
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite o data de nascimento: dd/mm/aaaa: ')
    endereco = input('Digte o seu endereço: ')
    usuarios.append(
        {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'endereco': endereco,
            'CPF': cpf
        }
    )

    print('Usuário criando com sucesso.')




def criar_conta(agencia, numero_conta, usuarios,contas):
    cpf = int(input('Digite o CPF: '))
    usuario, nome_conta = verifica_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso.')
        contas.append(
            {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': nome_conta
            }
        )
    print('Usuário não encontrado.')

def listar_consta(contas):

    if not contas:
        print('================================================= ')
        print('Nenhuma conta foi localizado em nossos registros.\n')
        return
    else:
        for indice, conta in enumerate(contas):
            card_conta = f'''
=================================================    
Agencia: {contas[indice]['agencia']}
Conta: {contas[indice]['numero_conta']}
usuario: {contas[indice]['usuario']}         
================================================     
                 \n  
            '''

            print(card_conta)


def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'
    extrato = ''
    limite = 500
    numero_de_saque = 0
    usuarios = []
    contas = []
    saldo = 0
    while True:
        opcao = menu()

        if opcao == 'D':
            valor = float(input('Digite o valor de deposito: '))
            saldo, extrato = deposito(saldo, extrato, valor)

        elif opcao == 'S':
            valor = float(input('Digite o valor de saque: '))
            saldo, extrato = saque(
                saldo=saldo,
                extrato=extrato,
                valor_de_saque=valor,
                limite_de_saque=limite,
                numero_de_saque=numero_de_saque,
                limite_numero_saque=LIMITE_SAQUE

            )
        elif opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'RU':
            criar_usuarios(usuarios)

        elif opcao == 'CC':
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == 'LC':
            listar_consta(contas)
        elif opcao == 'Q':
            break

        else:
            print('Algo deu errado. Tente novamente.')


main()
