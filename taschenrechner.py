# Auswahl(menu) anzeigen
# Benutzer nach Rechenoperation fragen
auswahlmenu = """
Welche Rechenoperation soll durchgeführt werden?

[1] addition (+)
[2] subtraktion (-)
[3] mulitplikation (*)
[4] division (/)
"""

eingabe = input(auswahlmenu)

# Wenn Auswahl richtig
if eingabe == "1":
    print("addition")
    # Benutzer nach zwei Zahlen fragen
    zahl1 = input("Bitte erste Zahl eingeben: ")
    zahl2 = input("Bitte zweite Zahl eingeben: ")
    # Rechenoperation durchführen
    ergebnis = float(zahl1) + float(zahl2)
    # NOTE: Beste Stelle zur Ausgabe von ergebnis?
    print(ergebnis)
else:
    print("Falsche Eingabe")
# Ergebnis ausgeben