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

def calcular_media_idades():
    try:
        total_idades = sum(int(idade) for idade in pessoas_idades.values())
        numero_pessoas = len(pessoas_idades)
        if numero_pessoas > 0:
            media = total_idades / numero_pessoas
            return media
        else:
            return "Não há pessoas no dicionário."
    except ValueError:
        return "Há um valor inválido no dicionário de idades."


media_idades = calcular_media_idades()
print(f"A média das idades é {media_idades:.2f}")