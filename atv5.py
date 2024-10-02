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

def remover_pessoa(nome):
    if nome in pessoas_idades:
        del pessoas_idades[nome]
        print(f"{nome} foi removido(a) do dicionário.")
    else:
        print("Nome não encontrado.")

remover_pessoa("Diego")
print(pessoas_idades)