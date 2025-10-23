opcao = ""

while opcao != 0:
    print ("Menu de opções:")
    print ("1 - Cadastrar nova peça")
    print ("2 - Listar peças aprovadas/reprovadas")
    print ("3 - Remover peça cadastrada")
    print ("4 - Listar caixas fechadas")
    print ("5 - Gerar relatório final")
    print ("0 - Para Sair do sistema")

    opcao = input ("Digite a opção desejada: ")
    if opcao == "1":
        print ("-------------")
        print ("UniFECAF")
        print ("-------------")
    elif opcao == "2":
        print ("-------------")
        print ("Algoritmos")
        print ("-------------")
    elif opcao == "3":
        print ("-------------")
        print ("Leonid")
        print ("-------------")
    elif opcao == "4":
        print ("-------------")
        print ("Aprovado")
        print ("-------------")
    elif opcao == "0":
        print ("-------------")
        print ("Sistema encerrado!")
        print ("-------------")
        exit()
    else:
        print ("-------------")
        print ("Opção inválida, tente novamente...")
        print ("-------------")