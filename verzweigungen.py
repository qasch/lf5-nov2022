name1 = "kai"
name2 = "gretl"

alter1 = 43
alter2 = 9

wesen1 = "Mensch"
wesen2 = "Hund"

eingabe = input("Bitte einen Namen eingeben: ")

# falls eingabe == kai
# der folgende Code-Block wird ausgeführt, wenn die Bedingung True ist
if eingabe == "kai" or eingabe == "Kai":    
    # Der Code-Block wird über Einrückungen (4 Leerzeichen) definiert
    print("Du bist " + name1)
    print("Du bist ein " + wesen1)
elif eingabe == "gretl":       # elif wird nur geprüft, wenn das erste if False ist
    print("Du bist " + name2)
    print("Du bist ein " + wesen2)
else:
    print("Du bist unbekannt.")  



print("Ende des Programms")