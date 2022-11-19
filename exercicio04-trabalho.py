# INÍCIO cadastrar_funcionario
def cadastrar_funcionario (id):
    print('-'*43, 'MENU CADASTRAR FUNCIONÁRIO', '-'*43)
    funcionario = {}
    print('Código do funcionario: {}'.format(id))
    funcionario['id'] = id
    funcionario['nome'] = input('Por favor informe o nome: ')
    funcionario['setor'] = input('Por favor informe o setor: ').upper()
    funcionario['salario'] = input('Por favor informe o salário: ')
    return funcionario

# INÍCIO consultar_funcionario
def consultar_funcionario(lista):
    print('-' * 43, 'MENU CONSULTAR FUNCIONÁRIO', '-' * 43)
    while True:
        print('Escolha a opção desejada:')
        print('1-Consultar TODOS funcionários\n2-Consultar funcionários por ID')
        print('3-Consultar funcionários por Setor\n4-RETORNAR')
        op = int(input('>>>'))
        if op == 1:
            # RETORNA TODOS FUNCIONÁRIOS
            for func in lista:
                print('-' * 15)
                for chave, valor in func.items():
                    print(f'{chave} : {valor}')
            print('-' * 15)
            continue

        elif op == 2:
            # RETORNA O FUNCIONÁRIO COM O ID INFORMADO
            id = int(input('Digite o ID do funcionário: '))
            for func in lista:
                print('-' * 15)
                if id == func['id']:
                    for chave, valor in func.items():
                        print(f'{chave} : {valor}')
            print('-' * 15)
            continue

        elif op == 3:
            # RETORNA O FUNCIONÁRIO COM O SETOR INFORMADO
            setor = input('Digite o SETOR do funcionário: ')
            for func in lista:
                print('-' * 15)
                if setor.upper() == func['setor']:
                    for chave, valor in func.items():
                        print(f'{chave} : {valor}')
            print('-' * 15)
            continue

        elif op == 4:
            return

# INÍCIO remover_funcionario
def remover_funcionario(lista):
    print('-' * 43, 'MENU REMOVER FUNCIONÁRIO', '-' * 43)
    id = int(input('Digite o ID do funcionário a ser removido: '))
    for func in lista:
        if id == func['id']:
            lista.remove(func)
            return

# menu_principal
lista_funcionario = []
id = 100

print('Bem-vindos ao controle de funcionários do Riatla Dias') # INICIO DO PROGRAMA
while True:
    print('*' * 100)
    print('-'*43, 'MENU PRINCIPAL', '-'*43)
    print('Escolha a opção desejada:')
    print('1-Cadastrar funcionário(a)\n2-Consultar funcionário(s)\n3-Remover funcionário(a)\n4-Sair')
    try:
        op = int(input('>>>'))
    except ValueError:
        print('!!! Valor informado incorreto, por favor digite novamente !!!')
    else:
        if op == 1:
            print('*' * 100)
            id += 1
            lista_funcionario.append(cadastrar_funcionario(id))
        elif op ==2:
            print('*' * 100)
            consultar_funcionario(lista_funcionario)
        elif op == 3:
            print('*' * 100)
            remover_funcionario(lista_funcionario)
        elif op == 4:
            print('*' * 100)
            print('-'*43, 'FIM DO PROGRMA', '-'*43)
            break
        else:
            print('!!! OPÇÃO INVÁLIDA !!!')
            continue
