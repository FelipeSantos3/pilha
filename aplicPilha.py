import pilha

tam=int(input("Digite o tamanho da pilha: "))
opc=1
while(opc!=9):
    opc=int(input("\n1-Empilhar \n2-Desempilhar \n3-Verificar se a pilha está cheia \n4-Verificar se a pilha está vazia \n9-Fim \nSelecione: "))
    if opc==1:
        n=1
        elementos.empilhar(n)
        elementos.mostrapilha()
    elif opc==2:
        print(elementos.desempilha())
        elementos.mostrapilha()
    elif opc==3:
        print(elementos.pilhacheia())
    elif opc==4:
        print(elementos.pilhavazia())
    elif opc==9:
        print("Saindo")
    else:
        print("Opção inválida")