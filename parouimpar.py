num = input('Digite um número inteiro: ')

if num.isnumeric():
    if int(num) % 2 == 0:
        print('Par')
    else:
        print('Impar')
else:
    print('Não é um número inteiro.')
