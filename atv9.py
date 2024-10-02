pessoas_idades = {  "Jofre": 25, 
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

def pessoa_mais_nova():
    try:
        
        idades_convertidas = {nome: int(idade) for nome, idade in pessoas_idades.items()}
        pessoa = min(idades_convertidas, key=idades_convertidas.get)
        return pessoa, idades_convertidas[pessoa]
    except ValueError:
        return "Há um valor inválido no dicionário de idades."
    except Exception as e:
        return str(e)


resultado = pessoa_mais_nova()
if isinstance(resultado, tuple):
    nome, idade = resultado
    print(f"A pessoa mais nova é {nome} com {idade} anos.")
else:
    print(resultado)