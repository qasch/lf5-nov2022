# Schleifen - Loops

bedingung = True

while bedingung == True:
    print("haha")
    bedingung = False

# Benutzername und Passwort dreimal eingeben
# zaehler = 0
# while zaehler < 3:
#     login = input("Benutzername: ")
#     pw = input("Passwort: ")
#     # zaehler = zaehler + 1
#     zaehler += 1                # Kurzschreibweise obige Zeile

# Achtung: Endlosschleife, da durch die fehlende Einrückung
# die Variable zaehler nie verändert wird -> häufige Fehlerquelle
# while zaehler < 3: #     login = input("Benutzername: ")
#     pw = input("Passwort: ")
# zaehler += 1

# pw = ""
# while not pw == "supersecret":
#     pw = input("Passwort: ")
# print("Das war das richtige Passowrt!")

"""
*
**
***
****
*****
"""

anzahl = 1
while anzahl <= 5:
    print(anzahl * "*")
    anzahl += 1

"""
   *
  ***
 *****
*******
   |
"""


# Benuzer so lange nach einer Zahl fragen, bis wirklich eine 
# Zahl eingegeben wird
# dann wird die Schleife verlassen und mit dem Rest des Codes
# weitergemacht
while True:
    zahl = input("Bitte gib eine Zahl ein: ")
    if zahl.isdigit():
        zahl = int(zahl)
        print("Casting erfolgreich")
        break     # mit dem Schlüsselwort break wird die Schleife verlassen, 
                  # Code nach der Schleife wird ausgeführt
                  # Ansonsten wird die Schleife immer wieder ausgeführt und 
                  # nie verlassen
                  # continue überspringt den Rest des Loops für diesen einen 
                  # Durchgang, verlässt den Loop aber nicht
    print("Ungültige Eingabe")

zahl = zahl + 2
print(zahl)





