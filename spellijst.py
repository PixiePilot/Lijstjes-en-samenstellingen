import _random
from random import *
import random
def spelprogramma(min,max):
    if max > 10:
        print('The max value allowed for the 2nd parameter is 10')
        return
    Spellijst = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
    random.shuffle(Spellijst)
    amount = (randint(min,max))
    print(Spellijst[0:amount])
    return
spelprogramma(3,11)
