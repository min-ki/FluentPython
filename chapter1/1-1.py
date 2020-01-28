import collections
from random import choice

# collections.namedtuple() 을 이용해 개별 카드를 나타내는 클래스를 구현
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

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()

print(len(deck))
print(deck[0])
print(deck[1])

print(choice(deck))

# 파이썬 데이터 모델
# 사용자가 표준 연산 수행을 위해 클래스 자체에서 구현한 임의 메서드명을 암기할 필요 없다.
# 파이썬 표준 라이브러리에서 제공하는 풍부한 기능을 별도로 구현할 필요 없이 바로 사용할 수 있다.

print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# dict을 선언하는 방법
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

# python3에서는 기본적으로 object를 상속받는다.
# FrenchDeck 은 불변객체

# 특별 메서드는 파이썬 인터프리터가 호출하기 위한 것
# 사용자 정의 속성을 만들 때에는 앞뒤로 이중 언더바를 가 형태의 속성명은 피하라.


