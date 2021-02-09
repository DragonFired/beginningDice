#!/usr/bin/env python
__author__ = "Arana Fireheart"

from die import *

trialsList = [(6, 1, 1, "Purple", "Die"), (10, 0, 1, "Purple", "Die"), (12, 1, 12, "Red", "Fred")]
valueList = []
for sides, start, step, color, name in trialsList:
    valueList.clear()
    die1 = Die(sides, start, step, color, name)
    # die1 = Die(6, 1, 1, "Purple", "Die")
    print(die1)
    for number in range(0, 30):
        valueList.append(die1.roll())
    print(valueList)
    print()

print(die1)
die1.setValue(24)
print("Value {0}".format(die1.getValue()))
print(die1)

print(die1)
try:
    die1.setValue(10)
except ValueError:
    print("Bad set low value was ignored")
print("Value {0}".format(die1.getValue()))
print(die1)

print(die1)
try:
    die1.setValue(150)
except ValueError:
    print("Bad set high value was ignored")
print("Value {0}".format(die1.getValue()))
print(die1)

print(die1)
try:
    die1.setValue(140)
except ValueError:
    print("Bad set increment value was ignored")
print("Value {0}".format(die1.getValue()))
print(die1)

print(die1)
die1.setNumberOfSides(10)
print("Sides {0}".format(die1.getNumberOfSides()))
print(die1)

print(die1)
die1.setStartingValue(10)
print("Starting {0}".format(die1.getStartingValue()))
print(die1)

print(die1)
die1.setIncrement(10)
print("Increment {0}".format(die1.getIncrement()))
print(die1)

print(die1)
die1.setColor("Blue")
print("Color {0}".format(die1.getColor()))
print(die1)

try:
    die1.setColor(140)
except ValueError:
    print("Bad set color value was ignored")

print(die1)
die1.setName("Sleepy")
print("Name {0}".format(die1.getName()))
print(die1)

try:
    die1.setName(140)
except ValueError:
    print("Bad set name value was ignored")
