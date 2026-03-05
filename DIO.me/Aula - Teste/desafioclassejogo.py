class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()
        
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "arte marcial",
            "ninja": "shuriken"
        }

        self.descricao_ataque = ataques.get(self.tipo, "fez um ataque desconhecido")

    
    def atacar (self):
        print(f'O {self.tipo} {self.nome} atacou usando sua {self.descricao_ataque}')

heroi_mago = Heroi("Merlin", 150, "Mago")
print(f"O {heroi_mago.nome} da classe {heroi_mago.tipo} atacou usando: {heroi_mago.descricao_ataque}")
heroi_mago.atacar()

heroi_guerreiro = Heroi("Conan", 35, "Guerreiro")
print(f"O {heroi_guerreiro.nome} da classe {heroi_guerreiro.tipo} atacou usando: {heroi_guerreiro.descricao_ataque}")
heroi_guerreiro.atacar()