name = "radek"
# print(len(name))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name[0:4])
# print(name[-3])
# print(name[-3:])

miasto = "Czechowice - Dziedziece"
# print(miasto.split(" "))
join_string = " "
# print(join_string.join(['jak', 'nau', 'sie', 'prg']))

print(name.startswith("r"))
print(name.endswith("k"))
print(name.rstrip("k"))
print(name.lstrip("r"))
print(name.strip())  # usuwa spacje

print(name + " " + miasto)

print(join_string.join([name, miasto]))

james_bond = 7
print(str(james_bond).zfill(3))
