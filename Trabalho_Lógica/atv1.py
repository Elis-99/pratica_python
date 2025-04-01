print("Seja bem vindo (a) a loja da Elisangela Sena");

# Variáveis que recebem o valor do produto e a quantidade de produtos
produto1 = float(input('Digite o valor do produto 1: '));
qntProduto1 = int(input('Digite a quantidade do produto 1: '));

# Função que calcula o valor total da compra
def calculaCompra(produto1, qntProduto1):
    compra = produto1 * qntProduto1;
    return compra;

#Chamada da função que calcula o valor total da compra
total = calculaCompra(produto1, qntProduto1);

# Função que calcula o desconto
def calculaDesconto(total):
    if total < 2500:
        desconto = 0;
        return desconto;
    elif total >= 2500 and total < 6000:
        desconto = total * 0.04;
        return desconto;
    elif total >= 6000 and total < 10000:
        desconto = total * 0.07;
        return desconto;
    else:
        desconto = total * 0.11;
        return desconto;

#Chamada da função que calcula o desconto
totalDesconto = calculaDesconto(total);

#Cálculo do valor com desconto
valorDescontado = total - totalDesconto;
print ('O valor sem desconto é: ', total);
print ('O valor com desconto é: ', valorDescontado);
