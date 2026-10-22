numero = int(input('Digite um número inteiro: '))

print('Escolha a base de conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:].upper()}')
else:
    print('Opção inválida. Tente novamente.')
    