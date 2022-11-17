# Dateizugriff unter Python

# 1. Datenstrom erzeugen / Datei öffnen, Zugriffsmodus festlegen
# 2. Datei bearbeiten (lesen/schreiben...)
# 3. Datenstrom schliessen

# Unterschied relativer/absoluter Pfad:
#  relativer Pfad: ausgehend vom aktuellen Verzeichnis (in dem sich die Datei befindet)
#  absoluter Pfad (Windows): C:\code\python\.vscode\settings.json
#  absoluter Pfad (Linux): ~/code/python/.vscode/settings.json

# Dateimodus:
#   r : lesen
#   w : schreiben, Datei erstellen, falls nicht vorhanden -> Inhalt wird überschrieben!
#   x : Datei anlegen
#   a : schreiben, Datei erstellen, falls nicht vorhanden -> Inhalt wird angehängt
#   + : lesend und schreibend (rw)
#   b : Binärmodus
#   t : Textmodus (Default)

# try - except nicht vergessen!
# write/append
try:
    # 1. Datenstrom erzeugen / Datei öffnen, Zugriffsmodus festlegen
    file = open("datei.txt", "a")

    # 2. Datei bearbeiten (schreiben)
    file.write("Zweite Zeile\n")

    # 3. Datenstrom schliessen
    file.close()
except IOError as e:
    print("Fehler beim Lesen der Datei", e)

# read
try:
    file = open("datei.txt", "r")

    content = file.read()
    print(content)

    file.close()
except IOError as e:
    print("Fehler beim Lesen der Datei", e)
