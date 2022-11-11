# Addierer

# zwei Variablen
# Benutzer soll diese eingeben können
zahl1 = input("Bitte Zahl1 eingeben: ")   # input gibt *immer* einen String zurück
zahl2 = input("Bitte Zahl2 eingeben: ")   # wollen wir einen Integer haben, müssen wir den String in 
                                          # einen Integer umwandeln/casten (-> explizites Casting)


#print("Datentypen von zahl1 und zahl2 vor dem Casting:")
#print(type(zahl1))
#print(type(zahl2))

# Casting von String in Integer (Wert wird nicht verändert)
# extra Schritt, können wir uns sparen (wenn wir wollen, kein Muss)
#zahl1 = int(zahl1)
#zahl2 = int(zahl2)

print("Datentypen von zahl1 und zahl2 nach dem Casting:")
zahl1 = input("Bitte Zahl1 eingeben: ")   # input gibt *immer* einen String zurück
zahl2 = input("Bitte Zahl2 eingeben: ")   # wollen wir einen Integer haben, müssen wir den String in 
                                          # einen Integer umwandeln/casten (-> explizites Casting)

#print("Datentypen von zahl1 und zahl2 vor dem Casting:")
#print(type(zahl1))
#print(type(zahl2))

# Casting von String in Integer (Wert wird nicht verändert)
# extra Schritt, können wir uns sparen (wenn wir wollen, kein Muss)
#zahl1 = int(zahl1)
#zahl2 = int(zahl2)
zahl1 = input("Bitte Zahl1 eingeben: ")   # input gibt *immer* einen String zurück
zahl2 = input("Bitte Zahl2 eingeben: ")   # wollen wir einen Integer haben, müssen wir den String in 
                                          # einen Integer umwandeln/casten (-> explizites Casting)

#print("Datentypen von zahl1 und zahl2 vor dem Casting:")
#print(type(zahl1))
#print(type(zahl2))

# Casting von String in Integer (Wert wird nicht verändert)
# extra Schritt, können wir uns sparen (wenn wir wollen, kein Muss)
#zahl1 = int(zahl1)
#zahl2 = int(zahl2)
zahl1 = input("Bitte Zahl1 eingeben: ")   # input gibt *immer* einen String zurück
zahl2 = input("Bitte Zahl2 eingeben: ")   # wollen wir einen Integer haben, müssen wir den String in 
                                          # einen Integer umwandeln/casten (-> explizites Casting)

#print("Datentypen von zahl1 und zahl2 vor dem Casting:")
#print(type(zahl1))
#print(type(zahl2))

# Casting von String in Integer (Wert wird nicht verändert)
# extra Schritt, können wir uns sparen (wenn wir wollen, kein Muss)
#zahl1 = int(zahl1)
#zahl2 = int(zahl2)
print(type(zahl1))
#print(type(zahl2))

# beide Variablen addieren                
# Ergebnis in Variable ergebnis ablegen
ergebnis = float(zahl1) + float(zahl2)
# ergebnis ausgeben
# Die Summe von zahl1=kontreter Wert und ... ist : ergebnis
#print(ergebnis)
print("Die Summe von", zahl1, "und", zahl2, "ist:", ergebnis)
print("Die Summe von " + zahl1 + " und " + zahl2 + " ist: " + str(ergebnis))

#print("Ergebnis: " + ergebnis)  # führt zu Fehler
