# carol
desafio carta super trufo
import random

class Carta:
    def __init__(self, nome, caracteristicas, super_trunfo=False):
        self.nome = nome
        self.caracteristicas = caracteristicas
        self.super_trunfo = super_trunfo
    
    def __str__(self):
        return f'{self.nome} - {self.caracteristicas}'

class Jogo:
    def __init__(self, cartas):
        self.cartas = cartas
        self.mesa = []

    def embaralhar_cartas(self):
        random.shuffle(self.cartas)
    
    def distribuir_cartas(self):
        # Distribuir as cartas entre dois jogadores
        self.jogador1 = self.cartas[:len(self.cartas)//2]
        self.jogador2 = self.cartas[len(self.cartas)//2:]
    
    def escolher_caracteristica(self, carta_jogador, carta_adversario):
        print(f'\nEscolha a característica da carta para desafiar:')
        for idx, caracteristica in enumerate(carta_jogador.caracteristicas):
            print(f'{idx + 1}. {caracteristica[0]}')
        
        escolha = int(input("\nEscolha uma característica pelo número: ")) - 1
        valor_jogador = carta_jogador.caracteristicas[escolha][1]
        valor_adversario = carta_adversario.caracteristicas[escolha][1]

        print(f'\nVocê escolheu {carta_jogador.caracteristicas[escolha][0]} ({valor_jogador})')
        print(f'O adversário escolheu {carta_adversario.caracteristicas[escolha][0]} ({valor_adversario})')

        return valor_jogador, valor_adversario
    
    def jogar(self):
        self.embaralhar_cartas()
        self.distribuir_cartas()
        
        while self.jogador1 and self.jogador2:
            carta_jogador1 = self.jogador1.pop(0)
            carta_jogador2 = self.jogador2.pop(0)
            
            print(f'\nCarta do Jogador 1: {carta_jogador1.nome}')
            print(f'Carta do Jogador 2: {carta_jogador2.nome}')
            
            if carta_jogador1.super_trunfo:
                print('Jogador 1 tem o Super Trunfo! Ele ganha a rodada!')
                self.jogador1.append(carta_jogador1)
                self.jogador1.append(carta_jogador2)
                continue
            if carta_jogador2.super_trunfo:
                print('Jogador 2 tem o Super Trunfo! Ele ganha a rodada!')
                self.jogador2.append(carta_jogador1)
                self.jogador2.append(carta_jogador2)
                continue
            
            # Escolher característica
            valor_jogador1, valor_jogador2 = self.escolher_caracteristica(carta_jogador1, carta_jogador2)
            
            if valor_jogador1 > valor_jogador2:
                print(f'\nJogador 1 ganhou a rodada!')
                self.jogador1.append(carta_jogador1)
                self.jogador1.append(carta_jogador2)
            elif valor_jogador2 > valor_jogador1:
                print(f'\nJogador 2 ganhou a rodada!')
                self.jogador2.append(carta_jogador1)
                self.jogador2.append(carta_jogador2)
            else:
                print(f'\nEmpate! As cartas são devolvidas aos jogadores.')
                self.jogador1.append(carta_jogador1)
                self.jogador2.append(carta_jogador2)
            
            print(f'Cartas do Jogador 1: {len(self.jogador1)} | Cartas do Jogador 2: {len(self.jogador2)}')
        
        if len(self.jogador1) > len(self.jogador2):
            print("\nJogador 1 venceu o jogo!")
        else:
            print("\nJogador 2 venceu o jogo!")

# Definir algumas cartas para o jogo
cartas = [
    Carta("Ferrari", [("Velocidade", 350), ("Potência", 800), ("Preço", 250000)]),
    Carta("Lamborghini", [("Velocidade", 340), ("Potência", 780), ("Preço", 240000)]),
    Carta("Porsche", [("Velocidade", 330), ("Potência", 700), ("Preço", 220000)]),
    Carta("Tesla", [("Velocidade", 300), ("Potência", 500), ("Preço", 90000)]),
    Carta("Bugatti", [("Velocidade", 400), ("Potência", 1000), ("Preço", 300000)]),
    Carta("McLaren", [("Velocidade", 360), ("Potência", 850), ("Preço", 280000)]),
    Carta("Super Carro", [("Velocidade", 1000), ("Potência", 1000), ("Preço", 1000000)], super_trunfo=True)
]

# Iniciar o jogo
jogo = Jogo(cartas)
jogo.jogar()
