import random
# obige Zeile importiert das komplette Modul ranom mit allen Funktionalitäten
# das hat zur Folge, dass die einzelnen Methoden in folgender Form aufgerufen werden müssen:
#  random.methode()
#
# Die folgende Zeile importiert ausschliesslich die beiden Methoden randint und random.
# Diese Methoden können dann direkt aufgerufen werden, ohne random. davor schreiben zu müssen.
#
# from random import randint, random
#
# Imports sollten immer am Anfang der Datei stehen -> guter Stil


zufallszahl = random.randint(0, 10)   # Zufalls-Integer zwischen 0 und 10 inklusive
# zufallszahl = randint(0, 10)   # Zufalls-Integer zwischen 0 und 10 inklusive
print("randint: " + str(zufallszahl))

zufallszahl = random.random()          # Zufalls-Float zwischen 0 bis 1
# zufallszahl = random()          # Zufalls-Float zwischen 0 bis 1
print(f"{ zufallszahl = }")
zufallszahl = zufallszahl * 100
print(zufallszahl)

# zufallszahl = random.gauss(3, 10)
# print(zufallszahl)

# zufallszahl = random.uniform(1, 10)
# print(zufallszahl)

