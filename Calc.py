while True:
    print("Digite SAIR em um dos números para sair do programa.")
    num1 = input("Digite um número: ")
    if num1 == "SAIR".lower() or "SAIR":
        break
    if not num1.isnumeric():
        print("POR FAVOR DIGITE APENAS NÚMEROS.")
        continue
    op = input("Digite o operador: ")
    num2 = input("Digite o segundo número: ")
    if not num2.isnumeric():
        print("POR FAVOR DIGITE APENAS NÚMEROS.")
        continue
    if num1 == "SAIR":
        break

    num1 = int(num1)
    num2 = int(num2)

    if op == '+':
        print(f'O resultado é: {num1 + num2}.')
    elif op == '-':
        print(f'O Resultado é {num1 - num2}.')
    elif op == '*':
        print(f'O Resultado é {num1 * num2}.')
    elif op == '/':
        print(f'O Resultado é {num1 / num2}.')
    else:
        print("Por favor digite uma das operações: -, +, * ou /")
