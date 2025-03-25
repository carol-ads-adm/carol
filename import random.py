import random

# Definição das cartas
cartas = [
    {"nome": "Dragão", "força": 9, "velocidade": 7, "inteligência": 6},
    {"nome": "Fênix", "força": 8, "velocidade": 9, "inteligência": 7},
    {"nome": "Grifo", "força": 7, "velocidade": 8, "inteligência": 8},
    {"nome": "Minotauro", "força": 9, "velocidade": 6, "inteligência": 5},
    {"nome": "Centauro", "força": 6, "velocidade": 9, "inteligência": 7}
]

# Distribuir cartas para os jogadores
random.shuffle(cartas)
jogador1_cartas = cartas[:len(cartas)//2]
jogador2_cartas = cartas[len(cartas)//2:]

# Jogo
while jogador1_cartas and jogador2_cartas:
    carta1 = jogador1_cartas.pop(0)
    carta2 = jogador2_cartas.pop(0)
    
    print(f"Jogador 1: {carta1['nome']} - {carta1}")
    print(f"Jogador 2: {carta2['nome']} - {carta2}")
    
    atributo = input("Escolha um atributo (força, velocidade, inteligência): ").strip().lower()
    
    if atributo not in carta1:
        print("Atributo inválido! Perde a rodada.")
        jogador2_cartas.append(carta2)
        jogador2_cartas.append(carta1)
    elif carta1[atributo] > carta2[atributo]:
        print("Jogador 1 venceu esta rodada!")
        jogador1_cartas.append(carta1)
        jogador1_cartas.append(carta2)
    elif carta1[atributo] < carta2[atributo]:
        print("Jogador 2 venceu esta rodada!")
        jogador2_cartas.append(carta2)
        jogador2_cartas.append(carta1)
    else:
        print("Empate! As cartas voltam para o final do deck.")
        jogador1_cartas.append(carta1)
        jogador2_cartas.append(carta2)
    
    print(f"Cartas restantes - Jogador 1: {len(jogador1_cartas)} | Jogador 2: {len(jogador2_cartas)}")
    print("-" * 40)

# Verificando o vencedor final
if jogador1_cartas:
    print("Jogador 1 venceu o jogo!")
else:
    print("Jogador 2 venceu o jogo!")
