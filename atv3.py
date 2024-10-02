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

def obter_idade(nome):
    return pessoas_idades.get(nome, "Nome não encontrado")


nome_digitado = input("Digite o nome da pessoa: ")
print(f"A idade de {nome_digitado} é {obter_idade(nome_digitado)}")