print('Bem-vindo a loja do Riatla Dias')
# entrada de dados
valor_unitario = float(input('Informe o valor unitário do produto: '))
qtd_produto = int(input('Informe a quantidade de produtos: '))

# iniciando as variáveis
total_sem_frete = 0
total_com_frete = 0
valor_frete = 0

# Testando o valor do frete apartir da quantidade de produtos
if 0 <= qtd_produto < 11:
    # valor do frete R$30,00
    valor_frete = 30.00
    total_sem_frete = qtd_produto * valor_unitario
    total_com_frete = total_sem_frete + valor_frete
elif 11 <= qtd_produto < 101:
    # valor do frete R$60,00
    valor_frete = 60.00
    total_sem_frete = qtd_produto * valor_unitario
    total_com_frete = total_sem_frete + valor_frete
elif 101 <= qtd_produto < 1001:
    # valor do frete R$120,00
    valor_frete = 120.00
    total_sem_frete = qtd_produto * valor_unitario
    total_com_frete = total_sem_frete + valor_frete
else:
    # valor do frete R$240,00
    valor_frete = 240.00
    total_sem_frete = qtd_produto * valor_unitario
    total_com_frete = total_sem_frete + valor_frete

# Saída de dados / exibição dos resultados
print('O valor sem frete foi: R$ {:.2f}'.format(total_sem_frete))
print('O valor com frete foi: R$ {:.2f} (valor do frete R$ {})'.format(total_com_frete, valor_frete))
