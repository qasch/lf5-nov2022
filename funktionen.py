# Eigene Funktinen erstellen und nutzen
# Rückgabetypen, Güligkeitsbereich von Variablen

# Erstellen einer Funktion mit dem Schlüsselwort def -> define
# Deklaration der Funktion
def gib_etwas_aus():
    print("gib")
    print("etwas")
    print("aus")

# text ist ein Übergabeparameter
# innerhalb der Funktion ist text als Variable bekannt
def gib_aus_was_ich_uebergebe(text):
    print(text)


# Führt zu Fehler, da der Aufruf vor der Deklaration stattfindet
# Definition ab Zeile 24
# addiere(3, 3)   

# werden bei der Funktionsdeklaration zwei Parameter angegeben,
# müssen beim Aufruf der Funktion auch die gleiche Anzahl an
# Argumenten übergeben werden
def addiere(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    # print(ergebnis) # String wird ausgedruckt
    return ergebnis  # Inhalt von Ergebnis wird zurückgegeben

# Aufruf der Funktionen
gib_etwas_aus()

gib_aus_was_ich_uebergebe("hallo")

# da addiere etwas zurückgibt, können/müssen wir selbst entscheiden,
# wie wir mit dem Ergebnis weiter verfahren wollen
# wir können es z.B. ausgeben lassen mit print()
print(addiere(3, 4))
print(addiere(1234, 1234))
print(addiere(3, 3))

# Funktionen können auch innerhalb anderer Funktionen genutzt werden
# Man sollte also darauf achten, Funktionen möglichst generisch, also 
# vielseitig verwendbar zu definieren
def verdopple_addition():
    foo = addiere(3, 4)
    ergebnis = foo * 2
    return ergebnis

print(verdopple_addition())


## Gülitgkeitsbereich von Variablen an Beispielen:

# Leerzeile
print()

# Folgender Code führt zu Fehler, da *lokale* Variable var die globale Variable var überlagert
# var = "Variable"
# def gueltigkeitsbereich():
#     var = var + "ngueltigkeitsbereich"   
#     return var
#
# print(gueltigkeitsbereich())
# print(var)   # enthält immer noch "Variable"

# var = "Variable"
# def gueltigkeitsbereich():
#     var = "Variable"
#     var = var + "ngueltigkeitsbereich"
#     return var
#
# print(gueltigkeitsbereich())  # gibt Variablengueltigketsbereich aus
# print(var)   # gibt "Variable" aus


# var = "Variable"
# def gueltigkeitsbereich():
#     global var    # durch global können wir die globale Variable var nutzen und ändern
#     var = var + "ngueltigkeitsbereich"
#     return var
#
# print(gueltigkeitsbereich())  # gibt Variablengueltigketsbereich aus
# print(var)                    # gibt Variablengueltigketsbereich aus

var = "Variable"
def gueltigkeitsbereich():
    global var
    var = var + "ngueltigkeitsbereich"

# print(gueltigkeitsbereich())  # git None aus, da kein return, also kein Rückgabetyp 
# print(var)                    # gibt Variablengueltigketsbereich aus, globale Variable wurde also geändert




# Beispiel einer Funktion mit Rückgabetyp int in Java
#
# int addiere(int zahl1, int zahl2){
#     int ergebnis = zahl1 + zahl2;
#     #System.out.println(ergebnis);
#     return ergebnis;
# }
