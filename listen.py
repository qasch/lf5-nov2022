# Lists in Python

# Listen sind Datenstrukturen, die mehrere Werte aufnehmen können
# In anderen Sprachen oft als Array bekannt

# index    0  1  2     3  4
my_list = [4, "hallo", True, 1.23324, 1, 1234, 2342342, 234 , 1223]

# print(type(my_list))

print("ganze List: ", my_list)
print()
print("Index 0, Element 1: ", my_list[0])
print("Index 1, Element 2: ", my_list[1])
print("Index 2, Element 3: ", my_list[2])
print("Index 3, Element 4: ", my_list[3])
print("Index 4, Element 5: ", my_list[4])

# Fehleranfällig, abhängig von der Anzahl der Elemente der List (hier 11)
# counter = 0
# while counter < 11:
#     print(my_list[counter])
#     counter += 1

# print(len(my_list))          # len() gibt hier die Anzahl der *Elemente* der Liste zurück

# counter = 0
# while counter < len(my_list):
#     print(my_list[counter])
#     counter += 1


# for element in my_list:
#     print(element)


# number = 0
# while number <= 10:
#     print(number)
#     number += 1


for number in range(0, 11):     # Obergrenze bei range() ist exklusive, also nicht enthalten
    print(number)

# number ist ein beliebig gewählter Name der Zählvariable

# _ ist eine *anonyme* Variable
# for _ in range(11):     # Obergrenze bei range() ist exklusive, also nicht enthalten
#     print(_)

for number in range(0, 11, 2):     # 2 gibt hier die Höhe des Inkrements (Step) an
    print(number)



# # JAVA  - Beispiel für eine for-Schleife
# for(int i; i < 11; i++){
#     System.out.println(i);
# }
