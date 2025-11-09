class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return f"{self.titulo} por {self.autor}"
    
    def __repr__(self):
        return f"Livro('{self.titulo}', {self.autor}, {self.paginas})"
    
    def __len__(self):
        return self.paginas
    
    def __eq__(self, outro):
        return self.titulo == outro.titulo and self.autor == outro.autor

# Usar a classe
livro1 = Livro("Python Fluente", "Luciano Ramalho", 800)
livro2 = Livro("PHP Fluente", "Luciano Ramalho", 800)

print(livro1) # Usa __str__
print(repr(livro1)) # Usa __repr__
print(f"Páginas: {len(livro1)}") # Usa __len__
print(f"Livros iguais? {livro1 == livro2}") # Usa __eq__