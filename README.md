# 🚀 Portfólio de Sistemas Python

Coleção de sistemas desenvolvidos em Python para gestão comercial e serviços

## 📋 Índice de Projetos
1. [Loja de Produtos](#-loja-de-produtos)
2. [Loja de Açaí](#-loja-de-açaí)
3. [Sistema de Copiadora](#-sistema-de-copiadora)
4. [Gerenciador de Livros](#-gerenciador-de-livros)

---

## 🏪 Loja de Produtos
**Arquivo:** `loja_produtos.py`

### Funcionalidades
- Cálculo de preços por serviço:
  - 📄 Digitalização: R$ 1.10/página
  - 🖨️ Impressão Colorida: R$ 1.00/página
  - ⚫ Impressão P&B: R$ 0.40/página
  - 🖨️ Fotocópia: R$ 0.20/página

- **Descontos progressivos**:
  ```python
  if paginas >= 2000: 25%
  elif paginas >= 200: 20%
  elif paginas >= 20: 15%
🍇 Loja de Açaí
Arquivo: acai_shop.py

Cardápio
Tamanho	Preço
300ml	R$ 10
500ml	R$ 13
700ml	R$ 15
Complementos: Granola, Paçoca, Leite Ninho, Morango

📠 Sistema de Copiadora
Arquivo: copiadora.py

Fluxo do Sistema
Seleciona serviço

Informa quantidade de páginas

Escolhe extras:

🔖 Encadernação Simples (+R$15)

📘 Capa Dura (+R$40)

Gera relatório completo

📖 Gerenciador de Livros
Arquivo: biblioteca.py

Funcionalidades CRUD
python
Copy
# Estrutura de dados
{
    'id': 101,
    'titulo': 'Dom Casmurro',
    'autor': 'Machado de Assis',
    'editora': 'Martin Claret'
}
Operações:

➕ Cadastrar novo livro

🔍 Consultar por ID/Autor

❌ Remover registros

📜 Listar acervo completo

🛠 Como Executar
bash
Copy
# Para qualquer sistema
python nome_do_arquivo.py
📝 Requisitos
Python 3.8+

Nenhuma dependência externa

📌 Melhorias Futuras
Adicionar persistência em banco de dados

Implementar interface gráfica

Criar módulo de relatórios

Desenvolvido por Elisangela Sena


