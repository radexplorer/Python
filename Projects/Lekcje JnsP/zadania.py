# amount1 = int(input("podaj liczbe: "))
# amount2 = int(input("podaj liczbe2: "))


# if amount1 > 10 and amount2 < 100:
#     print(max(amount1, amount2))
# else:
#     print("wprowadz liczby z przedziały 10-100")

#######################################################################

# import turtle
# turtle.heading = float(input("podaj kąt: "))
# if turtle.heading >= 0 and turtle.heading <= 45:
#     turtle.pendown()
# else:
#     print("Wprowadz kąt 0-45")

#######################################################################

# day = int(input("Podaj liczbe 1-7: "))

# if day <= 1:
#     print("poniedziałek")
# elif day <= 2:
#     print("wtorek")
# elif day <= 3:
#     print("sroda")
# elif day <= 4:
#     print("czwartek")
# elif day <= 5:
#     print("piątek")
# elif day <= 6:
#     print("sobota")
# elif day <= 7:
#     print("niedziela")
# else:
#     print("nieprawidłowa liczba")

#########################################################################

# width1 = float(input("podaj szerokość 1 prostokąta "))
# height1 = float(input("podaj wysokość 1 prostokąta "))
# width2 = float(input("podaj szerokość 2 prostokąta "))
# height2 = float(input("podaj wysokość 2 prostokąta "))

# area1 = width1*height1
# area2 = width2*height2

# if area1 > area2:
#     print("area1 is bigger than area2")
# elif area1 < area2:
#     print("area2 is bigger than area1")
# else:
#     print("area1 and area2 are equal")

##########################################################################

# arabic = int(input("Podaj liczbę 1-10: "))

# if arabic <= 1:
#     print("W zapisie rzymskim to I")
# elif arabic <= 2:
#     print("W zapisie rzymskim to II")
# elif arabic <= 3:
#     print("W zapisie rzymskim to III")
# elif arabic <= 4:
#     print("W zapisie rzymskim to IV")
# elif arabic <= 5:
#     print("W zapisie rzymskim to V")
# elif arabic <= 6:
#     print("W zapisie rzymskim to Vi")
# elif arabic <= 7:
#     print("W zapisie rzymskim to VII")
# elif arabic <= 8:
#     print("W zapisie rzymskim to ViII")
# elif arabic <= 9:
#     print("W zapisie rzymskim to IX")
# elif arabic <= 10:
#     print("W zapisie rzymskim to X7")
# else:
#     print("błąd")

###############################################################################

# mass = int(input("Podaj masę obiektu: "))

# weight = mass*9.8

# if mass > 500:
#     print("Too heavy")
# elif mass < 100:
#     print("Too light")
# else:
#     print("correct weight")

###############################################################################

# day = int(input("Podaj dzień: "))
# month = int(input("Podaj miesiąc: "))
# year = int(input("Podaj rok(dwie ostatnie cyfry): "))

# if (day*month) == year:
#     print("It's a magic number")
# else:
#     print("It's an ordinary number")

##############################################################################

# guests = int(input("how many guests will be at the party: "))

# packs_of_sausages = int(guests/10)
# rest_of_sausages = int(guests % 10)
# print("paczek parówek: ", packs_of_sausages)
# print("niewykorzystane parówki: ", rest_of_sausages)
# print("ilość patrzebnyh opakowań parówek: ", packs_of_sausages+1)

################################################################################

# ♦

#################################################################################

# amount_products = int(input("How many products you want to buy: "))
# total_value = amount_products*99

# if amount_products >= 10 and amount_products <= 19:
#     print(total_value*(0.9))
# elif amount_products >= 20 and amount_products <= 49:
#     print(total_value*(0.8))
# elif amount_products >= 50 and amount_products <= 99:
#     print(total_value*(0.7))
# elif amount_products >= 100:
#     print(total_value*(0.6))
# else:
#     print(total_value)

#################################################################################

# seconds = int(input("how many second: "))
# minutes = int(seconds/60)
# print(minutes, "minut", (seconds % 60), "sekund")
# hours = int(seconds/3600)
# print(hours, "godzin", (minutes-hours*60), "minut", (seconds % 60), "sekund")
# days = int(seconds/86400)
# print(days, "dni", (hours-days*24), "godzin",
#       (minutes-hours*60), "minut", (seconds % 60), "sekund")

##################################################################################

# year = int(input("Podaj rok: "))

# if ((year % 100 == 0) and (year % 400 == 0)) and ((year % 100 != 0) and (year % 4 == 0)):
#     print("rok przestępny, luty ma 29dni")
# else:
#     print("rok ma 28dni")

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("29")
# else:
#     print("28")

#####################################################################################


