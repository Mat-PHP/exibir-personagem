import json
import random
import os

nomes = ['Artemis', 'Drako', 'Luna', 'Ragnar', 'Kira', 'Zephyr', 'Nova', 'Thorne']
habilidades = ['Fogo', 'Gelo', 'Raio', 'Vento', 'Cura', 'Invisibilidade', 'Teleporte', 'Força Bruta']

def gerar_personagem():
    personagem = {
        "nome": random.choice(nomes),
        "força": random.randint(50, 100),
        "defesa": random.randint(30, 90),
        "agilidade": random.randint(20, 80),
        "habilidade_especial": random.choice(habilidades)
    }
    return personagem

def salvar_personagem(personagem, arquivo='personagens.json'):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            dados = json.load(f)
    else:
        dados = []

    dados.append(personagem)

    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def exibir_personagens(arquivo='personagens.json'):
    if not os.path.exists(arquivo):
        print("Nenhum personagem salvo ainda.")
        return

    with open(arquivo, 'r') as f:
        personagens = json.load(f)
        for i, p in enumerate(personagens, 1):
            print(f"\nPersonagem {i}")
            for chave, valor in p.items():
                print(f"{chave.capitalize()}: {valor}")

# Execução
if __name__ == '__main__':
    print("Gerando personagem aleatório...")
    novo = gerar_personagem()
    print("Personagem criado:")
    print(novo)
    salvar_personagem(novo)
    print("\nLista de personagens salvos:")
    exibir_personagens()
