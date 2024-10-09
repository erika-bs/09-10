from datetime import date

dataAtual = date.today()

class Livro:
    def __init__(self,titulo,autor,isbn,disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidade = disponibilidade

    def __str__(self):
        return f"\n--------------------\nTítulo:{self.titulo}\nAutor:{self.autor}\nISBN:{self.isbn}\n-------------------"

class Usuario:
    def __init__(self,nome,id,email):
        self.nome = nome
        self.id = id
        self.email = email

    def __str__(self):
        return f"Nome:{self.nome}\nId:{self.id}\nEmail:{self.email}"
    
class Emprestimo(Usuario):
    def __init__(self,nome,id,email,dataEmprestimo,dataDevolucao):
        super().__init__(nome,id,email)
        self.dataEmprestimo = dataEmprestimo
        self.dataDevolucao = dataDevolucao

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = {}
        self.lastId = 0

    def cadastrarLivro(self):
        titulo = input("Digite o nome o livro:")
        autor = input("Digite o nome do autor:")
        isbn = input("Digite o código isbn:")

        if titulo in self.livros:
            print(f"O {titulo} já foi cadastrado")
        else:
            self.livros[titulo] = Livro(titulo,autor,isbn,disponibilidade=True)
            print(f"\n-----------------------Livro cadastrado com sucesso!\nTítulo:{titulo}\nAutor:{autor}\nISBN:{isbn}\n-----------------------")

    def removerLivro(self):
        titulo = input("Qual nome do livro que vc deseja remover?")

        if titulo in self.livros:
            del self.livros[titulo]
            print(f"{titulo} removido com sucesso!")
        else:
            print(f"{titulo} não encontrado")

    def exibirLivros(self):
        if not self.livros:
            print("\n-----------------------\nNenhum livro cadastrado.\n-----------------------")
        else:
            for livro in self.livros.values():
                print(livro)

    def cadastrarUsuario(self):
        nome = input("Qual seu nome:")
        email = input("Digite seu email:")

        if email in self.usuarios:
            print(f"{nome} já está cadastrado")
        else:
            self.lastId += 1
            self.usuarios[email] = Usuario(nome,self.lastId,email,)
            print(f"Usuário {nome.upper()} cadastrado com sucesso!")

    def registrarEmprestimo(self):
        titulo = input("Qual livro gostaria de pegar emprestado?")
       
        if titulo in self.livros:
            livro = self.livros[titulo]
            if livro.disponibilidade:
                email = input("Digite seu email cadastrado: ")
                if email in self.usuarios:
                    usuario = self.usuarios[email]
                    livro.disponibilidade = False
                    emprestimo = Emprestimo(usuario, livro, dataAtual)
                    self.emprestimos[titulo] = emprestimo  
                    print(f"Empréstimo iniciado em {dataAtual}.")
                else:
                    print("Usuário não cadastrado. Cadastre-se primeiro.")
            else:
                print("Livro está emprestado no momento.")
        else:
            print("Livro não encontrado.")

    def finalizarEmprestimo(self):
        titulo = input("Qual livro você deseja devolver? ")

        if titulo in self.emprestimos:
            emprestimo = self.emprestimos[titulo]
            emprestimo.livro.disponibilidade = True
            emprestimo.dataDevolucao = date.today()
            del self.emprestimos[titulo]
            print(f"Empréstimo do livro {titulo} finalizado com sucesso.")
        else:
            print("Livro não encontrado entre os empréstimos.")