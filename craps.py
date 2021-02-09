#!/usr/bin/env python
__author__ = "Arana Fireheart"

from die import *

firstRoll = True
previousRoll = 0
currentBet = 0
numberOfWins = 0
numberOfLosses = 0
currentBank = 10000
die1 = Die()
die2 = Die()

currentBet = int(input("How much would you like to bet? "))

while currentBet > 0:
    if firstRoll:
        rollValue = die1.roll() + die2.roll()
        print("You rolled a {0}".format(rollValue))
        if rollValue in (2, 3, 12):
            print("You lost.")
            numberOfLosses += 1
            currentBank -= currentBet
        elif rollValue in (7, 11):
            print("You won!")
            numberOfWins += 1
            currentBank += currentBet
        else:
            previousRoll = rollValue
            firstRoll = False
    else:
        rollValue = die1.roll() + die2.roll()
        print("You rolled a {0} and you needed a {1}".format(rollValue, previousRoll))
        if rollValue == previousRoll:
            print("You won!")
            numberOfWins += 1
            currentBank += currentBet
        else:
            print("You lost!")
            numberOfLosses += 1
            currentBank -= currentBet
        firstRoll = True
    if firstRoll:
        currentBet = int(input("how much would you like to bet? "))
