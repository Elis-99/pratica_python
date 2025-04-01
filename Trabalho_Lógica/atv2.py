print("Seja bem-vindo(a) a loja da Elisangela Sena")

total_pedido = 0  

#loop para pedir os produtos
while True:
    print("\nEscolha o sabor e o tamanho do seu açaí:");
    print("Sabores disponíveis:");
    print("CP - Cupuaçu\n");
    print("AC - Açaí\n");
    print("Tamanhos disponíveis:");
    print("P - Pequeno\n");
    print("M - Médio\n");
    print("G - Grande");

    #loop para validar o sabor
    while True:
        sabor = input("Digite o sabor desejado (CP --> Cupuaçu\n AC --> Açaí): ").upper()
        if sabor in ["CP", "AC"]:
            break
        else:
            print("Sabor inválido. Tente novamente.");

    #loop para validar o tamanho
    while True:
        tamanho = input("Digite o tamanho desejado (P/M/G): ").upper()
        if tamanho in ["P", "M", "G"]:
            break
        else:
            print("Tamanho inválido. Tente novamente.");

    #calcular o valor do pedido
    if sabor == "CP":
        if tamanho == "P":
            valor = 9.00
        elif tamanho == "M":
            valor = 14.00
        else:
            valor = 18.00
    elif sabor == "AC":
        if tamanho == "P":
            valor = 11.00
        elif tamanho == "M":
            valor = 16.00
        else:
            valor = 20.00

   
    total_pedido += valor  
    print(f"\nPedido registrado: Sabor {sabor}, Tamanho {tamanho}, Valor R${valor:}");

   #loop para continuar ou não
    while True:
        continuar = input("\nDeseja pedir mais alguma coisa? (S/N): ").upper()
        if continuar in ["S", "N"]:
            break
        else:
            print("Opção inválida. Digite S para sim ou N para não.");

    
    if continuar == "N":
        break

print(f"\nTotal do pedido: R${total_pedido:}");
