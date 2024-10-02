pessoas_idades = {  "Jofre": '25', 
                    "Adair": 26,
                    "Carla": 22,
                    "Diego": 28,
                    "Fernanda": 27,
                    "Gabriel": 35,
                    "Helena": 24,
                    "Isabela": 29,
                    "Julia": 31,
                    "Lucas": 26
}

def pessoas_com_nome_j():
 
    pessoas_j = [nome for nome in pessoas_idades.keys() if nome.startswith("J")]
    return pessoas_j


resultado = pessoas_com_nome_j()
print("Pessoas cujo nome começa com a letra 'J':", resultado)