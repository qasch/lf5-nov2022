# Auswahl(menu) anzeigen
# Benutzer nach Rechenoperation fragen
auswahlmenu = """
Welche Rechenoperation soll durchgeführt werden?

[1] addition (+)
[2] subtraktion (-)
[3] mulitplikation (*)
[4] division (/)
"""

# NOTE: Division durch 0 ist nicht erlaubt!

eingabe = input(auswahlmenu)

# Benutzer nach zwei Zahlen fragen
zahl1 = input("Bitte erste Zahl eingeben: ")
zahl2 = input("Bitte zweite Zahl eingeben: ")

# Wenn Auswahl richtig
if eingabe == "1":
    print("addition")
    # TODO: Eingabe prüfen!
    # Rechenoperation durchführen
    ergebnis = float(zahl1) + float(zahl2)
    # NOTE: Beste Stelle zur Ausgabe von ergebnis?
    print(ergebnis)
elif eingabe == "4":
    print("division")
    # Benutzer nach zwei Zahlen fragen
    # Redundanz -> (immer) zu vermeiden!
    # zahl1 = input("Bitte erste Zahl eingeben: ")
    # zahl2 = input("Bitte zweite Zahl eingeben: ")
    # TODO: Eingabe prüfen!
    # Rechenoperation durchführen
    if zahl2 != "0":
        ergebnis = float(zahl1) / float(zahl2)
        print("Das Ergebnis der Division ist " + str(ergebnis))
    else:
        print("Division durch 0 ist nicht zulässig.")
    # NOTE: Beste Stelle zur Ausgabe von ergebnis?
else:
    print("Falsche Eingabe")
# Ergebnis ausgeben