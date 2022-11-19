# Iniciando as funções
def metragem_limpeza(): # Avaliação do valor por metragem
    print(42 * '-', 'Menu 1 de 3 - Metragem da limpeza', 43 * '-')
    while True:
        try: # validação dos input
            metragem = float(input('Informe a metragem da residência: '))
        except ValueError:
            print('!! Valor digitado é inválido, tente novamente !!')
        else:
            if 30 <= metragem < 300:
                # Metragem da casa entre 30m² e 300m²
                print('Será necessário(a) um(uma) funcionário(a) para a limpeza')
                valor_metragem = 60 + 0.3 *  metragem
                return valor_metragem
            elif 300 <= metragem < 700:
                # Metragem da casa entre 300m² e 700m²
                print('Seram necessários(as) dois(duas) funcionários(as) para a limpeza')
                valor_metragem = 120 + 0.5 * metragem
                return valor_metragem
            else:
                # Não são aceitos
                print('!! Não aceitamos casa com metragem menor que 30m² ou maior que 700m² !!')
                continue

def tipo_limpeza(): # Avaliação de tipo de limpeza e valor
    print(42 * '-', 'Menu 2 de 3 - Tipo de limpeza', 43 * '-')
    while True:
        print('B - Básica - Indicada para sujeiras semanais ou quinzenais')
        print('C - Completa - Indicada para sujeiras antigas e/ou não rotineiras')
        opcao = input('Informe qual o tipo mais encaixa-se a usa necessidade: ')
        if opcao in 'bB':
            # TIPO B
            print('Você selecionou a limpeza BÁSICA')
            tipo = 1.00
            return tipo
        elif opcao in 'cC':
            # TIPO C
            print('Você selecionou a limpeza COMPLETA')
            tipo = 1.30
            return tipo
        else:
            # VALORES INVÁLIDOS
            print('!!! Opção inválida !!!')
            continue

def adicional_limpeza(): # Verificação de serviços adicionais
    print(42 * '-', 'Menu 3 de 3 - Adicional de limpeza', 43 * '-')
    adicionais = 0
    while True:
        print('Deseja mais algum adicional? ')
        print('0 - Não desejo mais nada (ENCERRAR)')
        print('1 - Passar 10 peças de roupas - R$10,00')
        print('2 - Limpeza de 1 Forno/Micro-ondas - R$12,00')
        print('3 - Limpeza de 1 Geladeira/Freezer - R$20,00')
        opcao = int(input('>>> '))
        if opcao == 1:
            adicionais += 10.00
        elif opcao == 2:
            adicionais += 12.00
        elif opcao == 3:
            adicionais += 20.00
        elif opcao == 0:
            # Encerrar o programa
            return adicionais
        else:
            # VALOR INVÁLIDO
            print('!!! OPÇÃO INVÁLIDA !!!')

# Programa principal
print('Bem-vindo ao programa de Serviços de limpeza do Riatla Dias')
print(60 * ' *')
valor_metragem = metragem_limpeza()
print(60 * ' *')
tipo = tipo_limpeza()
print(60 * ' *')
adicional = adicional_limpeza()
print(60 * ' *')
total = (valor_metragem * tipo) + adicional
print('TOTAL R$ {:.2f} (metragem: R$ {:.2f} * tipo: {}) + adicionais: R$ {:.2f}.'.format(total, valor_metragem, tipo, adicional ))
print(60 * ' *')
