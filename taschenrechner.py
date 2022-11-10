while True:
    # Auswahlmenu anzeigen
    auswahlmenu = """
    Welche Rechenoperation soll durchgeführt werden?

    [1] addition (+)
    [2] subtraktion (-)
    [3] mulitplikation (*)
    [4] division (/)

    [q] Programm beenden

    """


    # Benutzer nach der gewünschten Rechenoperation fragen
    eingabe = input(auswahlmenu)

    # Programm beenden
    # muss an dieser Stelle stehen, da ansonsten versucht wird,
    # zahl1 und zahl2 zu caste etc.
    if eingabe == "q":
        print("Uuuuund tschüss...")
        exit(0)

    # Benutzer nach zwei Zahlen fragen
    # Falls es beim Casting zu einem Fehler (Exception) kommen sollte,
    # entsprechende Meldung ausgeben und Programm beenden
    try:
        zahl1 = float(input("Bitte erste Zahl eingeben: "))
        zahl2 = float(input("Bitte zweite Zahl eingeben: "))
    except ValueError as e:
        print("ERROR: Beim Casting ist ein Fehler aufgetreten: " + e.args[0])
        # print("Programm wird beendet.")
        # exit(1)   # Beende das Programm, gib zurück, dass es zu einem Fehler gekommen ist.
        continue    # Alternative: Zeige Auswahlmenu anstatt Programm zu beenden.
    except Exception:
        print("Es ist irgendein anderer Fehler aufgetreten")

    if eingabe == "1":
        rechenoperation ="Addition"
        ergebnis = zahl1 + zahl2
    elif eingabe == "2":
        rechenoperation ="Subtraktion"
        ergebnis = zahl1 - zahl2
    elif eingabe == "3":
        rechenoperation ="Mulitplikation"
        ergebnis = zahl1 * zahl2
    elif eingabe == "4":
        rechenoperation = "Division"
        # Benutzer nach zwei Zahlen fragen
        # Redundanz -> (immer) zu vermeiden!
        # zahl1 = input("Bitte erste Zahl eingeben: ")
        # zahl2 = input("Bitte zweite Zahl eingeben: ")
        # NOTE: Division durch 0 ist nicht erlaubt -> Prüfung
        # if zahl2 != 0.0:
        #     ergebnis = zahl1 / zahl2
        # else:
            # print("Die Division durch 0 ist nicht zulässig!")
        # NOTE: Besserer Weg als oben: Benutzer kann wiederholt die zweite Zahl eingeben
        while zahl2 == 0:
            print("Die Division durch 0 ist nicht zulässig!")
            zahl2 = float(input("Zahl 2 darf nicht 0 sein. Bitte erneut eingeben: "));
        else:
            ergebnis = zahl1 / zahl2
    else:
        print("Falsche Eingabe. Bitte eine Zahl zwischen 1 und 4 eingeben.")

    # Ausgabe des Ergebnisses mit Stringkonkatenation
    # print("Das Ergebnis der " + rechenoperation + " von " + str(zahl1) + " und " + str(zahl2) + " ist " + str(ergebnis))

    # Ausgabe des Ergebnisses mit String Format
    # print("Das Ergebnis der {0} von {1} und {2} ist {3}.".format(rechenoperation, zahl1, zahl2, ergebnis))

    # Ausgabe mit F-String
    print(f"Das Ergebnis der {rechenoperation} von {zahl1} und {zahl2} ist {ergebnis}.")


