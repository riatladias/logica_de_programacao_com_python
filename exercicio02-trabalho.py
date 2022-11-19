print('Bem-vindo a Sorveteria do Riatla Dias')
# Iniciando as informações das opções do cardápio
print(42 * '-', 'Cardápio', 43 * '-')
print('| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print(95 * '-')

# Iniciando as variáveis
op_tamanho = ''
op_codigo = ''
sair = ''
valor_total = 0

while True:
    # input de dados das opções desejadas
    op_tamanho = input('Informe o TAMANHO do pote desejado (P/M/G): ')
    op_codigo = input('Informe o CÓDIGO do sabor do sorvete desejado (TR/ES/PR): ')

    # Verificação quanto ao tamanho e sabor desejado:
    if op_tamanho in 'pP' and op_codigo.upper() in 'TR':
        # TAMANHO P / SABOR TRADICIONAL
        valor_total += 6.00
        print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00')
        print('-' * 60)
    elif op_tamanho in 'pP' and op_codigo.upper() in 'ES':
        # TAMANHO P / SABOR ESPECIAL
        valor_total += 7.00
        print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00')
        print('-' * 60)
    elif op_tamanho in 'pP' and op_codigo.upper() in 'PR':
        # TAMANHO P / SABOR PREMIUM
        valor_total += 8.00
        print('Você pediu um sorvete sabor PREMIUM P de R$ 8,00')
        print('-' * 60)
    elif op_tamanho in 'mM' and op_codigo.upper() in 'TR':
        # TAMANHO M / SABOR TRANDICIONAL
        valor_total += 10.00
        print('Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00')
        print('-' * 60)
    elif op_tamanho in 'mM' and op_codigo.upper() in 'ES':
        # TAMANHO M / SABOR ESPECIAL
        valor_total += 12.00
        print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00')
        print('-' * 60)
    elif op_tamanho in 'mM' and op_codigo.upper() in 'PR':
        # TAMANHO M / SABOR PREMIUM
        valor_total += 14.00
        print('Você pediu um sorvete sabor PREMIUM M de R$ 14,00')
        print('-' * 60)
    elif op_tamanho in 'gG' and op_codigo.upper() in 'TR':
        # TAMANHO G / SABOR TRANDICIONAL
        valor_total += 18.00
        print('Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00')
        print('-' * 60)
    elif op_tamanho in 'gG' and op_codigo.upper() in 'ES':
        # TAMANHO G / SABOR ESPECIAL
        valor_total += 21.00
        print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00')
        print('-' * 60)
    elif op_tamanho in 'gG' and op_codigo.upper() in 'PR':
        # TAMANHO G / SABOR PREMIUM
        valor_total += 24.00
        print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00')
        print('-' * 60)
    else:
        # INPUT INVÁLIDO
        print('TAMANHO OU CÓDIGO INVÁLIDO(S) !!!!!')
        continue

    # Verificação de continuidade do programa
    sair = input('Deseja pedir mais alguma coisa? (S/N): ')
    if sair in 'sS':
        continue
    else:
        print('O total a ser pago é R$ {:.2f}'.format(valor_total))
        break
