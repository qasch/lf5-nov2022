# Umgang mit Lists in Python - Methoden

# leere List erstellen
my_list = []

# String Repräsentation der List ausgeben
print(my_list)

# Wert/Element "Hund" zur List hinzufügen bzw. neue List mit dem Element "Hund" erstellen
# my_list = ["Hund"]
# my_list = ["Hund", "Kanarienvogel"]

# Die Methode append() der Klasse list fügt den übergebenen Wert an die List an
my_list.append("hund")
print(my_list)

my_list.append("kanarienvogel")
print(my_list)

my_list.append(2.12343)
print(my_list)

# Wert an Index 2 durch "meerschweinchen" ersetzen
my_list[2] = "meerschweinchen"
print(my_list)

# # Führt zu Fehler, da versucht wird, ein Index anzusprechen, der nicht existiert
# my_list[7] = "meerschweinchen"
# print(my_list)


# Element aus der List entfernen, diese wird automatisch verkleinert
# remove() erwartet den konkreten Wert des Elements
my_list.remove("kanarienvogel")
print(my_list)

my_list.append("schildkroete")
print(my_list)

# pop() entfernt ein Element am angegebenen Index
# und gibt diesen Wert gleichzeitig zurück
gepoppt = my_list.pop(1)
print(my_list)
print(gepoppt)
# ohne Argument wird das letzte Element entfernt
print(my_list.pop())
print(my_list)

my_list.append("kanarienvogel")
my_list.append("schildkroete")
print(my_list)

# umständlicher Weg, das Verhalten von remove() zu imitieren
# index() gibt den Index des übergebenen Elements zurück
my_list.pop(my_list.index("kanarienvogel"))
print(my_list)

my_list.append("affe")
print(my_list)

# sort() sortiert die List alphanumerisch
my_list.sort()
print(my_list)

# reverse() kehrt die Reihenfolge der Elemente der List um 
my_list.reverse()
print(my_list)

other_list = ["Biene", "Hummerl", "Eichhörnchen"]
print(other_list)

# Lists können auch mit dem + Operator verbunden werden (genauso wie Strings)
new_list = my_list + other_list
print(new_list)


# Strings sind "etwas ähnliches" wie Lists:
my_string = "Ich bin ein String"

# gibt alle Buchstaben aus my_string untereinander aus
for i in my_string:
    print(i)

print()

# Einen einzelnen Buchstaben aus dem String ausgeben
# Hinweis: Recherchiert mal zu "String Manipulation" in Python
print(my_string[0])  # Ausgabe: "I"

print()

# my_list um die Elemente von other_list erweitern
# my_list wird also verändert
my_list.extend(other_list)
print(my_list)

print()

# Fügt "Biber" an Index 3 in die List ein, List wird also vergrössert 
my_list.insert(3, "Biber")
print(my_list)


# List mit 100 zufällig generierten Elementen
from random import randint

# Leere List erstellen
generated_list = []

# # mit einer while Schleife
# counter = 0
# while counter < 100:
#     generated_list.append(randint(-100, 100))
#     counter += 1
#
# print(generated_list)

# wie oben nur mit for-Loop
for i in range(100):
    generated_list.append(randint(-100, 100))

print(generated_list)

print()

# pythonic way:
print([randint(0, 100) for i in range(100)])