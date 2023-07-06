import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

# Devolvendo o número de cartas contidos na classe   
deck = FrenchDeck()
print(len(deck))

# Explorando as funcionalidades do método __getitem__
print(deck[0])
print(deck[-1])

# Utilizando a função choice para obter cartas aleatoriamente
print(choice(deck))
print(choice(deck))
print(choice(deck))

# Como inspecionar as três primeiras cartas de um baralho novo
print(deck[:3])

# Como escolher somente os ases do baralho
# (iniciando da posição 12 do primeiro ás e então avançando de 13 em 13 cartas)
print(deck[12::13])

# Explorando o baralho como iterável
for card in deck:
    print(card)

# A iteração pode ser feita também na ordem reversa
for card in reversed(deck):
    print(card)