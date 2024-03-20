opcao_de_operacao = 0

while opcao_de_operacao != 5:
    print("Selecione o número para a operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - multiplicaçao\n4 - Divisão\n5 - Sair")
    
    opcao_de_operacao = int(input("Digite sua opção(1/2/3/4/5): "))
    
    if opcao_de_operacao == 5:
        print("Você saiu da calculadora")
        break
    
    numero1 = int(input("Digite o primeiro número para operaçao: "))
    numero2 = int(input("Digite o segundo número para operação: "))
    
    if opcao_de_operacao == 1:
        print(f"{numero1} + {numero2} =", numero1 + numero2)
    elif opcao_de_operacao == 2:
        print(f"{numero1} - {numero2} =", numero1 - numero2)
    elif opcao_de_operacao ==  3:
        print(f"{numero1} x {numero2} =", numero1 * numero2)
    elif opcao_de_operacao == 4:
        print(f"{numero1} / {numero2} =", numero1 / numero2)