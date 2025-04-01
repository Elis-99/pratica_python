lista_livro = [];
id_global = 0

# Função para cadastrar livro
def cadastrar_livro(id_livro):
    nome = input("Digite o nome do livro: ");
    autor = input("Digite o autor do livro: ");
    editora = input("Digite a editora do livro: ");
    #objeto livro: onde ficam as informações do livro
    livro = {
        'id': id_livro,
        'nome': nome,
        'autor': autor,
        'editora': editora
    };

    #adiciona o livro na lista de livros
    lista_livro.append(livro);
    print("Livro cadastrado com sucesso!");

# Função para consultar livros
def consultar_livro():
    """Menu de consulta de livros"""
    while True:
        print("\nOpções de consulta:");
        print("1. Consultar Todos");
        print("2. Consultar por Id");
        print("3. Consultar por Autor");
        print("4. Retornar ao menu");
        
        # Seleção da opção
        opcao = input("Escolha a opção desejada: ");
        
        if opcao == '1':
            print("\nTodos os livros cadastrados:");
            for livro in lista_livro:
                print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}");
        
        elif opcao == '2':
            id_busca = int(input("Digite o ID do livro: "));
            encontrado = False;
            for livro in lista_livro:
                if livro['id'] == id_busca:
                    print(f"\nLivro encontrado:");
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}");
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado!");
        
        elif opcao == '3':
            autor_busca = input("Digite o nome do autor: ");
            encontrados = [livro for livro in lista_livro if livro['autor'].lower() == autor_busca.lower()];
            
            if encontrados:
                print(f"\nLivros do autor {autor_busca}:");
                for livro in encontrados:
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Editora: {livro['editora']}");
            else:
                print("Nenhum livro encontrado para este autor.");
        
        elif opcao == '4':
            return
        
        else:
            print("Opção inválida!");

# Função para remover livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "));
            
            for i, livro in enumerate(lista_livro):
                if livro['id'] == id_remover:
                    lista_livro.pop(i);
                    print("Livro removido com sucesso!");
                    return
            
            print("ID inválido! Livro não encontrado.");
        except ValueError:
            print("Por favor, digite um número válido para o ID.");

# Lista vazia e variável id_global
lista_livro = [];
id_global = 0

def main():
    global id_global  # Declaração da variável global
    
    print("Bem-vindo ao Sistema de Gerenciamento de Livros - Desenvolvido por Elisangela Sena");

    # Menu principal
    while True:
        print("\nMenu Principal:");
        print("1. Cadastrar Livro");
        print("2. Consultar Livro");
        print("3. Remover Livro");
        print("4. Encerrar Programa");
        
        opcao = input("Escolha a opção desejada: ");
        
        if opcao == '1':
            id_global += 1
            cadastrar_livro(id_global);
        
        elif opcao == '2':
            consultar_livro();
        
        elif opcao == '3':
            remover_livro();
        
        elif opcao == '4':
            print("Encerrando o programa...");
            break
        
        # Caso a opção seja inválida
        else:
            print("Opção inválida!");

if __name__ == "__main__":
    main();