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

def atualizar_idade(nome, nova_idade):
    if nome in pessoas_idades:
        pessoas_idades[nome] = nova_idade
        print(f"A idade de {nome} foi atualizada para {nova_idade}.")
    else:
        print("Nome não encontrado.")


atualizar_idade("Carla", 23)
atualizar_idade("Jofre", 22)
print(pessoas_idades)