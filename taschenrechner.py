# Auswahlmenu anzeigen
auswahlmenu = """
Welche Rechenoperation soll durchgeführt werden?

[1] addition (+)
[2] subtraktion (-)
[3] mulitplikation (*)
[4] division (/)

"""


# Benutzer nach der gewünschten Rechenoperation fragen
eingabe = input(auswahlmenu)

# Benutzer nach zwei Zahlen fragen
# Falls es beim Casting zu einem Fehler (Exception) kommen sollte,
# entsprechende Meldung ausgeben und Programm beenden
try:
    zahl1 = float(input("Bitte erste Zahl eingeben: "))
    zahl2 = float(input("Bitte zweite Zahl eingeben: "))
except Exception:
    print("ERROR: Beim Casting ist ein Fehler aufgetreten!")
    print("Programm wird beendet.")
    exit(1)

if eingabe == "1":
    print("Addition")
    # Rechenoperation durchführen
    ergebnis = zahl1 + zahl2
    print("Das Ergebnis der Addition von " + str(zahl1) + " und " + str(zahl2) + " ist " + str(ergebnis))
elif eingabe == "4":
    print("Division")
    # Benutzer nach zwei Zahlen fragen
    # Redundanz -> (immer) zu vermeiden!
    # zahl1 = input("Bitte erste Zahl eingeben: ")
    # zahl2 = input("Bitte zweite Zahl eingeben: ")
    # NOTE: Division durch 0 ist nicht erlaubt -> Prüfung
    if zahl2 != 0.0:
        ergebnis = zahl1 / zahl2
        print("Das Ergebnis der Division von " + str(zahl1) + " und " + str(zahl2) + " ist " + str(ergebnis))
    else:
        print("Die Division durch 0 ist nicht zulässig!")
else:
    print("Falsche Eingabe. Bitte eine Zahl zwischen 1 und 4 eingeben.")