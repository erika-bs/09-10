from Biblioteca import Biblioteca

def menu():
    livros = Biblioteca()
    while True:
        print("\nBem-vindo a Biblioteca!")
        print("Escolha uma das opções abaixo, digitando o número correspondente:")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Remover Livro")
        print("4. Exibir lista de livros cadastrados")
        print("5. Pegar livro emprestado")
        print("6. Finalizar Emprestimo")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            livros.cadastrarLivro()
        elif escolha == '2':
            livros.cadastrarUsuario()
        elif escolha == '3':
            livros.removerLivro()
        elif escolha == '4':
            livros.exibirLivros()
        elif escolha == '5':
            livros.registrarEmprestimo()
        elif escolha == '6':
            livros.finalizarEmprestimo()
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()