# Questao 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}'

Carro = Carro("bugarri", "preto", 2023)
print(Carro)

# Questao 2
class Restaurante:
    def __init__(self, nome, categoria, endereco, ativo=False, estrelas=5, capacidade=150):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.ativo = ativo
        self.estrelas = estrelas
        self.capacidade = capacidade

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Estrelas: {self.estrelas}, Capacidade: {self.capacidade}"
    
# Questao 4
def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}"

restaurante1 = Restaurante('Costa', 'Restaurante e Lanchonete', 'R. xv de Novembro, 1666 - Centro', capacidade=250)
print(restaurante1)

# Questao 3
restaurante1 = Restaurante('Costa', 'Restaurante e Lanchonete')
restaurante1.endereco = 'R. xv de Novembro, 1666 - Centro'
restaurante1.capacidade = 250
print(restaurante1)

# Construtor
restaurante2 = Restaurante('10 Pasteis', 'Brasil')
print(restaurante2)


# Questao 5
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

cliente1 = Cliente('Pedro', 'pedro.fracaro.martim@escola.pr.gov.br', '0 0000-0000', 'Atras do Fanatico')
cliente2 = Cliente('Camila', 'camila.zanella@escola.pr.gov.br', '0 0000-0000', 'Próximo a panificadora')
cliente3 = Cliente('Maria Eduarda', 'maria.eduarda@escola.pr.gov.br', '0 0000-0000', 'nfrente ao mato')

print(cliente1)
print(cliente2)
print(cliente3)