pessoas_idades = {  "Jofre": 25, 
                    "Adair": 26,
                    "Carla": 22,
                    "Diego": 28,
                    "Fernanda": 27,
                    "Gabriel": 35,
                    "Helena": 24,
                    "Isabela": 29,
                    "Luan": 31,
                    "Lucas": 26
}

def pessoa_mais_velha():
    if pessoas_idades:
        pessoa = max(pessoas_idades, key=pessoas_idades.get)
        return pessoa, pessoas_idades[pessoa]
    else:
        return "O dicionário está vazio."


nome, idade = pessoa_mais_velha()
print(f"A pessoa mais velha é {nome} com {idade} anos.")