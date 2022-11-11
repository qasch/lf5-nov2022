# Umgang mit Lists in Python - Methoden

my_list = []

print(my_list)

# my_list = ["Hund"]

# my_list = ["Hund", "Kanarienvogel"]

# Die Methode append() der Klasse list fügt den übergebenen Wert an die List an
my_list.append("hund")
print(my_list)

my_list.append("kanarienvogel")
print(my_list)

my_list.append(2.12343)
print(my_list)

# # Führt zu Fehler, da versucht wird, ein Index anzusprechen, der nicht existiert
# my_list[7] = "meerschweinchen"
# print(my_list)


## Element aus der List entfernen, diese wird automatisch verkleinert
my_list.remove("kanarienvogel")
print(my_list)

my_list.append("schildkroete")
print(my_list)

gepoppt = my_list.pop(1)
print(my_list)
print(gepoppt)
print(my_list.pop(1))
print(my_list)

my_list.append("kanarienvogel")
my_list.append("schildkroete")
print(my_list)

# print(my_list.index("kanarienvogel"))
# umständlicher Weg, das Verhalten von remove() zu imitieren
my_list.pop(my_list.index("kanarienvogel"))
print(my_list)

my_list.append("affe")
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

other_list = ["Biene", "Hummerl", "Eichhörnchen"]
print(other_list)

new_list = my_list + other_list
print(new_list)


# Strings sind "etwas ähnliches" wie Lists:
my_string = "Ich bin ein String"

for i in my_string:
    print(i)

print()
print()
print()
# Einen einzelnen Buchstaben aus dem String ausgeben
# Hinweis: Recherchiert mal String Manipulationen in Python
print(my_string[1])

print()
print()
print()

# my_list wird um die Elemente von other_list erweitert
# my_list wird also verändert
my_list.extend(other_list)
print(my_list)

print()

# Fügt "Biber" an Index 3 in die List ein, List wird also vergrössert 
my_list.insert(3, "Biber")
print(my_list)



# List mit 100 zufällig generierten Elementen