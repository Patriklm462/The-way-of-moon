class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f"{self.nome} ({self.nacionalidade})"
    
    class Livro:
        def __init__(self, titulo, autor, isbn):
            self.titulo = titulo
            self.autor = autor
            self.isbn = isbn
            self.disponivel = True

        def adicionar(self, biblioteca):
            biblioteca.append(self)
            print(f'O livro "{self.titulo}" de {self.autor} foi adicionado à biblioteca.')

        def buscar(self, titulo=None, autor=None):
            if titulo and titulo.lower() in self.titulo.lower():
                return self
            if autor and autor.lower() in self.autor.nome.lower():
                return self
            return None

        def emprestar(self):
            if self.disponivel:
                self.disponivel = False
                print(f'O livro "{self.titulo}" foi devolvido.')
            else:
                print(f'O livro "{self.titulo}" já está na biblioteca.')

    class Usuario:
        def __init__(self, nome, usuario_id):
            self.nome = nome
            self.usuario_id = usuario_id
            self.livros_emprestados = []

        def emprestar_livro(self, livro):
            if livro.emprestar():
                self.livros_emprestados.append(livro)

        def devolver_livro(self, livro):
            if livro in self.livros_emprestados:
                livro.devolver()
                self.livros_emprestados.remove(livro)
            else:
                print(f'O usuário "{self.nome}" não possui o livro "{livro.titulo}".')

        def criar_biblioteca():
            biblioteca = []
            return biblioteca

        def adicionar_livros(biblioteca):
            autor1 = Autor("Gabriel García Márquez", "Colombiano")                    
            autor2 = Autor("Jane Austen", "Britânica")                    
            autor3 = Autor("Haruki Murakami", "Japonês")                    
            autor4 = Autor("Agatha Christie", "Britânica")

            livro1 = livro1  ("Cem Anos de Solidão", autor1, "9780307474728")                    
            livro2 = livro2 ("Orgulho e Preconceito", autor2, "9780141439518")                    
            livro3 = livro3 ("Kafka à Beira-Mar", autor3, "9788535917554")                    
            livro4 = livro4 ("O Assassinato de Roger Ackroyd", autor4, "9788550302873")

            livro1.adicionar(biblioteca)                    
            livro2.adicionar(biblioteca)    
            livro3.adicionar(biblioteca)    
            livro4.adicionar(biblioteca)

        def interagir_com_usuario():
            biblioteca = biblioteca()

            adicionar_livros = (biblioteca)

            usuario1 = usuario1("Ana Costa", 101)
            usuario2 = usuario2("Carlos Silva", 102)

            livro_encontrado = biblioteca[0].buscar(titulo = "Cem Anos de Solidão")
            if livro_encontrado:
                usuario1.emprestar_livro(livro_encontrado)

                livro_encontrado = biblioteca[1].buscar(titulo = "Orgulho e Preconceito")
            if livro_encontrado:
                usuario2.emprestar_livro(livro_encontrado)

            usuario1.devolver_livro(livro_encontrado)
            usuario2.devolver_livro(livro_encontrado)





