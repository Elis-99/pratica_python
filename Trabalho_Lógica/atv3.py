# função que seleciona o serviço
def escolha_servico():
    while True:
        servico = input('''\nServiços disponíveis:
DIG - Digitalização R$ 1,10 (por página)
ICO - Impressão Colorida R$ 1,00 (por página)
IPB - Impressão Preto e Branco R$ 0,40 (por página)
FOT - Fotocópia R$ 0,20 (por página)
        
Digite o serviço desejado (DIG/ICO/IPB/FOT): ''').lower();
        
        if servico in ['dig', 'ico', 'ipb', 'fot']:
            return servico
        
        # Se a opção não for válida, o loop continua
        print("Opção inválida. Por favor, escolha entre DIG, ICO, IPB ou FOT.");

# função que solicita o número de páginas e calcula o desconto
def num_pagina():
    """Solicita e valida o número de páginas, aplicando descontos"""
    while True:
        try:
            paginas = int(input("\nDigite o número de páginas: "));
            
            if paginas >= 20000:
                print("Não aceitamos pedidos com 20000 páginas ou mais.");
                continue
            elif paginas >= 2000:
                return paginas, 0.25;
            elif paginas >= 200:
                return paginas, 0.20;
            elif paginas >= 20:
                return paginas, 0.15;
            else:
                return paginas, 0;
        except ValueError:
            print("Por favor, digite um número válido.");

# função que solicita e valida serviços adicionais
def servico_extra():
    """Solicita e valida serviços adicionais"""
    while True:
        extra = input('''\nServiços extras:
1 - Encadernação simples (R$ 15.00)
2 - Encadernação de capa dura (R$ 40.00)
0 - Não desejo mais nada
        
Digite o serviço extra desejado (0/1/2): ''');
        
        if extra in ['0', '1', '2']:
            return int(extra)
        # Se a opção não for válida, o loop continua
        print("Opção inválida. Por favor, escolha entre 0, 1 ou 2.");
# função principal
def main():
    print("\nBem-vindo a copiadora - Desenvolvido por Elisangela Sena");
    
    
    # Pedido válido
    print("\n=== PEDIDO VÁLIDO ===");
    servico = escolha_servico();
    paginas, desconto = num_pagina();
    extra = servico_extra();
    
    # Cálculo principal (fora de funções)
    precos = {'dig':1.10, 'ico':1.00, 'ipb':0.40, 'fot':0.20}
    extras = {0:0.00, 1:15.00, 2:40.00}
    
    valor_servico = precos[servico] * paginas * (1 - desconto);
    valor_extra = extras[extra];
    total = valor_servico + valor_extra;
    
    print("\n=== RESUMO DO PEDIDO ===");
    print(f"Serviço escolhido: {servico.upper()}");
    print(f"Número de páginas: {paginas}");
    if desconto > 0:
        print(f"Desconto aplicado: {desconto*100:.0f}%");
    print(f"Serviço extra: {extra}");
    print(f"Valor total: R$ {total:.2f}");

if __name__ == "__main__":
    main();
    
    