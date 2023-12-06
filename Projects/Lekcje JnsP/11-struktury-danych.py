names_list = []
names_list.append("Radosław")
names_list.append("Paulina")
names_list.append("Małgosia")

print(names_list)

# names_list.reverse()

names_list.sort()
names_list[0]
print(names_list.count("Paulina"))
print(len(names_list))
print(names_list.pop(1))

names_list2 = ["Błażej", "Kasia", "Basia"]

names_list3 = names_list + names_list2

names_list3.sort(reverse=True)

print(names_list3)

# metoda .remove usuwa pierwsze wystąpienie arg w liście

# metoda .clear czyści listę

# metoda .

for name in names_list:
    print(name)


########################################################################################

# KROTKA = lista z okrągłymi nawiasami
# Krotka jest NIEZMIENIALNA

person = ("Palina", "Głowacka", 29)
print(person.count(29))

# Krotka nie może być pusta!!!!

#########################################################################################

# SET
# Nie może być zduplikowanych danych
# nawiasy klamrowe

names_set = set()
names_set.add("kamil")
names_set.remove("kamil")  # wyskoczy błąd
names_set.discard("kamil")  # nie wyskkoczy błąd


# elementy nie sa uporządkowane (worek losu losu)
# nie można dodać listy do krotki
# niemitowalne
# set to ZBIÓR


names_set2 = {"Beata", "Ania", "Kasia"}
names_set3 = {"Gienek", "Radek", "Paula"}
names_set4 = names_set2.union(names_set3)
names_set4.symmetric_difference(names_set2)
print(names_set4)

# .difference usuwa drugi set z pierwszego set
# .intersection szuka części wspólnej
# .symetric difference elementy spoza części wspólnej

# DODAWANIE LISTY DO SETA
print(names_list2)
names_list2.extend(names_set4)
print(names_list2)

############################################################################################

# DICTIONARY - SŁOWNIK

# Pierwsze to keys,
# Drugie to values

countries_and_capitals = {"Poland": "Warasaw", "France": "Paris"}

countries_and_capitals['Italy'] = "Romek"

print(countries_and_capitals)

for country in countries_and_capitals.keys():
    print(country)

for capital in countries_and_capitals.values():
    print(capital)

for country, capital in countries_and_capitals.items():
    print(country + " - " + capital)

# print(countries_and_capitals["Poland"])
# print(countries_and_capitals.get("Poland"))
print(countries_and_capitals.setdefault("USA", "Washington"))

countries_and_capitals["Poland"] = "Cracov"
print(countries_and_capitals)


if "Poland" in countries_and_capitals.keys():
    print("Znaleziono")
else:
    print("nie znaleziono")

print("Poland" in countries_and_capitals)
